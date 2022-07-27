from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url, path=""):
        self.browser.get(url + path)

    def verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 2).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Couldn't find element by locator: {locator}")

    def _verify_all_elements_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 2).until(ec.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Couldn't find elements by locator: {locator}")

    def _element(self, locator: tuple):
        return self.verify_element_presence(locator)

    def verify_page_title(self, title):
        return WebDriverWait(self.browser, 2).until(ec.title_is(title))

    def get_element_text(self, locator):
        return self.verify_element_presence(locator).text
