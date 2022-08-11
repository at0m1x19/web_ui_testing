from page_objects.admin_page import AdminPage
from page_objects.main_page import MainPage
from page_objects.desktops_page import DesktopsPage
from page_objects.item_page import ItemPage
from page_objects.registration_page import RegistrationPage
from page_objects.elements.currency_switcher import CurrencySwitcher


def test_main_page(driver, base_url):
    main_page = MainPage(driver, base_url)

    main_page.open()
    main_page.verify_page_title(main_page.TITLE)
    main_page.verify_element_presence(main_page.SLIDER)
    main_page.verify_element_presence(main_page.FEATURED_TITLE)
    main_page.verify_element_presence(main_page.FEATURED_ITEMS_LIST)
    main_page.verify_element_presence(main_page.ADS_CAROUSEL)
    assert main_page.get_number_of_featured_items() == main_page.EXPECTED_FEATURED_ITEMS_AMOUNT


def test_desktops_page(driver, base_url):
    desktops_page = DesktopsPage(driver, base_url)

    desktops_page.open()
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
    item_page = ItemPage(driver, base_url)

    item_page.open()
    item_page.verify_element_presence(item_page.ITEM_PICTURES)
    item_page.verify_element_presence(item_page.ADD_TO_CART)
    item_page.verify_element_presence(item_page.COMPARE_THIS_PRODUCT)
    item_page.verify_element_presence(item_page.ADD_TO_WISHLIST)
    item_page.verify_element_presence(item_page.DESCRIPTION_TAB)
    item_page.verify_element_presence(item_page.SPECIFICATION_TAB)
    item_page.verify_element_presence(item_page.REVIEWS_TAB)


def test_admin_page(driver, base_url):
    admin_page = AdminPage(driver, base_url)

    admin_page.open()
    admin_page.verify_element_presence(admin_page.USERNAME_INPUT)
    admin_page.verify_element_presence(admin_page.PASSWORD_INPUT)
    admin_page.verify_element_presence(admin_page.FORGOTTEN_PASSWORD_LINK)
    admin_page.verify_element_presence(admin_page.SUBMIT_BUTTON)
    assert admin_page.get_element_text(admin_page.TITLE) == admin_page.TITLE_TEXT
    assert admin_page.get_element_text(admin_page.USERNAME_TITLE) == admin_page.USERNAME_TITLE_TEXT
    assert admin_page.get_element_text(admin_page.PASSWORD_TITLE) == admin_page.PASSWORD_TITLE_TEXT


def test_registration_page(driver, base_url):
    registration_page = RegistrationPage(driver, base_url)

    registration_page.open()
    assert registration_page.get_element_text(registration_page.TITLE) == registration_page.TITLE_TEXT
    registration_page.verify_element_presence(registration_page.FIRST_NAME_INPUT)
    registration_page.verify_element_presence(registration_page.LAST_NAME_INPUT)
    registration_page.verify_element_presence(registration_page.EMAIL_INPUT)
    registration_page.verify_element_presence(registration_page.PHONE_INPUT)
    registration_page.verify_element_presence(registration_page.PASSWORD_INPUT)
    registration_page.verify_element_presence(registration_page.PASSWORD_CONFIRM_INPUT)
    registration_page.verify_element_presence(registration_page.CONTINUE_BUTTON)


def test_adding_and_removing_new_item(driver, base_url):
    item_name = "New Test Item"
    item_model = "New model X"
    admin_page = AdminPage(driver, base_url)

    admin_page.open()
    admin_page.login()
    admin_page.add_product(item_name, item_model)
    admin_page.filter_products_by_name_and_model(item_name, item_model)
    assert admin_page.get_element_text(admin_page.FILTERED_RESULTS_TEXT) == "Showing 1 to 1 of 1 (1 Pages)"
    admin_page.remove_products_by_name_and_model(item_name, item_model)
    admin_page.filter_products_by_name_and_model(item_name, item_model)
    assert admin_page.get_element_text(admin_page.FILTERED_RESULTS_TEXT) == "Showing 0 to 0 of 0 (0 Pages)"


def test_register_user(driver, base_url, faker_email):
    register_page = RegistrationPage(driver, base_url)

    register_page.open()
    register_page.register_user(email=faker_email)
    assert register_page.get_element_text(
        register_page.SUCCESS_PAGE_TITLE) == register_page.SUCCESSFUL_REGISTRATION_MESSAGE
    my_account_page = register_page.submit_successful_registration_message()
    assert my_account_page.get_element_text(my_account_page.TITLE) == my_account_page.PAGE_TITLE


def test_switch_currency(driver, base_url):
    main_page = MainPage(driver, base_url)
    currency_switcher = CurrencySwitcher(driver, base_url)

    main_page.open()
    currency_switcher.switch_currency_to("EUR")
    main_page.verify_if_price_in_correct_currency("EUR")
    currency_switcher.switch_currency_to("GBP")
    main_page.verify_if_price_in_correct_currency("GBP")
    currency_switcher.switch_currency_to("USD")
    main_page.verify_if_price_in_correct_currency("USD")
