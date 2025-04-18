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
from tests.test_data import test_data
from selenium.webdriver.common.keys import Keys

class UTM_Page(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def Utm_direct(self):
        url_utm=test_data.utm_links
        for utm_li in url_utm:
            self.driver.get(utm_li)
            if "google" in url_utm:
                search=By.CSS_SELECTOR,"div>textarea.gLFyf"
                ser=self.wait.until(EC.presence_of_element_located(search))
                ser.send_keys("policy bazzar"+Keys.ENTER)
                time.sleep(10)
                sponsored=".fP1Qef"
                all_sponsored=self.wait.until(EC.presence_of_all_elements_located(sponsored))
                for all_s in all_sponsored:
                    s_text=all_s.text
                    if "Sponsored" in s_text:
                        links=all_s.find_elements(By.TAG_NAME,"a")
                        for link in links:
                            li =link.get_attribute('href')
                            assert all(param in li for param in ["gbraid", "gad_source", "pb_campaign", "pb_term"])

                
