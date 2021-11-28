import allure
from allure_commons.types import AttachmentType
from .base_page import BasePage
from .locators import LoginPageLocators
from configs import config


class LoginPage(BasePage):
    def sign_in(self):
        login_input_field = self.find_element_expl_waiting(*LoginPageLocators.LOGIN_FIELD)
        password_input_field = self.find_element_expl_waiting(*LoginPageLocators.PASSWORD_FIELD)
        # if not login_input_field:
        #     allure.attach(self.browser.get_screenshot_as_png(), name="noUsernameScreen",
        #                   attachment_type=AttachmentType.PNG)
        #     assert False, "Can't see login input field"
        #
        assert login_input_field, "Can't see password input field"
        login_input_field.send_keys(config.login)
        password_input_field.send_keys(config.password)
        return self.do_click_explicit_waiting(*LoginPageLocators.SUBMIT_BUTTON)
