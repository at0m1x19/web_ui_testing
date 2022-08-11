import os

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
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DASHBOARD_TITLE = (By.XPATH, "//h1[text()='Dashboard']")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu #menu-catalog")
    MENU_PRODUCTS = (By.XPATH, "//li[@id='menu-catalog']//a[text()='Products']")
    PRODUCTS_TITLE = (By.XPATH, "//h1[text()='Products']")
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "input#input-name1")
    PRODUCT_META_TAG_FIELD = (By.CSS_SELECTOR, "input#input-meta-title1")
    PRODUCT_MODEL_FIELD = (By.CSS_SELECTOR, "input#input-model")
    PRODUCT_DATA_TAB = (By.CSS_SELECTOR, "a[href='#tab-data']")
    PRODUCT_SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    FILTER_PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "#filter-product input#input-name")
    FILTER_PRODUCT_MODEL_FIELD = (By.CSS_SELECTOR, "#filter-product input#input-model")
    FILTER_PRODUCT_SUBMIT = (By.CSS_SELECTOR, "button#button-filter")
    CHOOSE_ALL_CHECK_BOX = (By.CSS_SELECTOR, "thead input[type='checkbox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    FILTERED_RESULTS_TEXT = (By.XPATH, "//div[@class='col-sm-6 text-right']")

    def open(self):
        self.browser.get(self.base_url + self.PATH)

    def login(self):
        self.element(self.USERNAME_INPUT).send_keys(os.getenv("ADMIN_LOGIN"))
        self.element(self.PASSWORD_INPUT).send_keys(os.getenv("ADMIN_PASSWORD"))
        self.element(self.SUBMIT_BUTTON).submit()
        self.element(self.DASHBOARD_TITLE)

    def navigate_to_products_section(self):
        self.element(self.MENU_CATALOG).click()
        self.element(self.MENU_PRODUCTS).click()
        self.verify_element_presence(self.PRODUCTS_TITLE)

    def add_product(self, name="TestName", model="TestModel", meta_tag="TestMetaTag"):
        self.navigate_to_products_section()
        self.element(self.ADD_NEW_PRODUCT_BUTTON).click()
        self.element(self.PRODUCT_NAME_FIELD).send_keys(name)
        self.element(self.PRODUCT_META_TAG_FIELD).send_keys(meta_tag)
        self.element(self.PRODUCT_DATA_TAB).click()
        self.element(self.PRODUCT_MODEL_FIELD).send_keys(model)
        self.element(self.SUBMIT_BUTTON).click()
        self.verify_element_presence(self.PRODUCT_SUCCESS_ALERT)

    def filter_products_by_name_and_model(self, name="TestName", model="TestModel"):
        self.element(self.FILTER_PRODUCT_NAME_FIELD).clear()
        self.element(self.FILTER_PRODUCT_MODEL_FIELD).clear()
        self.element(self.FILTER_PRODUCT_NAME_FIELD).send_keys(name)
        self.element(self.FILTER_PRODUCT_MODEL_FIELD).send_keys(model)
        self.element(self.FILTER_PRODUCT_SUBMIT).click()

    def remove_products_by_name_and_model(self, name, model):
        self.filter_products_by_name_and_model(name, model)
        self.element(self.CHOOSE_ALL_CHECK_BOX).click()
        self.element(self.DELETE_BUTTON).click()
        self.accept_alert()
        self.verify_element_presence(self.PRODUCT_SUCCESS_ALERT)
