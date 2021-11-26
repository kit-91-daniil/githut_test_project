from .base_page import BasePage
from .locators import RepositoryPageLocators


class RepositoryPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(RepositoryPage, self).__init__(*args, **kwargs)

    def should_have_repository_correct_name(self, expected_rep_name):
        actual_rep_name = self.find_element_expl_waiting(*RepositoryPageLocators.REPOSITORY_NAME)
        assert actual_rep_name.text == expected_rep_name, \
            "Actual repository name not equal to expected one"

    def go_to_repository_settings_page(self):
        assert self.do_click_explicit_waiting(*RepositoryPageLocators.REPOSITORY_SETTING_BUTTON), \
            "Repository setting button can not be clicked"

    def go_to_create_readme_file_page(self):
        assert self.do_click_explicit_waiting(*RepositoryPageLocators.ADD_README_FILE), \
            "Readme file link is not present"

    def should_be_file_link(self, filename):
        readme_file_locator = RepositoryPageLocators.generate_link_by_filename(filename=filename)
        assert self.is_element_present(*readme_file_locator), \
            "File link is not present on repository page"
