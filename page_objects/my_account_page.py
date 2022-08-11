from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MyAccountPage(BasePage):
    PATH = "/index.php?route=account/account"

    PAGE_TITLE = "My Account"
    TITLE = (By.CSS_SELECTOR, "div.row div#content h2")
