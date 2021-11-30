from .base_page import BasePage
from .locators import RepositoryPageLocators


class RepositoryPage(BasePage):
    def should_have_repository_correct_name(self, expected_rep_name):
        actual_rep_name = self.find_element_after_explicit_waiting(*RepositoryPageLocators.REPOSITORY_NAME)
        assert actual_rep_name.text == expected_rep_name, \
            "Actual repository name not equal to expected one"

    def go_to_repository_settings_page(self):
        self.click_element_to_be_visible_after_explicit_waiting(*RepositoryPageLocators.REPOSITORY_SETTING_BUTTON)

    def go_to_create_readme_file_page(self):
        self.click_element_to_be_visible_after_explicit_waiting(*RepositoryPageLocators.ADD_README_FILE)

    def should_be_file_link(self, filename):
        readme_file_locator = RepositoryPageLocators.generate_link_by_filename(filename=filename)
        assert self.is_element_present(*readme_file_locator), \
            "File link is not present on repository page"
