from selenium.webdriver.common.by import By

from ..base_page import BasePage


class CurrencySwitcher(BasePage):
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "button.btn-link[data-toggle='dropdown']")

    def switch_currency_to(self, currency):
        if currency not in ["EUR", "USD", "GBP"]:
            raise ValueError(
                f"Currency argument: {currency} or format of currency is not supported. Choose from EUR, USD, GBP.")
        switch_to_currency_locator = (By.CSS_SELECTOR, f"button.currency-select[name='{currency}']")
        self.element(self.CURRENCY_DROPDOWN).click()
        self.element(switch_to_currency_locator).click()
