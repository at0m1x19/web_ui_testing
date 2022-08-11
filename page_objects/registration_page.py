from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.my_account_page import MyAccountPage


class RegistrationPage(BasePage):
    PATH = "/index.php?route=account/register"

    TITLE_TEXT = "Register Account"
    SUCCESSFUL_REGISTRATION_MESSAGE = "Congratulations! Your new account has been successfully created!"

    TITLE = (By.CSS_SELECTOR, "#content h1")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#input-firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#input-email")
    PHONE_INPUT = (By.CSS_SELECTOR, "input#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#input-password")
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "input#input-confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    POLICY_AGREE_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    SUCCESS_PAGE_TITLE = (By.CSS_SELECTOR, "div#content p")
    AFTER_REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "a.btn-primary")

    def open(self):
        self.browser.get(self.base_url + self.PATH)

    def register_user(self, email, first_name="test", last_name="test", password="123456", phone="123"):
        self.element(self.FIRST_NAME_INPUT).send_keys(first_name)
        self.element(self.LAST_NAME_INPUT).send_keys(last_name)
        self.element(self.EMAIL_INPUT).send_keys(email)
        self.element(self.PHONE_INPUT).send_keys(phone)
        self.element(self.PASSWORD_INPUT).send_keys(password)
        self.element(self.PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.element(self.POLICY_AGREE_CHECKBOX).click()
        self.element(self.CONTINUE_BUTTON).click()

    def submit_successful_registration_message(self):
        self.element(self.AFTER_REGISTER_SUBMIT_BUTTON).click()
        return MyAccountPage(self.browser, self.base_url)
