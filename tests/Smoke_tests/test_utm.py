from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pytest
from Pages.homepagejio import HomePage
from object.Selenium_helper import SeleniumHelper
import asyncio
from tests.Pages.utm_jio import UTM_Page

class Testone(BaseClass):

    def utm_positive(self):
        log = self.getLogger()
        utmP=UTM_Page(self.driver)
        utmP.Utm_direct()
        log.info("utm_pass")