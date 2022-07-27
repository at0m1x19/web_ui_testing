from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/admin"

    TITLE_TEXT = "Please enter your login details."
    USERNAME_TITLE_TEXT = "Username"
    PASSWORD_TITLE_TEXT = "Password"

    TITLE = (By.CSS_SELECTOR, "h1.panel-title")
    USERNAME_TITLE = (By.CSS_SELECTOR, "label[for='input-username']")
    PASSWORD_TITLE = (By.CSS_SELECTOR, "label[for='input-password']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#input-password")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, ".help-block a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
