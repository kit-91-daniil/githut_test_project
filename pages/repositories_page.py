from .base_page import BasePage
from .locators import RepositoriesPageLocators


class RepositoriesPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(RepositoriesPage, self).__init__(*args, **kwargs)

    def go_to_repository_page_by_name(self, repository_name):
        repository_link_locator = RepositoriesPageLocators.create_defined_repository_link_locator(repository_name)
        assert self.do_click_explicit_waiting(*repository_link_locator), "Defined repository link is not present"

    def should_be_repositories_search_form(self):
        assert self.find_element_expl_waiting(*RepositoriesPageLocators.REPOSITORIES_SEARCH_FORM), \
            "Repositories search form is not present"
