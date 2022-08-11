from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ItemPage(BasePage):
    PATH = "/desktops/test"

    ITEM_TITLE = (By.CSS_SELECTOR, "#content h1")
    ITEM_PICTURES = (By.CSS_SELECTOR, "#content a.thumbnail")
    ADD_TO_CART = (By.CSS_SELECTOR, ".form-group button#button-cart")
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, ".btn-group button[data-original-title='Compare this Product']")
    DESCRIPTION_TAB = (By.CSS_SELECTOR, "a[href='#tab-description']")
    SPECIFICATION_TAB = (By.CSS_SELECTOR, "a[href='#tab-specification']")
    REVIEWS_TAB = (By.CSS_SELECTOR, "a[href='#tab-review']")

    def open(self):
        self.browser.get(self.base_url + self.PATH)
