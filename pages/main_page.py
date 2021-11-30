import allure
from allure_commons.types import AttachmentType
from .base_page import BasePage
from .locators import MainPageLocators, RepositoriesPageLocators, HeaderSectionLocators


class MainPage(BasePage):
    def go_to_repository_page(self, repository_name):
        repository_link_locator = RepositoriesPageLocators.create_defined_repository_link_locator(repository_name)
        self.click_element_to_be_visible_after_explicit_waiting(*repository_link_locator)

    def is_user_authorized(self):
        return self.is_element_present(*HeaderSectionLocators.NAVBAR_DROPDOWN_CARET)

    def should_not_be_repository_link_by_name(self, repository_name):
        repository_locator = RepositoriesPageLocators.create_defined_repository_link_locator(repository_name)
        assert self.is_not_element_present(*repository_locator), "The repository link is present on main page"

    def should_be_repository_link_by_name(self, repository_name):
        repository_locator = RepositoriesPageLocators.create_defined_repository_link_locator(repository_name)
        assert self.is_element_present(*repository_locator), "The repository link is not present on main page"

    def should_be_authorized_user(self):
        assert self.is_user_authorized(), "User is not authorized"
