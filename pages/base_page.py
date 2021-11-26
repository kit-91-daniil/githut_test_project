import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    # @staticmethod
    def generate_unique_name(self):
        """This method should be static"""
        return "repository" + str(time.time()).replace(".", "-")

    def do_click_explicit_waiting(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located((how, what))).click()
        except TimeoutException:
            return False
        return True

    def do_click_waiting_active_element(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable((how, what))).click()
        except TimeoutException:
            return False
        return True

    def find_element_expl_waiting(self, how, what, timeout=4):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return element

    def is_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present_and_has_a_text(self, how, what, timeout=4):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        result = element.text if hasattr(element, "text") else True
        return result

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def is_user_authorized(self):
        return self.is_element_present(*BasePageLocators.NAVBAR_DROPDOWN_CARET)

    def go_to_create_repository_page(self):
        self.do_click_explicit_waiting(*BasePageLocators.NAVBAR_ADD_DROPDOWN_CARET)
        self.do_click_explicit_waiting(*BasePageLocators.NAVBAR_NEW_REPOSITORY_BUTTON)

    def go_to_repositories_page(self):
        self.do_click_explicit_waiting(*BasePageLocators.NAVBAR_DROPDOWN_CARET)
        self.do_click_explicit_waiting(*BasePageLocators.NAVBAR_USER_REPOSITORIES_BUTTON)

    def go_to_defined_by_name_repository_page(self, rep_name):
        rep_css_selector = f"[href$='/{rep_name}']"
        self.do_click_explicit_waiting(By.CSS_SELECTOR, rep_css_selector)
