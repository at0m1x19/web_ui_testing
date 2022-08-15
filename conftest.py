import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
from faker import Faker

load_dotenv()


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise AttributeError(f"Browser '{browser_name}' is not supported")

    request.addfinalizer(driver.close)

    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='function', autouse=True)
def faker_email():
    faker = Faker()
    return faker.email()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run")
    parser.addoption("--url", default="http://192.168.3.6:8081", help="Base host URL")

