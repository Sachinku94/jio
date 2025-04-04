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

                        br=By.ID,"make"
                        brands=wait.until(EC.visibility_of_all_elements_located(br))
                        
                        
                        if brands:
                            time.sleep(4)
                        
                            ra_br=random.choice(brands)
                            ra_br.click()
                        time.sleep(5)
                        
                        
                            
                        vars=By.ID,"model"
                        varints=wait.until(EC.visibility_of_all_elements_located(vars)) 
                        
                        if varints:
                                ra_vr=random.choice(varints)
                                ra_vr.click()
                                time.sleep(9)
                                log.info("trupass")
                        
                        radio=By.CSS_SELECTOR,".preQuoteFormBox Input"
                        radio_btn=wait.until(EC.visibility_of_all_elements_located(radio))
                        if radio_btn:
                              rad_bt=random.choice(radio_btn)
                              rad_bt.click()
                        var_cc=By.ID,"variant_cc"
                        varints_cc=wait.until(EC.visibility_of_element_located(var_cc))
                        varints_cc.click()
                        var_choices=By.CSS_SELECTOR,"css-djn3hl"
                        var_allchoices=wait.until(EC.presence_of_all_elements_located(var_choices))
                        if var_allchoices:
                              var_ch=random.choice(var_allchoices)
                              var_ch.click()
                              
    def healthprequote(self):
          
        log=self.getLogger()
        Ac = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        quote=homepagejio.HomePage
        quote.leads(self)
        prod=By.CSS_SELECTOR,"div.css-12hd50 p"
        product=wait.until(EC.presence_of_all_elements_located(prod))
        pop_up=SeleniumHelper(self.driver)
        
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
                        time.sleep(5)
                        self.driver.refresh()
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
                                # pop_up.remove_popup()
                                rel=By.CSS_SELECTOR,".css-43hhca .MuiAutocomplete-inputRoot .MuiAutocomplete-input"
                                relation=wait.until(EC.visibility_of_all_elements_located(rel))
                                for rell in relation:
                                    
                                    time.sleep(5)
                                    rell.click()
                                    all_option =By.CSS_SELECTOR,".css-17glcv2 li"
                                    all_inoption=wait.until(EC.presence_of_all_elements_located(all_option))
                                    sel=random.choice(all_inoption)
                                    sel.click()
                                    # pop_up.remove_popup()
                                # time.sleep(70)
                                # pop_up.remove_popup()
                                # time.sleep(5)
                                qutbut=self.driver.find_element(By.CSS_SELECTOR,".primaryBtns .MuiButton-root")
                                qutbut.click()
                                # self.driver.refresh()
                                time.sleep(10)
                                url=self.driver.current_url
                                log.info(url)
                                assert "quote_no" in url
                                
                            
                                
                                # quotetions=By.CSS_SELECTOR,".css-14kjlot"
                                # all_quote=wait.until(EC.visibility_of_any_elements_located(quotetions))
                                # assert all_quote


                               
                                
                        elif value=="One Adult" :
                                time.sleep(5)
                                    
                                cont="#Continue"
                                conti=self.driver.find_element(By.CSS_SELECTOR,cont) 
                                conti.click()

                                rel=By.CSS_SELECTOR,".css-43hhca .MuiAutocomplete-inputRoot .MuiAutocomplete-input"
                                relation=wait.until(EC.visibility_of_element_located(rel))
                                relation.click()

                                all_option =By.CSS_SELECTOR,".css-17glcv2 li"
                                all_inoption=wait.until(EC.presence_of_all_elements_located(all_option))
                                sel=random.choice(all_inoption)
                                sel.click()  

                                qutbut=self.driver.find_element(By.CSS_SELECTOR,".primaryBtns .MuiButton-root")
                                qutbut.click()
                                # time.sleep(70)
                                # pop_up.remove_popup()
                                time.sleep(5)
                                url=self.driver.current_url
                                log.info(url)
                                assert "quote_no" in url
                                log.info("prequote pass")
                                
                                # quotetions=By.CSS_SELECTOR,".css-14kjlot"
                                # all_quote=wait.until(EC.visibility_of_any_elements_located(quotetions))
                                # assert all_quote
                                
                                # self.driver.quit()              
                        elif value == "Children":
                                ra_slcheck.click()
                                time.sleep(5)
                                cont="#Continue"
                                conti=self.driver.find_element(By.CSS_SELECTOR,cont) 
                                conti.click()

                                rel=By.CSS_SELECTOR,".css-43hhca .MuiAutocomplete-inputRoot .MuiAutocomplete-input"
                                relation=wait.until(EC.visibility_of_element_located(rel))
                                relation.click()

                                all_option =By.CSS_SELECTOR,".css-17glcv2 li"
                                all_inoption=wait.until(EC.presence_of_all_elements_located(all_option))
                                sel=random.choice(all_inoption)
                                sel.click()  

                                qutbut=self.driver.find_element(By.CSS_SELECTOR,".primaryBtns .MuiButton-root")
                                qutbut.click()
                                # time.sleep(70)
                                # pop_up.remove_popup()
                                time.sleep(5)
                                self.driver.refresh()
                                time.sleep(10)
                                url=self.driver.current_url
                                log.info(url)
                                assert "quote_no" in url
                                log.info("prequote pass")

                                
                                
                                # quotetions=By.CSS_SELECTOR,".css-14kjlot"
                                # all_quote=wait.until(EC.visibility_of_any_elements_located(quotetions))
                                # assert all_quote
                                 
                            
                            
                        break            
                    else:
                          continue
                        
                           
                    
                                       
                    
                
        log.info("prequote pass")

