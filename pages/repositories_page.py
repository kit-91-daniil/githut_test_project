from .base_page import BasePage
from .locators import RepositoriesPageLocators


class RepositoriesPage(BasePage):
    def go_to_repository_page_by_name(self, repository_name):
        repository_link_locator = RepositoriesPageLocators.create_defined_repository_link_locator(repository_name)
        self.click_element_to_be_visible_after_explicit_waiting(*repository_link_locator)

    def should_be_repositories_search_form(self):
        self.find_element_after_explicit_waiting(*RepositoriesPageLocators.REPOSITORIES_SEARCH_FORM)
