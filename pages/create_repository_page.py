from .base_page import BasePage
from .locators import CreateRepositoryPageLocators


class CreateRepositoryPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CreateRepositoryPage, self).__init__(*args, **kwargs)

    def create_new_repository(self, repository_name):
        create_rep_name_input = self.find_element_expl_waiting(
            *CreateRepositoryPageLocators.NEW_REPOSITORY_NAME_INPUT)
        create_rep_name_input.send_keys(repository_name)
        create_rep_submit_button_locator = CreateRepositoryPageLocators.CREATE_NEW_REP_BUTTON
        self.do_click_waiting_active_element(*create_rep_submit_button_locator)
