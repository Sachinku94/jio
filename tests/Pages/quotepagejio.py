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
class QuotePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
    def motor(self):
        log=self.getLogger()
        Ac = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        quote=homepagejio.HomePage
        quote.leads(self)
        prod=By.CSS_SELECTOR,"div.css-12hd50 p"
        product=wait.until(EC.presence_of_all_elements_located(prod))
        
        
        for podu in product:
                    pod=podu.text
                    if pod=="Car":
                    

                        vehino="Enter car registration number"
                        vehin=self.driver.find_element(By.ID,vehino)
                        vehin.send_keys("MH01WG7452")
                        mobino="Enter mobile number"
                        mobin=self.driver.find_element(By.ID,mobino)
                        mobin.send_keys("7894566623")
                        button="button#Get\ free\ quotes"
                        buttonquo=self.driver.find_element(By.CSS_SELECTOR,button)
                        buttonquo.click()
                        time.sleep(5)

                        br=By.ID,"#make"
                        brands=wait.until(EC.visibility_of_all_elements_located(br))
                        
                        
                        if brands:
                            time.sleep(4)
                        
                            ra_br=random.choice(brands)
                            ra_br.click()
                        time.sleep(5)
                        
                        
                            
                        vars=By.ID,"#model"
                        varints=wait.until(EC.visibility_of_all_elements_located(vars)) 
                        
                        if varints:
                                ra_vr=random.choice(varints)
                                ra_vr.click()
                                time.sleep(9)
                                log.info("trupass")
                              
                        
                        

