from page_objects.admin_page import AdminPage
from page_objects.main_page import MainPage
from page_objects.desktops_page import DesktopsPage
from page_objects.item_page import ItemPage
from page_objects.registration_page import RegistrationPage


def test_main_page(driver, base_url):
    main_page = MainPage(driver)
    main_page.open(base_url)

    main_page.verify_page_title(main_page.TITLE)
    main_page.verify_element_presence(main_page.SLIDER)
    main_page.verify_element_presence(main_page.FEATURED_TITLE)
    main_page.verify_element_presence(main_page.FEATURED_ITEMS_LIST)
    main_page.verify_element_presence(main_page.ADS_CAROUSEL)
    assert main_page.get_number_of_featured_items() == main_page.EXPECTED_FEATURED_ITEMS_AMOUNT


def test_desktops_page(driver, base_url):
    desktops_page = DesktopsPage(driver)
    desktops_page.open(base_url + desktops_page.PATH)

    desktops_page.verify_page_title(desktops_page.TITLE)
    desktops_page.verify_element_presence(desktops_page.BREADCRUMB_HOME)
    desktops_page.verify_element_presence(desktops_page.BREADCRUMB_DESKTOPS)
    desktops_page.verify_element_presence(desktops_page.CATALOG_IMAGE)
    desktops_page.verify_element_presence(desktops_page.SORT_SELECT)
    desktops_page.verify_element_presence(desktops_page.SHOW_SELECT)
    desktops_page.verify_element_presence(desktops_page.ITEM_SNIPPET)
    desktops_page.verify_element_presence(desktops_page.ITEM_IMAGE)
    desktops_page.verify_element_presence(desktops_page.ITEM_NAME)
    desktops_page.verify_element_presence(desktops_page.ITEM_PRICE)
    desktops_page.verify_element_presence(desktops_page.ADD_TO_CART)
    desktops_page.verify_element_presence(desktops_page.ADD_TO_WISHLIST)
    desktops_page.verify_element_presence(desktops_page.COMPARE_THIS_PRODUCT)
    assert desktops_page.get_catalog_description_text() == desktops_page.DESCRIPTION


def test_item_page(driver, base_url):
    item_page = ItemPage(driver)
    item_page.open(base_url + item_page.PATH)

    item_page.verify_element_presence(item_page.ITEM_PICTURES)
    item_page.verify_element_presence(item_page.ADD_TO_CART)
    item_page.verify_element_presence(item_page.COMPARE_THIS_PRODUCT)
    item_page.verify_element_presence(item_page.ADD_TO_WISHLIST)
    item_page.verify_element_presence(item_page.DESCRIPTION_TAB)
    item_page.verify_element_presence(item_page.SPECIFICATION_TAB)
    item_page.verify_element_presence(item_page.REVIEWS_TAB)


def test_admin_page(driver, base_url):
    admin_page = AdminPage(driver)
    admin_page.open(base_url + admin_page.PATH)

    admin_page.verify_element_presence(admin_page.USERNAME_INPUT)
    admin_page.verify_element_presence(admin_page.PASSWORD_INPUT)
    admin_page.verify_element_presence(admin_page.FORGOTTEN_PASSWORD_LINK)
    admin_page.verify_element_presence(admin_page.LOGIN_BUTTON)
    assert admin_page.get_element_text(admin_page.TITLE) == admin_page.TITLE_TEXT
    assert admin_page.get_element_text(admin_page.USERNAME_TITLE) == admin_page.USERNAME_TITLE_TEXT
    assert admin_page.get_element_text(admin_page.PASSWORD_TITLE) == admin_page.PASSWORD_TITLE_TEXT


def test_registration_page(driver, base_url):
    registration_page = RegistrationPage(driver)
    registration_page.open(base_url + registration_page.PATH)

    assert registration_page.get_element_text(registration_page.TITLE) == registration_page.TITLE_TEXT
    registration_page.verify_element_presence(registration_page.FIRST_NAME_INPUT)
    registration_page.verify_element_presence(registration_page.LAST_NAME_INPUT)
    registration_page.verify_element_presence(registration_page.EMAIL_INPUT)
    registration_page.verify_element_presence(registration_page.PHONE_INPUT)
    registration_page.verify_element_presence(registration_page.PASSWORD_INPUT)
    registration_page.verify_element_presence(registration_page.PASSWORD_CONFIRM_INPUT)
    registration_page.verify_element_presence(registration_page.CONTINUE_BUTTON)

    assert WebDriverWait(driver, 1).until(
        ec.visibility_of_element_located(registration_page.TITLE)).text == registration_page.TITLE_TEXT
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.FIRST_NAME_INPUT))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.LAST_NAME_INPUT))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.EMAIL_INPUT))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.PHONE_INPUT))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.PASSWORD_INPUT))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.PASSWORD_CONFIRM_INPUT))
    WebDriverWait(driver, 1).until(ec.visibility_of_element_located(registration_page.CONTINUE_BUTTON))
