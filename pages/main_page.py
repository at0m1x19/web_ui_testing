from selenium.webdriver.common.by import By

EXPECTED_FEATURED_ITEMS_AMOUNT = 4
PAGE_TITLE = "Your Store"

SLIDER = (By.CSS_SELECTOR, "div#slideshow0")
FEATURED_TITLE = (By.XPATH, "//h3[text()='Featured']")
FEATURED_ITEMS_LIST = (By.CSS_SELECTOR, ".product-layout")
ADS_CAROUSEL = (By.CSS_SELECTOR, "div#carousel0")
