from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data.constants_home_page import HomePageConstants
import allure


class BaseHelper:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Element not found: {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Elements not found: {locator}")

    def find_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f"Elements not clickable: {locator}")

    @allure.step("Нажать на элемент {field_name}")
    def click_button(self, locator, field_name='Placeholder', time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Заполнить поле {field_name} значением {value}")
    def fill_input_field(self, locator, field_name, value):
        input_field = self.find_element(locator)
        input_field.click()
        input_field.send_keys(value)

    @allure.step("Открыт URL: {url}")
    def wait_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))
