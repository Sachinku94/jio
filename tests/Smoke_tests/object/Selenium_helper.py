# In a file named selenium_helper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from concurrent.futures import ThreadPoolExecutor
from selenium.common.exceptions import TimeoutException
import inspect
import logging
import requests
import asyncio
import aiohttp
import time


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def fetch_css_properties_for_element(self, element, css_properties_list):
        """
        Helper function to fetch all specified CSS properties for a given element.
        :param element: Web element
        :param css_properties_list: List of CSS properties to fetch
        :return: Set of fetched CSS property values
        """
        return {
            element.value_of_css_property(css_property)
            for css_property in css_properties_list
        }

    async def fetch_css_properties_async(self, element, css_properties_list):
        """
        Asynchronously fetch CSS properties by offloading the blocking task to a thread pool.
        :param element: Web element
        :param css_properties_list: List of CSS properties to fetch
        :return: Fetched CSS properties as a set
        """
        loop = asyncio.get_event_loop()
        executor = ThreadPoolExecutor()
        return await loop.run_in_executor(
            executor,
            self.fetch_css_properties_for_element,  # use instance method directly
            element,
            css_properties_list,
        )

    async def fetch_and_check_css_properties(
        self, css_selector, expected_css_properties, css_properties_list
    ):
        """
        Optimized with asyncio: Fetches CSS properties from elements using the given CSS selector
        and checks them against expected values.
        :param css_selector: CSS selector to locate elements
        :param expected_css_properties: Set of expected CSS properties
        :param css_properties_list: List of CSS properties to fetch
        :return: True if the fetched properties match the expected properties, False otherwise
        """
        wait = WebDriverWait(self.driver, 20)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
        )

        try:
            fetched_css_properties = set()

            # Create a thread pool executor
            with ThreadPoolExecutor() as executor:
                # Schedule async tasks to fetch CSS properties for each element
                tasks = [
                    self.fetch_css_properties_async(element, css_properties_list)
                    for element in elements
                ]

                # Wait for all tasks to complete and gather results
                results = await asyncio.gather(*tasks)

            # Merge all fetched CSS properties
            for result in results:
                fetched_css_properties.update(result)

                # Early exit if all expected properties are fetched
                if fetched_css_properties == expected_css_properties:
                    return True

            # Final comparison after fetching all properties
            return fetched_css_properties == expected_css_properties

        except (StaleElementReferenceException, NoSuchElementException) as e:
            print(f"Error occurred: {str(e)}")
            return False

    def verify_links(self, selectors, additional_links, expected_link_count):
        all_links = []
        log = logging.getLogger()

        for selector in selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            links = [element.get_attribute("href") for element in elements]
            all_links.extend(links)

        if additional_links:
            all_links.extend(additional_links)

        for link in all_links:
            self.driver.execute_script("window.open(arguments[0])", link)

        handles = self.driver.window_handles
        opened_links = []
        result_broken = []

        for window in handles:
            self.driver.switch_to.window(window)
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            opened_links.append(self.driver.current_url)

        assert set(all_links) == set(opened_links) or (
            len(all_links) == len(opened_links) or expected_link_count
        )

        for link in opened_links:
            response = requests.get(link)
            status_code = response.status_code
            if status_code == 404:

                result_broken.append("fail")
                log.info(f"Link {link} is broken with status code {status_code}")

            elif status_code != 404:
                result_broken.append("pass")

        assert all(element == "pass" for element in result_broken)

    def verify_linkscloud(
        self,
        selectors,
    ):
        all_links = []
        log = logging.getLogger()

        for selector in selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            links = [element.get_attribute("href") for element in elements]
            all_links.extend(links)

        result_broken = []

        for link in all_links:
            response = requests.get(link)
            status_code = response.status_code
            if status_code == 404:

                result_broken.append("fail")
                log.info(f"Link {link} is broken with status code {status_code}")

            elif status_code != 404:
                result_broken.append("pass")

        assert all(element == "pass" for element in result_broken)

    async def check_link(session, link, log):
        try:
            async with session.head(link) as response:  # Using HEAD request
                status_code = response.status
                if status_code == 404:
                    log.info(f"Link {link} is broken with status code {status_code}")
                    return "fail"
                else:
                    return "pass"
        except Exception as e:
            log.error(f"Error checking link {link}: {e}")
            return "fail"

    # Define the asynchronous function to verify all links
    async def verify_links_async(self, selectors):
        all_links = []
        log = logging.getLogger()

        # Extract links using the provided selectors
        for selector in selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            links = [
                element.get_attribute("href")
                for element in elements
                if element.get_attribute("href")
            ]
            all_links.extend(links)

        # Check links asynchronously
        async with aiohttp.ClientSession() as session:

            tasks = [
                SeleniumHelper.check_link(session, link, log) for link in all_links
            ]
            results = await asyncio.gather(*tasks)

        # Verify if all links are okay
        assert all(result == "pass" for result in results), "Some links are broken."

    def get_pseudo_element_styles(self, element, pseudo_element, property_name):
        return self.driver.execute_script(
            f"""
        var element = arguments[0];
        var pseudo = window.getComputedStyle(element, "{pseudo_element}");
        return pseudo.getPropertyValue("{property_name}");
        """,
            element,
        )

    def remove_popup(self):
        """Checks for the pop-up periodically and removes it."""
        while True:
            try:
                modal = self.driver.find_element(By.CSS_SELECTOR, ".modal-scrollable .MuiPaper-root .modal-content.xsWidth")
                if modal:
                    print("Pop-up detected, closing it.")
                    close_button = modal.find_element(By.CSS_SELECTOR, ".MuiPaper-root .modal-content .closePopup")
                    close_button.click()
                    print("Pop-up closed.")
            except NoSuchElementException:
                pass
            print("Scheduled JavaScript pop-ups are cleared.")
    #     """Wait for the pop-up and remove it if it appears."""
    #     try:
    #         self.driver.execute_script("""
    #     window.alert = function() {};  // Disables alert pop-ups
    #     window.confirm = function() { return true; };  // Disables confirm pop-ups
    #     window.prompt = function() { return ''; };  // Disables prompt pop-ups
    # """)
    #     except:
    #         print("No pop-up found, proceeding.")

    def calander_picker(self, dob):
        """
        Improved function to select the date from the calendar.
        """
        # Split the dob into day, month, year
        month_map = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        
        day, month, year = dob.split('-')

        # Find and click the calendar input field
        calendar_field = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".evInputField .MuiInputBase-root .MuiIconButton-root")))
        calendar_field.click()

        # Explicit wait for the calendar to open
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1v994a0")))

        # Navigate to the correct year
        current_month_year = self.driver.find_element(By.CSS_SELECTOR, ".css-1v994a0")
        current_month, current_year = current_month_year.text.split()

        # Open the year dropdown
        year_select_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1wjkg3")))
        year_select_button.click()

        # Wait for the year dropdown to load
        year_elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-rhiqj0")))

        # Select the year from the dropdown
        for ye in year_elements:
            if ye.text == year:
                ye.click()
                break
        self.log.info("yer")
        time.sleep(4)
        # Wait for the calendar to update with the selected year
        while current_month != month or current_year != year:
            # Update the current displayed month and year
            

                # Navigate to the correct month using next/previous buttons
                current_month_year = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1v994a0")))
                current_month, current_year = current_month_year.text.split()
                self.log.info("done int")
                
                # Convert the month name to an integer using the month_map dictionary
                current_month_int = month_map[current_month]
                self.log.info("donemap")
                target_month_int = int(month)
                self.log.info(current_month_int)
                self.log.info(target_month_int)
                # Check if the current month is less than the target month or if the current year is less than the target year
                if current_month_int < target_month_int:
                    # Click "Next" month button
                    next_month_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1fklenr")))
                    next_month_button.click()
                    self.log.info('done')
                elif current_month > target_month_int:
                    # Click "Previous" month button
                    prev_month_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-11wxb")))
                    prev_month_button.click()
                    self.log.info("predone")
                
                # Wait for the calendar to update
                time.sleep(1)

                # Update the current month and year again after clicking
                current_month_year = self.driver.find_element(By.CSS_SELECTOR, ".css-1v994a0")
                current_month, current_year = current_month_year.text.split()

                # Convert again to int after the update
                current_month_int = month_map[current_month]

                # If current month matches the target month, break the loop
                if current_month_int == target_month_int:
                    break

        # Wait for the days to be visible
        days = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-a78wou")))

        # Select the specific day
        for alday in days:
            if alday.text.strip() == day:
                alday.click()
                break

        # Explicit delay before returning (optional, in case you need to wait for the UI to update)
        time.sleep(2)
