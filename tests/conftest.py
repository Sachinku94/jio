import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.config_reader import read_config
from Smoke_tests.object.Selenium_helper import SeleniumHelper

@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    CHROMEDRIVER_VERSION = "134.0.6998.166"
    path = ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()
    base_url = read_config("URL", "base_url")

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize the window on start
     # Disable extensions

    # Setup Service object using the chromedriver path from ChromeDriverManager
    service = Service(path)

    # Initialize the driver with the service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the base URL in the browser
    driver.get(base_url)
    wait = WebDriverWait(driver, 20)
    
    pop_up=By.CSS_SELECTOR,".modal-scrollable .MuiPaper-root .modal-content .closePopup"
    close=wait.until(EC.presence_of_element_located(pop_up))
    close.click()
    # Remove the pop-up before continuing to the next page
    # pop_up.remove_popup()=SeleniumHelper.remove_popup
    # pop_up.remove_popup()
    
    # Attach the driver to the test class (so tests can access it)
    request.cls.driver = driver

    # Yield the driver to run tests
    yield driver

    # Quit the driver after tests complete
    driver.quit()
