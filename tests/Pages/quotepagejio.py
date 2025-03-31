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
    def health(self):
          
        log=self.getLogger()
        Ac = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        quote=homepagejio.HomePage
        quote.leads(self)
        prod=By.CSS_SELECTOR,"div.css-12hd50 p"
        product=wait.until(EC.presence_of_all_elements_located(prod))
        
        
        for podu in product:
                    pod=podu.text
                    if pod=="Health":   
                        podu.click()             
                        mobilin="Enter mobile number"
                        vehin=self.driver.find_element(By.ID,mobilin)
                        vehin.send_keys("7894566623")
                        pincode="Enter your pincode"
                        mobin=self.driver.find_element(By.ID,pincode)
                        mobin.send_keys("7017889834")
                        button="button#Get\ free\ quotes"
                        buttonquo=self.driver.find_element(By.CSS_SELECTOR,button)
                        buttonquo.click()
                        checkbox=By.CSS_SELECTOR,".css-j8yymo"
                        selectcheck=wait.until(EC.presence_of_all_elements_located(checkbox))
                        ra_slcheck=random.choice(selectcheck)
                        value=ra_slcheck.get_attribute("id")
                        if value=="Two Adults":
                         
                               
                         ra_slcheck.click()
                         time.sleep(5)
                        
                         

                         cont="#Continue"
                         conti=self.driver.find_element(By.CSS_SELECTOR,cont) 
                         conti.click()
                         time.sleep(5)
                        
                        #  if value=="two Adult":
                        #       id_adult="1st Adult Age-autocomplete"
                        #       age=self.driver.find_elements(By.ID,id_adult)
                        #       age.click()
                        #       ages=By.ID," Adult Age-autocomplete-listbox"
                        #       listage=wait.until(EC.visibility_of_all_elements_located(ages))
                        #       options = self.driver.find_elements(By.CSS_SELECTOR,"[role='option']")  # You can adjust this selector as per your DOM

                        #         # Step 4: Choose a random option from the list
                        #       random_option = random.choice(options)

                        #         # Step 5: Click the random option
                        #       random_option.click()
                        elif value=="One Adult":
                              
                         cont="#Continue"
                         conti=self.driver.find_element(By.CSS_SELECTOR,cont) 
                         conti.click()
                        
                         if value=="one Adult":
                              id_adult="1st Adult Age-autocomplete"
                              age=self.driver.find_elements(By.ID,id_adult)
                              age.click()
                              ages=By.ID," Adult Age-autocomplete-listbox"
                              listage=wait.until(EC.visibility_of_all_elements_located(ages))
                              options = self.driver.find_elements(By.CSS_SELECTOR,"[role='option']")  # You can adjust this selector as per your DOM

                                # Step 4: Choose a random option from the list
                              random_option = random.choice(options)

                                # Step 5: Click the random option
                              random_option.click()
                              

                        else:
                              continue


