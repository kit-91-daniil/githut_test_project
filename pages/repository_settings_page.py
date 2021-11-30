from .base_page import BasePage
from .locators import RepositorySettingsPageLocators
from .logger_file import logger
import time


class RepositorySettingPage(BasePage):
    def delete_the_repository(self):
        self.click_element_to_be_visible_after_explicit_waiting(
            *RepositorySettingsPageLocators.REPOSITORY_DELETE_BUTTON)
        assurance_text = self.find_element_after_explicit_waiting(
            *RepositorySettingsPageLocators.DELETING_ASSURANCE_MESSAGE_TO_TYPE, timeout=7)
        assurance_input_field = self.find_element_after_explicit_waiting(
            *RepositorySettingsPageLocators.DELETING_ASSURANCE_INPUT_FIELD, timeout=7)
        assurance_input_field.send_keys(assurance_text.text)
        self.click_element_to_be_active_after_explicit_waiting(
            *RepositorySettingsPageLocators.DELETING_ASSURANCE_SUBMIT_BUTTON, timeout=7)

    def rename_repository(self, repository_name) -> str:
        name_field = self.find_element_after_explicit_waiting(*RepositorySettingsPageLocators.NAME_FIELD)
        new_repository_name = repository_name + "_renamed"
        name_field.clear()
        name_field.send_keys(new_repository_name)
        self.click_element_to_be_active_after_explicit_waiting(*RepositorySettingsPageLocators.RENAME_SUBNIT_BUTTON, timeout=6)
        return new_repository_name
