from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    EXPECTED_FEATURED_ITEMS_AMOUNT = 4
    TITLE = "Your Store"

    SLIDER = (By.CSS_SELECTOR, "div#slideshow0")
    FEATURED_TITLE = (By.XPATH, "//h3[text()='Featured']")
    FEATURED_ITEMS_LIST = (By.CSS_SELECTOR, ".product-layout")
    ADS_CAROUSEL = (By.CSS_SELECTOR, "div#carousel0")
    FEATURED_ITEMS_PRICE = (By.CSS_SELECTOR, "p.price")

    def open(self):
        self.browser.get(self.base_url)

    def verify_number_of_featured_items(self):
        number_of_featured_items = len(self.verify_all_elements_presence(self.FEATURED_ITEMS_LIST))
        assert number_of_featured_items == self.EXPECTED_FEATURED_ITEMS_AMOUNT

    def get_number_of_featured_items(self):
        return len(self.verify_all_elements_presence(self.FEATURED_ITEMS_LIST))

    def verify_if_price_in_correct_currency(self, currency):
        if currency not in ["EUR", "USD", "GBP"]:
            raise ValueError(
                f"Currency argument: {currency} or format of currency is not supported. Choose from EUR, USD, GBP.")
        currency_symbols_dict = {"USD": "$", "EUR": "€", "GBP": "£"}
        price = self.get_element_text(self.FEATURED_ITEMS_PRICE)
        assert currency_symbols_dict[currency] in price
