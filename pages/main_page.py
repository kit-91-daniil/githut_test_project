import allure
from allure_commons.types import AttachmentType
from .base_page import BasePage
from .locators import MainPageLocators, RepositoriesPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_not_be_repository_link_by_name(self, repository_name):
        repository_locator = RepositoriesPageLocators.create_defined_repository_link_locator(repository_name)
        assert self.is_not_element_present(*repository_locator), "The repository link is not present on main page"

    def should_be_authorized_user(self):
        if not self.is_user_authorized():
            allure.attach(self.browser.get_screenshot_as_png(), name="User is not authorized",
                          attachment_type=AttachmentType.PNG)
            assert False, "User is not authorized"
