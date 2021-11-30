from selenium.webdriver.common.by import By
import sys
import os.path

# For import from a parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


class BasePageLocators:
    def __init__(self, *args, **kwargs):
        super(BasePageLocators, self).__init__(*args, **kwargs)


class CreateRepositoryPageLocators(BasePageLocators):
    NEW_REPOSITORY_NAME_INPUT = (By.CSS_SELECTOR, "#repository_name")
    NEW_REPOSITORY_CHECKBOX_ADD_README = (By.CSS_SELECTOR, "#repository_auto_init")
    NEW_REPOSITORY_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#new_repository > div.js-with-permission-fields > button")


class HeaderSectionLocators(BasePageLocators):
    NAVBAR_DROPDOWN_CARET = (By.CSS_SELECTOR, "div:nth-child(7) > details")
    NAVBAR_USER_REPOSITORIES_BUTTON = (By.CSS_SELECTOR, "a[href$='repositories']")
    NAVBAR_ADD_DROPDOWN_CARET = (By.CSS_SELECTOR, "div:nth-child(6) > details")
    NAVBAR_NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "a[href='/new']")
    USER_SIGN_IN_ASSURANCE = (By.CSS_SELECTOR, "details-menu > div > a > strong")
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, "[href='https://github.com/']")


class LoginPageLocators(BasePageLocators):
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    INCORRECT_CREDS_FLASH_MESSAGE = (By.CSS_SELECTOR, "#js-flash-container > div.flash-error")


class MainPageLocators(BasePageLocators):
    pass


class RepositoriesPageLocators(BasePageLocators):
    REPOSITORIES_PAGE_NEW_REPO_BUTTON = (By.CSS_SELECTOR, "form+div>[href='/new']")
    REPOSITORIES_SEARCH_FORM = (By.CSS_SELECTOR, "#your-repos-filter")
    REPOSITORY_LINK_SELECTOR_PATTERN = "[href$='/{repository_name}']"

    @classmethod
    def create_defined_repository_link_locator(cls, repository_name):
        return By.CSS_SELECTOR, cls.REPOSITORY_LINK_SELECTOR_PATTERN.format(repository_name=repository_name)


class RepositoryPageLocators(BasePageLocators):
    REPOSITORY_NAME = (By.CSS_SELECTOR, "strong > a")
    REPOSITORY_SETTING_BUTTON = (By.CSS_SELECTOR, "#settings-tab")
    ADD_README_FILE = (By.CSS_SELECTOR, "[href*='?readme=']")
    README_FILE_LINK = (By.CSS_SELECTOR, "span>[href$='README.md']")
    FILENAME_SELECTOR = "[href$='{filename}']"

    @classmethod
    def generate_link_by_filename(cls, filename):
        return By.CSS_SELECTOR, cls.FILENAME_SELECTOR.format(filename=filename)


class RepositorySettingsPageLocators(BasePageLocators):
    SETTINGS_PAGE_SUBHEADER = (By.CSS_SELECTOR, "#options_bucket > div:nth-child(1) > h2")
    NAME_FIELD = (By.CSS_SELECTOR, "#rename-field")
    RENAME_SUBNIT_BUTTON = (By.CSS_SELECTOR, "#options_bucket>form> button")

    REPOSITORY_DELETE_BUTTON = (By.CSS_SELECTOR, ".color-border-danger li:nth-child(4) summary")
    DELETING_ASSURANCE_MESSAGE_TO_TYPE = (By.CSS_SELECTOR,
                                          "ul > li:nth-child(4) > details  p:nth-child(2) > strong")
    DELETING_ASSURANCE_INPUT_FIELD = (By.CSS_SELECTOR, "li:nth-child(4) form>p>input")
    DELETING_ASSURANCE_SUBMIT_BUTTON = (By.CSS_SELECTOR, "li:nth-child(4)  .d-md-inline-block")


class CodeEditorPageLocators(BasePageLocators):
    CODE_EDITOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-file")
    CODE_EDITOR_TEXT_FIELD = (By.CSS_SELECTOR, ".CodeMirror")


class SessionPageLocators(BasePageLocators):
    INCORRECT_USER_LOGGING_IN_MESSAGE = (By.CSS_SELECTOR, "#js-flash-container > div > div")


class UserRepositoryTreeBranchPageLocators(BasePageLocators):
    TREE_MAIN_README_LINK = (By.CSS_SELECTOR, "div[role='rowheader'] > span > a")
