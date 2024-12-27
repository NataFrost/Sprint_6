from data.constants_create_order_page import CreateOrderPageConstants
from selenium.webdriver.common.by import By


class CreateOrderPageLocators:
    LOCATOR_NAME_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_NAME}')]")
    LOCATOR_SURNAME_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_SURNAME}')]")
    LOCATOR_ADDRESS_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_ADDRESS}')]")
    LOCATOR_STATION_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_STATION}')]")
    LOCATOR_PHONE_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_PHONE_NUMBER}')]")
    LOCATOR_COMMENT_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_COMMENT}')]")

    LOCATOR_DATE_INPUT = (By.XPATH, f".//input[contains(@placeholder, '{CreateOrderPageConstants.PLACEHOLDER_DATE}')]")
    LOCATOR_PERIOD_INPUT = (By.XPATH, ".//div[contains(@class, 'Dropdown-root')]")

    LOCATOR_CHECKBOX_BLACK = (By.ID, "black")
    LOCATOR_CHECKBOX_GREY = (By.ID, "grey")

    LOCATOR_ALL_STATIONS = (By.XPATH, ".//li[@role='menuitem']")
    LOCATOR_STATION_NAME = (By.XPATH, ".//div[contains(@class, 'Order_Text')]")
    LOCATOR_NEXT_BUTTON = (By.XPATH, ".//div[contains(@class, 'NextButton')]/button")

    LOCATOR_ORDER_TITLE = (By.XPATH, ".//div[contains(@class, 'Order_Header')]")
    LOCATOR_PERIOD_OPTIONS = (By.XPATH, ".//div[@role='option']")

    LOCATOR_ORDER_BUTTONS = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button")

    LOCATOR_CONFIRM_ORDER_BUTTONS = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'Order_Buttons')]/button")
    LOCATOR_ORDER_CONFIRMATION_MODAL_TITLE = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'ModalHeader')]")
    LOCATOR_ORDER_CONFIRMATION_MODAL_TEXT = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'Order_Text')]")
    LOCATOR_ORDER_CONFIRMATION_MODAL_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'NextButton')]/button")

    LOCATOR_ORDER_SEARCH_FIELD = (By.XPATH, ".//div[contains(@class, 'Track_Form')]//input")

    LOCATOR_LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class, 'LogoScooter')]")
