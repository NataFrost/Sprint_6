import pytest
import allure

from pages.home_page import HomePage
from pages.home_page import HomePageLocators

from data.constants_home_page import HomePageConstants
from data.constants_create_order_page import CreateOrderPageConstants


class TestHomePage:

    @allure.title("Проверить, что элемент аккордеона {item_number} открывается при клике")
    @pytest.mark.parametrize("item_number", range(8))
    def test_accordion_expanded_after_click(self, driver, item_number):
        homepage = HomePage(driver)
        homepage.accept_cookies()
        homepage.scroll_to_sub_header(HomePageConstants.SUB_HEADER_FAQ)
        accordion_item = homepage.get_accordion_data(item_number)
        el_question, el_answer = accordion_item[0]
        attr_before_click = el_question.get_attribute('aria-expanded')
        homepage.click_accordion_item(accordion_item[1])
        attr_after_click = el_question.get_attribute('aria-expanded')
        with allure.step("Сравнение фактического и ожидаемого результата"):
            allure.attach(
                f"Арибут элемента {item_number} 'aria-expanded' изменился с {attr_before_click} на {attr_after_click} ",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert attr_before_click == 'false' and attr_after_click == 'true'

    @allure.title("Проверить, что текст ответа виден при клике на элемент аккордеона {item_number}")
    @pytest.mark.parametrize("item_number", range(8))
    def test_accordion_text_visible_after_click(self, driver, item_number):
        homepage = HomePage(driver)
        homepage.accept_cookies()
        homepage.scroll_to_sub_header(HomePageConstants.SUB_HEADER_FAQ)
        accordion_item = homepage.get_accordion_data(item_number)
        el_question, el_answer = accordion_item[0]
        attr_before_click = el_answer.get_attribute('hidden')
        homepage.click_accordion_item(accordion_item[1])
        attr_after_click = el_answer.get_attribute('hidden')

        with allure.step("Сравнение фактического и ожидаемого результата"):
            allure.attach(
                f"Арибут элемента {item_number} 'hidden' изменился с {attr_before_click} на {attr_after_click} ",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert attr_before_click == 'true' and attr_after_click is None

    @allure.title("Проверить, что текст ответа и вопроса элемента {item_index} верные")
    @pytest.mark.parametrize("item_index, expected", HomePageConstants.questions.items())
    def test_accordion_question_and_answer_text(self, driver, item_index, expected):
        question = expected[0]
        answer = expected[1]
        homepage = HomePage(driver)
        homepage.accept_cookies()
        homepage.scroll_to_sub_header(HomePageConstants.SUB_HEADER_FAQ)
        accordion_item = homepage.get_accordion_data(item_index)
        el_question, el_answer = accordion_item[0]
        homepage.click_accordion_item(accordion_item[1])

        with allure.step("Сравнение фактического и ожидаемого результаа"):
            allure.attach(
                f"Текст вопроса и ответа элемента {item_index} совпадают с ожидаемыми",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert el_question.text == question and el_answer.text == answer

    @allure.title("Проверить, что процесс заказа можно начать по кнопке {button_name}")
    @pytest.mark.parametrize("button_locator, button_name", [[HomePageLocators.LOCATOR_ORDER_BUTTON_HOMEPAGE, HomePageConstants.ORDER_BUTTON_HOME_PAGE],
                              [HomePageLocators.LOCATOR_ORDER_BUTTON_HEADER, HomePageConstants.ORDER_BUTTON_HEADER]])
    def test_start_order_creation(self, driver, button_locator, button_name):
        homepage = HomePage(driver)
        homepage.accept_cookies()
        homepage.click_button(button_locator, button_name)
        homepage.wait_url(HomePageConstants.ORDER_URL)
        title = homepage.find_element(HomePageLocators.LOCATOR_ORDER_HEADER).text
        current_url = driver.current_url

        with allure.step("Сравнение фактического и ожидаемого результата"):
            allure.attach(
                f"Заголовок страницы {title} совпадает с ожидаемым заголовком {CreateOrderPageConstants.TITLE_1}"
                f"и current_url {current_url} равен {HomePageConstants.ORDER_URL}",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert title == CreateOrderPageConstants.TITLE_1 and current_url == HomePageConstants.ORDER_URL

    @allure.title("Проверить, что по клику на логотип Яндекс открывается стартовая страница Дзен")
    def test_go_to_yandex_via_logo(self, driver):
        homepage = HomePage(driver)
        homepage.accept_cookies()
        homepage.click_button(HomePageLocators.LOCATOR_YANDEX_LOGO, HomePageConstants.LOGO_YANDEX)
        driver.switch_to.window(driver.window_handles[1])
        homepage.wait_url(HomePageConstants.DZEN_URL)
        current_url = driver.current_url
        with allure.step("Сравнение фактического и ожидаемого результата"):
            allure.attach(
                f"current_url {current_url} равен {HomePageConstants.DZEN_URL}",
                name="Детали проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            assert current_url == HomePageConstants.DZEN_URL


