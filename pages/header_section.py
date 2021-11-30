from .base_page import BasePage
from .locators import HeaderSectionLocators


class HeaderSection(BasePage):
    def go_to_create_repository_page(self):
        self.click_element_to_be_visible_after_explicit_waiting(*HeaderSectionLocators.NAVBAR_ADD_DROPDOWN_CARET)
        self.click_element_to_be_visible_after_explicit_waiting(*HeaderSectionLocators.NAVBAR_NEW_REPOSITORY_BUTTON)

    def go_to_repositories_page(self):
        self.click_element_to_be_visible_after_explicit_waiting(*HeaderSectionLocators.NAVBAR_DROPDOWN_CARET)
        self.click_element_to_be_visible_after_explicit_waiting(*HeaderSectionLocators.NAVBAR_USER_REPOSITORIES_BUTTON)

    def go_to_main_page(self):
        self.click_element_to_be_visible_after_explicit_waiting(*HeaderSectionLocators.MAIN_PAGE_LINK)
