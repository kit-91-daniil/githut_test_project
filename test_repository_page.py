import pytest
from .pages.code_editor_page import CodeEditorPage
from .pages.create_repository_page import CreateRepositoryPage
from .pages.locators import LoginPageLocators, RepositoryPageLocators
from .pages.login_page import LoginPage
from .pages.repository_page import RepositoryPage
from .pages.repository_settings_page import RepositorySettingPage
from .pages.locators import CreateRepositoryPageLocators, RepositorySettingsPageLocators
from pages.base_page import logger_expect_no_error
from configs import config


class TestRepositoryPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        print("Start sign in operation")
        login_page_url = LoginPageLocators.LOGIN_PAGE_URL
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        login_page.sign_in()
        print("Signed in")

    @pytest.fixture(scope="function", autouse=False)
    def prepare_new_repository_delete(self, browser):
        new_repository_page_url = CreateRepositoryPageLocators.NEW_REPOSITORY_PAGE_URL
        new_repository_page = CreateRepositoryPage(browser, new_repository_page_url)
        new_repository_page.open()
        self.unique_rep_name = new_repository_page.generate_unique_name()
        new_repository_page.create_new_repository(self.unique_rep_name)
        yield self.unique_rep_name
        repository_settings_page_url = RepositorySettingsPageLocators.create_rep_settings_url(
            config.login, self.unique_rep_name)
        repository_setting_page = RepositorySettingPage(browser, repository_settings_page_url)
        repository_setting_page.open()
        repository_setting_page.delete_the_repository()

    @pytest.mark.add_readme
    @logger_expect_no_error
    def test_user_can_add_readme_file(self, browser, prepare_new_repository_delete):
        repository_name = prepare_new_repository_delete
        repository_page_url = RepositoryPageLocators.generate_repository_page_url_by_name(
            username=config.login, repository_name=repository_name)
        repository_page = RepositoryPage(browser, repository_page_url)
        repository_page.open()
        repository_page.go_to_create_readme_file_page()
        editor_page = CodeEditorPage(browser, browser.current_url)
        editor_page.open()
        editor_page.create_file()
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.open()
        repository_page.should_be_file_link("README.md")
