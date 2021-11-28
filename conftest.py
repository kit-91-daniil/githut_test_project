import os
import allure
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

#
# @pytest.fixture
# def manage_logs(request, autouse=True):
#     """Set log file name same as test name"""
#
#     request.config.pluginmanager.get_plugin("logging-plugin")\
#         .set_log_path(os.path.join('log', request.node.name + '.log'))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
