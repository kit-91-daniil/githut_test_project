from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from .pages.base_page import logger


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="choose language: es or en or ru")
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        logger.info("start chrome browser for test..")
        options = Options()
        options.add_argument("--window-size=1400,1050")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        logger.info("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser name should be chrome or firefox")
    yield browser
    logger.info("Close browser")
    browser.quit()
