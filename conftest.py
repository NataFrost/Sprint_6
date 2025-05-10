import pytest
from selenium import webdriver
from data.constants_home_page import HomePageConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(HomePageConstants.BASE_URL)
    yield browser
    browser.quit()
