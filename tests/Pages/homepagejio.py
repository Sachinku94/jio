from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import test_data
import requests


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.view_more = "p.mb-3 a"

    # def login(self):

    #     links = []
    #     Ac = ActionChains(self.driver)
    #     wait = WebDriverWait(self.driver, 20)
    #     view_more = wait.until(
    #         EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.view_more))
    #     )
    #     time.sleep(10)
    #     for view in view_more:
    #         # Ac.move_to_element(view)

    #         # Ac.key_down(Keys.CONTROL).click(view).key_up(Keys.CONTROL).perform()

    #         # time.sleep(5)
    #         all_links = view.get_attribute("href")
    #         links.append(all_links)
    #     for li in links:
    #         self.driver.execute_script("window.open(arguments[0])", li)

    # def hover(self):
    #     Ac = ActionChains(self.driver)
    #     wait = WebDriverWait(self.driver, 20)
    #     hover = "a.more-link:hover"
    #     view_more = wait.until(
    #         EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.view_more))
    #     )
    #     for view in view_more:
    #         log = self.getLogger()
    #         Ac.move_to_element(view).context_click(view).perform()
    #         hovercolor = self.driver.find_element(By.CSS_SELECTOR, hover)
    #         hover_value = hovercolor.value_of_css_property("background-color")
    #         log.info(hover_value)
    #         assert hover_value == "rgba(119, 119, 119, 1)"

        

    def broken_img(self):
        images = []
        log = self.getLogger()
        imag = "img"
        all_images = self.driver.find_elements(By.TAG_NAME, imag)
        for image in all_images:
            sing_img = image.get_attribute("src")
            images.append(sing_img)
        for im in images:
            response = requests.get(im)

            assert response.status_code != 404
    def inter_link(self):
        log = self.getLogger()
        links = []
        Ac = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        interlinks=test_data.interlinks
        for test in interlinks:
            self.driver.get(test)
            view_more = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.view_more))
        )
            time.sleep(10)
            for view in view_more:
            # Ac.move_to_element(view)

            # Ac.key_down(Keys.CONTROL).click(view).key_up(Keys.CONTROL).perform()

            # time.sleep(5)
                all_links = view.get_attribute("href")
                links.append(all_links)
                
                log.info(all_links)
        log.info(links)
        assert links == test_data.interlinks_match
    
    def leads(self):
        time.sleep(10)

        dropdown=self.driver.find_element(By.CSS_SELECTOR,"div.css-1hyxel6 button")
        dropdown.click()
        
        

        




            
                

