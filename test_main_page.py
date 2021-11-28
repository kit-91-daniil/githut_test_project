import pytest
import allure
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators, LoginPageLocators, RepositoriesPageLocators, \
    CreateRepositoryPageLocators, RepositoryPageLocators, RepositorySettingsPageLocators
from .pages.login_page import LoginPage
from .pages.repository_page import RepositoryPage
from .pages.repositories_page import RepositoriesPage
from .pages.create_repository_page import CreateRepositoryPage
from .pages.repository_settings_page import RepositorySettingPage
from configs import config
from .pages.base_page import logger_expect_no_error
from .pages.base_page import logger


@allure.severity(allure.severity_level.NORMAL)
class TestLogInCreateDeleteRepository:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        logger.info("Start signing in")
        login_page_url = LoginPageLocators.LOGIN_PAGE_URL
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        assert login_page.sign_in(), "Login password were not send"
        main_page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
        main_page.open()
        main_page.should_be_authorized_user()
        logger.info("Signed in")

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

    @pytest.fixture(scope="function", autouse=False)
    def delete_repository_after_creating_test(self, browser):
        yield
        repository_setting_url = RepositorySettingsPageLocators.create_rep_settings_url(
            config.login, self.unique_rep_name)
        repository_setting_page = RepositorySettingPage(browser, repository_setting_url)
        repository_setting_page.open()
        repository_setting_page.delete_the_repository()

    @pytest.fixture(scope="function", autouse=False)
    def create_repository_before_deleting_test(self, browser):
        new_repository_page_url = CreateRepositoryPageLocators.NEW_REPOSITORY_PAGE_URL
        new_repository_page = CreateRepositoryPage(browser, new_repository_page_url)
        new_repository_page.open()
        self.unique_rep_name = new_repository_page.generate_unique_name()
        new_repository_page.create_new_repository(self.unique_rep_name)
        yield self.unique_rep_name

    @pytest.mark.correct_user_is_logged_in
    @logger_expect_no_error
    def test_user_should_be_authorized(self, browser):
        pass

    @pytest.mark.create_repository
    @logger_expect_no_error
    def test_user_can_create_repository(self, browser, delete_repository_after_creating_test):
        main_page_url = MainPageLocators.MAIN_PAGE_URL
        main_page = MainPage(browser, main_page_url)
        self.unique_rep_name = main_page.generate_unique_name()
        main_page.open()
        main_page.go_to_create_repository_page()
        create_repository_page = CreateRepositoryPage(browser, browser.current_url)
        create_repository_page.open()
        create_repository_page.create_new_repository(self.unique_rep_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.should_have_repository_correct_name(self.unique_rep_name)
        res = delete_repository_after_creating_test

    @pytest.mark.delete_repository
    @logger_expect_no_error
    def test_user_can_delete_repository(self, browser, create_repository_before_deleting_test):
        repository_name = create_repository_before_deleting_test
        repositories_page_url = RepositoriesPageLocators.generate_repositories_page_url()
        repositories_page = RepositoriesPage(browser, repositories_page_url)
        repositories_page.open()
        repositories_page.go_to_repository_page_by_name(repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.open()
        repository_page.go_to_repository_settings_page()
        repository_setting_page = RepositorySettingPage(browser, browser.current_url)
        repository_setting_page.delete_the_repository()
        main_page = MainPage(browser, browser.current_url)
        main_page.open()
        main_page.should_not_be_repository_link_by_name(repository_name)

    @logger_expect_no_error
    def test_user_can_go_to_repository_page(self, browser, prepare_new_repository_delete):
        repository_name = prepare_new_repository_delete
        repository_page_url = RepositoryPageLocators.generate_repository_page_url_by_name(
            username=config.login, repository_name=repository_name)
        repository_page = RepositoryPage(browser, repository_page_url)
        repository_page.open()
        repository_page.should_have_repository_correct_name(repository_name)

    @logger_expect_no_error
    def test_user_can_go_repositories_page(self, browser):
        main_page_url = MainPageLocators.MAIN_PAGE_URL
        main_page = MainPage(browser, main_page_url)
        main_page.open()
        main_page.go_to_repositories_page()
        repositories_page = RepositoriesPage(browser, browser.current_url)
        repositories_page.should_be_repositories_search_form()
