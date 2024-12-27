import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.base import BaseHelper
from data.locators_home_page import HomePageLocators


class HomePage(BaseHelper):

    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.find_element(locator=HomePageLocators.LOCATOR_COOKIES_BUTTON).click()

    @allure.step('Прокрутить страницу до подраздела {sub_header}')
    # функция для скролла к нужному разделу на главной
    def scroll_to_sub_header(self, sub_header):
        wels = self.find_elements(locator=HomePageLocators.LOCATOR_SUB_HEADERS)
        for wel in wels:
            if wel.text == sub_header:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", wel)

    # функция возвращает кортеж с локаторами и кортеж с веб элементами (для вопроса и ответа)
    def get_accordion_data(self, number=0):
        locator_question, locator_answer = self.get_accordion_locators(number)
        el_question = self.find_element(locator=locator_question)
        el_answer = self.find_element(locator=locator_answer)
        return (el_question, el_answer), (locator_question, locator_answer)

    # функция для определения лоакторов нужных элементов списка (вопрос и ответ)
    def get_accordion_locators(self, number=0):
        # усложнение для большей универсальности, потому что выяснилось,
        # что айдишники не всегда начинаются с нуля в зависимости от действий в сессии
        first_id = self.find_elements(locator=HomePageLocators.LOCATOR_ACCORDION_HEADINGS)[0].get_attribute('id').split('-')
        start = int(first_id[-1])
        locator_question = (By.ID, HomePageLocators.HEADING + str(start + number))
        locator_answer = (By.ID, HomePageLocators.PANEL + str(start + number))
        return locator_question, locator_answer

    @allure.step('Кликнуть на вопрос')
    def click_accordion_item(self, locators):
        locator_question, locator_answer = locators
        # кликаем на нужный вопрос
        self.find_clickable(locator_question).click()
        # ждем пока текст ответа станет видимым
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_answer))
