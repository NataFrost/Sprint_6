from framework.base import BaseHelper
from data.locators_create_order_page import CreateOrderPageLocators
import random
import allure


class CreateOrderPage(BaseHelper):

    @allure.step('Получить все станции метро')
    def get_all_stations(self):
        return self.find_elements(CreateOrderPageLocators.LOCATOR_ALL_STATIONS)

    @allure.step('Выбрать станцию метро по индексу {index}')
    def select_station_by_index(self, index):
        try:
            return self.get_all_stations()[index]
        except ValueError:
            return None
        except IndexError:
            return None

    @allure.step('Выбрать случайную санцию метро')
    def select_random_station(self):
        stations = self.get_all_stations()
        stations_len = len(stations)
        if stations_len:
            random_number = random.randint(0, stations_len - 1)
            chosen_station = stations[random_number]
            allure.attach(
                f"Выбрана станция: {chosen_station.text}",
                name="Выбранная станция",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.step(f"Выбрана станция метро: {chosen_station}")
            return chosen_station

    @allure.step('Получить все сроки аренды')
    def get_all_periods(self):
        return self.find_elements(CreateOrderPageLocators.LOCATOR_PERIOD_OPTIONS)

    @allure.step('Выбрать случайный период аренды')
    def select_random_period(self):
        periods = self.get_all_periods()
        periods_len = len(periods)
        if periods_len:
            random_number = random.randint(0, periods_len - 1)
            chosen_period = periods[random_number]
            allure.attach(
                f"Выбран период аренды: {chosen_period.text}",
                name="Выбранный период аренды",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.step(f"Выбрать случайный период аренды: {chosen_period}")
            return chosen_period

    @allure.step('Отправить заказ')
    def send_order(self):
        send_button = self.find_elements(CreateOrderPageLocators.LOCATOR_ORDER_BUTTONS)[1]
        send_button.click()

    @allure.step('Вернуться на предыдущую страницу заказа')
    def order_go_back(self):
        back_button = self.find_elements(CreateOrderPageLocators.LOCATOR_ORDER_BUTTONS)[0]
        back_button.click()

    @allure.step('Подтвердить отправку заказа')
    def confirm_order(self):
        confirm_button = self.find_elements(CreateOrderPageLocators.LOCATOR_CONFIRM_ORDER_BUTTONS)[1]
        confirm_button.click()

    @allure.step('Отменить отправку заказа')
    def cancel_order(self):
        cancel_button = self.find_elements(CreateOrderPageLocators.LOCATOR_CONFIRM_ORDER_BUTTONS)[0]
        cancel_button.click()

    @allure.step("Получить подтверждение заказа")
    def get_order_confirmation_text(self):
        return self.find_element(CreateOrderPageLocators.LOCATOR_ORDER_CONFIRMATION_MODAL_TEXT).text



