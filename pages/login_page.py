from .base_page import BasePage
from .locators import LoginPageLocators
from configs.config import TestData


class LoginPage(BasePage):
    def sign_in(self):
        login_input_field = self.find_element_after_explicit_waiting(*LoginPageLocators.LOGIN_FIELD)
        password_input_field = self.find_element_after_explicit_waiting(*LoginPageLocators.PASSWORD_FIELD)
        login_input_field.send_keys(TestData.LOGIN)
        password_input_field.send_keys(TestData.PASSWORD)
        return self.click_element_to_be_visible_after_explicit_waiting(*LoginPageLocators.SUBMIT_BUTTON)
