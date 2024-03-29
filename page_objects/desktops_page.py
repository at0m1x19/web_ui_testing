from selenium.webdriver.common.by import By

from .base_page import BasePage


class DesktopsPage(BasePage):
    PATH = "/desktops"

    TITLE = "Desktops"
    DESCRIPTION = "Example of category description text"

    BREADCRUMB_HOME = (By.CSS_SELECTOR, "#product-category ul li a[href$='/home']")
    BREADCRUMB_DESKTOPS = (By.CSS_SELECTOR, "#product-category ul li a[href$='/desktops']")
    CATALOG_TITLE = (By.XPATH, "//div[@id='content']//*[text()='Desktops']")
    CATALOG_DESCRIPTION = (By.CSS_SELECTOR, ".col-sm-10 p")
    CATALOG_IMAGE = (By.CSS_SELECTOR, "img.img-thumbnail")
    SORT_SELECT = (By.CSS_SELECTOR, "select#input-sort")
    SHOW_SELECT = (By.CSS_SELECTOR, "select#input-limit")
    ITEM_SNIPPET = (By.CSS_SELECTOR, ".product-thumb")
    ITEM_IMAGE = (By.CSS_SELECTOR, ".product-thumb .img-responsive")
    ITEM_NAME = (By.CSS_SELECTOR, ".product-thumb .caption a")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product-thumb .price")
    ADD_TO_CART = (By.XPATH, "//div[@class='product-thumb']//span[text()='Add to Cart']")
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, ".product-thumb button[data-original-title='Add to Wish List']")
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, ".product-thumb button[data-original-title='Compare this Product']")

    def open(self):
        self.browser.get(self.base_url + self.PATH)

    def get_catalog_description_text(self):
        return self.verify_element_presence(self.CATALOG_DESCRIPTION).text.strip('\n\t')
