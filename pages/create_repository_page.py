from .base_page import BasePage
from .locators import CreateRepositoryPageLocators
from utilites import helper


class CreateRepositoryPage(BasePage):
    def create_new_repository(self, repository_name_):

        new_repository_name_input = self.find_element_after_explicit_waiting(
            *CreateRepositoryPageLocators.NEW_REPOSITORY_NAME_INPUT)
        new_repository_name_input.send_keys(repository_name_)

        self.click_element_to_be_active_after_explicit_waiting(
            *CreateRepositoryPageLocators.NEW_REPOSITORY_SUBMIT_BUTTON)
