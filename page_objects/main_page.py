from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    EXPECTED_FEATURED_ITEMS_AMOUNT = 4
    TITLE = "Your Store"

    SLIDER = (By.CSS_SELECTOR, "div#slideshow0")
    FEATURED_TITLE = (By.XPATH, "//h3[text()='Featured']")
    FEATURED_ITEMS_LIST = (By.CSS_SELECTOR, ".product-layout")
    ADS_CAROUSEL = (By.CSS_SELECTOR, "div#carousel0")

    def verify_number_of_featured_items(self):
        number_of_featured_items = len(self._verify_all_elements_presence(self.FEATURED_ITEMS_LIST))
        assert number_of_featured_items == self.EXPECTED_FEATURED_ITEMS_AMOUNT

    def get_number_of_featured_items(self):
        return len(self._verify_all_elements_presence(self.FEATURED_ITEMS_LIST))
