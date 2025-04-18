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
from Pages import prequotepagejio
class postQuotePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def healthpostquote(self):
        postquote=prequotepagejio.QuotePage
        postquote.healthprequote(self)
    