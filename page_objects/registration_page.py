from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    PATH = "/index.php?route=account/register"

    TITLE_TEXT = "Register Account"

    TITLE = (By.CSS_SELECTOR, "#content h1")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#input-firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#input-email")
    PHONE_INPUT = (By.CSS_SELECTOR, "input#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#input-password")
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "input#input-confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
