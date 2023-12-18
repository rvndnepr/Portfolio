import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope='function')
# def init_driver():
#     driver_service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=driver_service)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.fixture(scope='class')
def init_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
