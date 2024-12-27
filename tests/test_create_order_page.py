import pytest
import allure

from pages.home_page import HomePage
from pages.create_order_page import CreateOrderPage

from data.constants_home_page import HomePageConstants
from data.locators_home_page import HomePageLocators
from data.constants_create_order_page import CreateOrderPageConstants
from data.locators_create_order_page import CreateOrderPageLocators
from data.data_generator import DataGenHelper


class TestCreateOrderPage:

    @allure.title('Проверка создания заказа - позитивный сценарий - все поля заполнены')
    @pytest.mark.parametrize("user", CreateOrderPageConstants.users.values())
    def test_create_order_positive_flow(self, driver, user):
        faker = DataGenHelper()
        user_name = user[0]
        user_surname = user[1]
        user_address = user[2]
        user_phone = user[3]
        user_comment = user[4]
        homepage = HomePage(driver)
        order = CreateOrderPage(driver)
        homepage.accept_cookies()
        homepage.click_button(HomePageLocators.LOCATOR_ORDER_BUTTON_HOMEPAGE, CreateOrderPageConstants.ORDER_BUTTON)
        order.fill_input_field(CreateOrderPageLocators.LOCATOR_NAME_INPUT, CreateOrderPageConstants.PLACEHOLDER_NAME, user_name)
        order.fill_input_field(CreateOrderPageLocators.LOCATOR_SURNAME_INPUT, CreateOrderPageConstants.PLACEHOLDER_SURNAME, user_surname)
        order.fill_input_field(CreateOrderPageLocators.LOCATOR_ADDRESS_INPUT, CreateOrderPageConstants.PLACEHOLDER_ADDRESS, user_address)
        order.find_clickable(CreateOrderPageLocators.LOCATOR_STATION_INPUT).click()
        rand_station = order.select_random_station()
        rand_station.click()
        order.fill_input_field(CreateOrderPageLocators.LOCATOR_PHONE_INPUT, CreateOrderPageConstants.PLACEHOLDER_PHONE_NUMBER, user_phone)
        order.click_button(CreateOrderPageLocators.LOCATOR_NEXT_BUTTON, CreateOrderPageConstants.NEXT_BUTTON)
        order_date = faker.generate_random_date()
        order.fill_input_field(CreateOrderPageLocators.LOCATOR_DATE_INPUT, CreateOrderPageConstants.PLACEHOLDER_DATE, order_date)
        order.find_clickable(CreateOrderPageLocators.LOCATOR_ORDER_TITLE).click()
        order.find_clickable(CreateOrderPageLocators.LOCATOR_PERIOD_INPUT).click()
        random_period = order.select_random_period()
        random_period.click()
        order.click_button(CreateOrderPageLocators.LOCATOR_CHECKBOX_BLACK, CreateOrderPageConstants.SCOOTER_COLOR_BLACK)
        order.click_button(CreateOrderPageLocators.LOCATOR_CHECKBOX_GREY, CreateOrderPageConstants.SCOOTER_COLOR_GREY)
        order.fill_input_field(CreateOrderPageLocators.LOCATOR_COMMENT_INPUT, CreateOrderPageConstants.PLACEHOLDER_COMMENT, user_comment)
        order.send_order()
        order.cancel_order()
        order.send_order()
        order.confirm_order()
        order_confirmation_text = order.get_order_confirmation_text()
        order.click_button(CreateOrderPageLocators.LOCATOR_ORDER_CONFIRMATION_MODAL_BUTTON, CreateOrderPageConstants.ORDER_STATUS_BUTTON)
        order_number = order.find_element(CreateOrderPageLocators.LOCATOR_ORDER_SEARCH_FIELD).get_attribute('value')
        with allure.step("Сравнение фактического и ожидаемого результата"):
            allure.attach(
                f"Номер заказа содержится в тексте подтверждения: '{order_confirmation_text}' и равен номеру заказа '{order_number}' в поле поиска заказа",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert order_number in order_confirmation_text, "Условие не выполнено"

    @allure.title("Проверка перехода на главную страницу по клику на логотип в хидере")
    def test_go_to_homepage_via_logo(self, driver):
        homepage = HomePage(driver)
        order = CreateOrderPage(driver)
        homepage.accept_cookies()
        homepage.click_button(HomePageLocators.LOCATOR_ORDER_BUTTON_HOMEPAGE, CreateOrderPageConstants.ORDER_BUTTON)
        order.wait_url(HomePageConstants.ORDER_URL)
        order.click_button(CreateOrderPageLocators.LOCATOR_LOGO_SCOOTER, CreateOrderPageConstants.SCOOTER_LOGO)
        order.wait_url(HomePageConstants.BASE_URL)
        current_url = driver.current_url

        with allure.step("Сравнение фактического и ожидаемого результата"):
            allure.attach(
                f"{current_url} == {HomePageConstants.BASE_URL}",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert current_url == HomePageConstants.BASE_URL, "Условие не выполнено"


