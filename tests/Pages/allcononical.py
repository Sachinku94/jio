from Pages import homepagejio
from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import test_data
import requests
import random
from Smoke_tests.object.Selenium_helper import SeleniumHelper
import threading
class cononical(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.ac = ActionChains(self.driver)
        self.log = self.getLogger()
    def allcononical(self):
        links = self.driver.find_elements(By.TAG_NAME,('a'))
        urls = [link.get_attribute('href') for link in links if link.get_attribute('href')]

    # 2. Iterate through each URL and check if canonical exists in the __next_f object
        missing_canonical_urls = []  # List to store URLs without canonical
        missing_next_f_urls = []      # List to store URLs where __next_f is missing

        for url in urls:
            # Navigate to the URL
            self.driver.get(url)

            # Wait for the page to load
           

            # Execute JavaScript to check for canonical URL in self.__next_f
            canonical_url = self.driver.execute_script("""
                if (typeof self.__next_f !== 'undefined') {
                    for (const item of self.__next_f) {
                        if (item[1] && item[1].rel === 'canonical') {
                            return item[1].href;  // Return the href of the canonical link
                        }
                    }
                }
                return null;  // If no canonical link is found, return null
            """)

            # Check if __next_f is available on the page
            next_f_available = self.driver.execute_script("""
                return typeof self.__next_f !== 'undefined';
            """)

            # If __next_f is not available, add the URL to missing_next_f_urls
            if not next_f_available:
                missing_next_f_urls.append(url)
            
            # If no canonical URL is found, add this URL to the missing_canonical_urls list
            if not canonical_url:
                missing_canonical_urls.append(url)

        # Print URLs that are missing the canonical link
        if missing_canonical_urls:
            print("The following URLs are missing a canonical link:")
            for url in missing_canonical_urls:
                print(url)

        # Print URLs where __next_f is missing
        if missing_next_f_urls:
            print("\nThe following URLs do not contain the __next_f object:")
            for url in missing_next_f_urls:
                print(url)

        # If all URLs have canonical links and __next_f is available, print this message
        if not missing_canonical_urls and not missing_next_f_urls:
            print("\nAll URLs have canonical links and the __next_f object is present.")