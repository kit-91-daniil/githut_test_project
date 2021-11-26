from .base_page import BasePage
from .locators import RepositorySettingsPageLocators


class RepositorySettingPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(RepositorySettingPage, self).__init__(*args, **kwargs)

    def delete_the_repository(self):
        assert self.do_click_explicit_waiting(*RepositorySettingsPageLocators.REPOSITORY_DELETE_BUTTON), \
            "Delete repository button is not present"
        assurance_text = self.find_element_expl_waiting(
            *RepositorySettingsPageLocators.DELETING_ASSURANCE_MESSAGE_TO_TYPE).text
        assert assurance_text, "Deleting assurance text not present"
        assurance_input_field = self.find_element_expl_waiting(
            *RepositorySettingsPageLocators.DELETING_ASSURANCE_INPUT_FIELD)
        assurance_input_field.send_keys(assurance_text)
        assert self.do_click_waiting_active_element(
            *RepositorySettingsPageLocators.DELETING_ASSURANCE_SUBMIT_BUTTON), "Delete assurance button si not active"

    def rename_repository(self, repository_name) -> str:
        name_field = self.find_element_expl_waiting(*RepositorySettingsPageLocators.NAME_FIELD)
        new_repository_name = repository_name + "_renamed"
        name_field.clear()
        name_field.send_keys(new_repository_name)
        assert self.do_click_waiting_active_element(*RepositorySettingsPageLocators.RENAME_SUBNIT_BUTTON), \
            "Rename submit button is not present or not active"
        return new_repository_name
