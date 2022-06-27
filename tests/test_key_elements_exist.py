from pages import item_desktop_page, admin_page, main_page, catalog_desktops_page, registration_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_main_page(driver, url):
    driver.get(url)

    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(main_page.SLIDER))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(main_page.FEATURED_TITLE))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(main_page.FEATURED_ITEMS_LIST))
    assert len(WebDriverWait(driver, 1).until(
        ec.visibility_of_all_elements_located(
            main_page.FEATURED_ITEMS_LIST))) == main_page.EXPECTED_FEATURED_ITEMS_AMOUNT
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(main_page.ADS_CAROUSEL))
    WebDriverWait(driver, 1).until(ec.title_is(main_page.PAGE_TITLE))


def test_catalog_desktops_page(driver, url):
    driver.get(url + catalog_desktops_page.PATH)

    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.BREADCRUMB_HOME))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.BREADCRUMB_DESKTOPS))
    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(catalog_desktops_page.CATALOG_TITLE)).text == catalog_desktops_page.TITLE
    assert WebDriverWait(driver, 1).until(ec.visibility_of_element_located(
        catalog_desktops_page.CATALOG_DESCRIPTION)).text == catalog_desktops_page.DESCRIPTION
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.CATALOG_IMAGE))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.SORT_SELECT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.SHOW_SELECT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.ITEM_SNIPPET))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.ITEM_IMAGE))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.ITEM_NAME))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(catalog_desktops_page.ITEM_PRICE))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.ADD_TO_CART))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.ADD_TO_WISHLIST))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(catalog_desktops_page.COMPARE_THIS_PRODUCT))


def test_item_desktop_page(driver, url):
    driver.get(url + item_desktop_page.PATH)

    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(item_desktop_page.ITEM_TITLE)).text == item_desktop_page.NAME
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.ITEM_PICTURES))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.ADD_TO_CART))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.COMPARE_THIS_PRODUCT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.ADD_TO_WISHLIST))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.DESCRIPTION_TAB))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.SPECIFICATION_TAB))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(item_desktop_page.REVIEWS_TAB))


def test_admin_page(driver, url):
    driver.get(url + admin_page.PATH)

    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(admin_page.TITLE)).text == admin_page.TITLE_TEXT
    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(admin_page.USERNAME_TITLE)).text == admin_page.USERNAME_TITLE_TEXT
    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(admin_page.PASSWORD_TITLE)).text == admin_page.PASSWORD_TITLE_TEXT
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(admin_page.USERNAME_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(admin_page.PASSWORD_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(admin_page.FORGOTTEN_PASSWORD_LINK))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(admin_page.LOGIN_BUTTON))


def test_registration_page(driver, url):
    driver.get(url + registration_page.PATH)

    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(registration_page.TITLE)).text == registration_page.TITLE_TEXT
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.FIRST_NAME_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.LAST_NAME_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.EMAIL_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.PHONE_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.PASSWORD_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.PASSWORD_CONFIRM_INPUT))
    WebDriverWait(driver, 1).until(ec.element_to_be_clickable(registration_page.CONTINUE_BUTTON))
