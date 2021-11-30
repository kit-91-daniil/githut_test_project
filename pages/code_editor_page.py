from .base_page import BasePage
from .locators import CodeEditorPageLocators


class CodeEditorPage(BasePage):
    def create_file(self):
        self.should_be_editor_text_field()
        self.click_editor_page_submit_button()

    def should_be_editor_text_field(self):
        assert self.is_element_present(*CodeEditorPageLocators.CODE_EDITOR_TEXT_FIELD), \
            "Code editor field is not present"

    def click_editor_page_submit_button(self):
        self.click_element_to_be_visible_after_explicit_waiting(*CodeEditorPageLocators.CODE_EDITOR_SUBMIT_BUTTON)
