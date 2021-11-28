import pytest
import allure
from allure_commons.types import AttachmentType
from .pages.locators import LoginPageLocators, CreateRepositoryPageLocators, RepositorySettingsPageLocators
from .pages.login_page import LoginPage
from .pages.repository_page import RepositoryPage
from .pages.create_repository_page import CreateRepositoryPage
from .pages.repository_settings_page import RepositorySettingPage
from configs import config
from .pages.base_page import logger_expect_no_error


# @pytest.mark.creating_repository
class TestRepositorySettingsPage:
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

    @pytest.mark.rename_repository
    @logger_expect_no_error
    def test_user_can_rename_repository(self, browser, prepare_new_repository_delete):
        repository_name = prepare_new_repository_delete
        rep_settings_url = RepositorySettingsPageLocators.create_rep_settings_url(
            username=config.login, repository_name=repository_name)
        rep_settings_page = RepositorySettingPage(browser, rep_settings_url)
        rep_settings_page.open()
        new_rep_name = rep_settings_page.rename_repository(repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.open()
        repository_page.should_have_repository_correct_name(new_rep_name)

