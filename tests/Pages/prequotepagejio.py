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
class QuotePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.ac = ActionChains(self.driver)
        self.log = self.getLogger()

    def motor(self):
        drop_down = By.CSS_SELECTOR, ".css-t1oczc"
        self.wait.until(EC.presence_of_element_located(drop_down)).click()

        # Get the product list and select "Car"
        products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-12hd50 p")))
        for product in products:
            if product.text == "Car":
                product.click()
                break

        # Enter registration number and mobile number
        self.driver.find_element(By.ID, "Enter car registration number").send_keys("MH01WG7452")
        self.driver.find_element(By.ID, "Enter mobile number").send_keys("7894566623")

        # Click the 'Get free quotes' button
        self.driver.find_element(By.CSS_SELECTOR, "button#Get\\ free\\ quotes").click()

        # Wait for brands and select one at random
        brands = self.wait.until(EC.visibility_of_all_elements_located((By.ID, "make")))
        if brands:
            random.choice(brands).click()
        time.sleep(3)

        # Wait for variants (models) and select one at random
        varints = self.wait.until(EC.visibility_of_all_elements_located((By.ID, "model")))
        if varints:
            random.choice(varints).click()
        time.sleep(3)

        # Wait for radio buttons and select one at random
        radio_btns = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']")))
        if radio_btns:
            random.choice(radio_btns).click()

        # Wait for variant choices (cc) and select one at random
        varints_cc = self.wait.until(EC.presence_of_all_elements_located((By.ID, "variant_cc")))
        if varints_cc:
            random.choice(varints_cc).click()

        # Wait for the variant choices (list) and select one at random
        var_choices = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='css-djn3hl']/li")))
        if var_choices:
            random.choice(var_choices).click()
        cont=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Continue')]")))
        cont.click()

        # Log success (or any other relevant log you want)
        self.log.info("trupass")
        time.sleep(20)
    
        
        date=self.wait.until(EC.visibility_of_all_elements_located((By.ID,"datepicker")))
        for da in date:
            da.click()
            SeleniumHelper.calander_picker(self,dob="21-05-2023")
            cont.click()

        
        
        # drop_down=By.CSS_SELECTOR,".css-t1oczc"
        # dropc=self.wait.until(EC.presence_of_element_located(drop_down))
        # dropc.click()
        # products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-12hd50 p")))
        # for product in products:
        #         if product.text == "Car":
        #             product.click()
        #             break
        # vehino="Enter car registration number"
        # vehin=self.driver.find_element(By.ID,vehino)
        # vehin.send_keys("MH01WG7452")
        # mobino="Enter mobile number"
        # mobin=self.driver.find_element(By.ID,mobino)
        # mobin.send_keys("7894566623")
        # button="button#Get\ free\ quotes"
        # buttonquo=self.driver.find_element(By.CSS_SELECTOR,button)
        # buttonquo.click()
        # time.sleep(5)

        # br=By.ID,"make"
        # brands=self.wait.until(EC.visibility_of_all_elements_located(br))
                        
                        
        # if brands:
        #  time.sleep(4)
                        
        #  ra_br=random.choice(brands)
        #  ra_br.click()
        #  time.sleep(5)
                        
                        
                            
        # vars=By.ID,"model"
        # varints=self.wait.until(EC.visibility_of_all_elements_located(vars)) 
                        
        # if varints:
        #     ra_vr=random.choice(varints)
        #     ra_vr.click()
        #     time.sleep(9)
        #     self.log.info("trupass")                                                                                
                        
        # radio=By.XPATH,"//input[@type='radio']"
        # radio_btn=self.wait.until(EC.presence_of_all_elements_located(radio))
        # if radio_btn:
        #         rad_bt=random.choice(radio_btn)
        #         rad_bt.click()                
        # var_cc=By.ID,"variant_cc"
        # varints_cc=self.wait.until(EC.presence_of_all_elements_located(var_cc))
        # if varints_cc:
        #      v_click=random.choice(varints_cc)
        #      v_click.click()
        # var_choices=By.XPATH,"//ul[@class='css-djn3hl']/li"
        # var_allchoices=self.wait.until(EC.presence_of_all_elements_located(var_choices))                
        # if var_allchoices:                
        #         var_ch=random.choice(var_allchoices)
        #         var_ch.click()                                                                

                        
        
                              
    def health_prequote(self):
        def handle_relations():
            
            try:
                relations = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-43hhca .MuiAutocomplete-inputRoot .MuiAutocomplete-input")))
                for rel in relations:
                    rel.click()
                    options = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-17glcv2 li")))
                    random.choice(options).click()
                    time.sleep(1)
            except Exception as e:
                self.log.error(f"Error selecting relations: {e}")
        drop_down=By.CSS_SELECTOR,".css-t1oczc"
        dropc=self.wait.until(EC.presence_of_element_located(drop_down))
        dropc.click()
        try:
            # Select "Health" product
            products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-12hd50 p")))
            for product in products:
                if product.text == "Health":
                    product.click()
                    break

            # Generate random phone number and pincode
            phone_number = "78945" + str(random.randint(10000, 99999))
            pincode = str(random.choice(["110001", "400001", "700001", "560001"]))

            # Fill mobile and pincode
            self.driver.find_element(By.ID, "Enter mobile number").send_keys(phone_number)
            self.driver.find_element(By.ID, "Enter your pincode").send_keys(pincode)
            self.driver.find_element(By.CSS_SELECTOR, "button#Get\\ free\\ quotes").click()
            time.sleep(5)

            # Choose family composition
            checkboxes = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-j8yymo")))
            selected = random.choice(checkboxes)
            value = selected.get_attribute("id")
            selected.click()
            time.sleep(3)

            # Continue button
            self.driver.find_element(By.CSS_SELECTOR, "#Continue").click()
            time.sleep(3)

            # Start relation selection in thread
            thread = threading.Thread(target=handle_relations)
            thread.start()
            thread.join()

            # Click quote button
            self.driver.find_element(By.CSS_SELECTOR, ".primaryBtns .MuiButton-root").click()
            time.sleep(10)

            # Validate quote URL
            current_url = self.driver.current_url
            self.log.info(current_url)
            assert "quote_no" in current_url
            self.log.info("Health prequote successful")

        except Exception as e:
            self.log.error(f"Health quote failed: {e}")
            self.log.info(f"Current URL: {self.driver.current_url}")

