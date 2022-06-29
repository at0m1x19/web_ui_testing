import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv

load_dotenv()  # add your GH_TOKEN to .env file


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise AttributeError(f"Browser '{browser_name}' is not supported")

    request.addfinalizer(browser.close)

    return browser


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run")
    parser.addoption("--url", default="http://10.14.77.199:8081", help="Base URL")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
