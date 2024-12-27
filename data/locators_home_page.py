from selenium.webdriver.common.by import By


class HomePageLocators:
    LOCATOR_HOME_HEADER = (By.XPATH, ".//div[contains(@class, 'Home_Header')]")

    LOCATOR_SUB_HEADERS = (By.XPATH, ".//div[contains(@class, 'SubHeader')]")
    LOCATOR_ACCORDION_HEADINGS = (By.XPATH, ".//div[contains(@id, 'accordion__heading-')]")
    LOCATOR_ACCORDION_PANELS = (By.XPATH, ".//div[contains(@id, 'accordion__panel-')]")

    HEADING = 'accordion__heading-'
    PANEL = 'accordion__panel-'

    LOCATOR_COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

    LOCATOR_ORDER_BUTTON_HOMEPAGE = (By.XPATH, ".//div[contains(@class, 'FinishButton')]")
    LOCATOR_ORDER_BUTTON_HEADER = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, Button)]")

    LOCATOR_ORDER_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_Header')]")

    LOCATOR_YANDEX_LOGO = (By.XPATH, ".//div[contains(@class, 'Header_Logo')]/a")
