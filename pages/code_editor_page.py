from .base_page import BasePage
from .locators import MainPageLocators, RepositoriesPageLocators, CodeEditorPageLocators


class CodeEditorPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CodeEditorPage, self).__init__(*args, **kwargs)

    def create_file(self):
        self.should_be_editor_text_field()
        self.click_editor_page_submit_button()

    def should_be_editor_text_field(self):
        assert self.is_element_present(*CodeEditorPageLocators.CODE_EDITOR_TEXT_FIELD), \
            "Code editor field is not present"

    def click_editor_page_submit_button(self):
        assert self.do_click_explicit_waiting(*CodeEditorPageLocators.CODE_EDITOR_SUBMIT_BUTTON), \
            "Code editor submit button is not present"
