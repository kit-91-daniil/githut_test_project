import pytest
from .pages.code_editor_page import CodeEditorPage
from .pages.header_section import HeaderSection
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.repository_page import RepositoryPage
from .pages.create_repository_page import CreateRepositoryPage
from .pages.repository_settings_page import RepositorySettingPage
from .pages.urls import Urls
from .utilites import helper
from .pages.logger_file import logger


class TestUserLogIn:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page_url = Urls.LOGIN_PAGE_URL
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        login_page.sign_in()

    @pytest.mark.correct_user_is_logged_in
    def test_correct_user_is_logged_in(self, browser):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.should_be_authorized_user()


class TestCreateDeleteRenameRepository:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page_url = Urls.LOGIN_PAGE_URL
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        login_page.sign_in()

    @pytest.fixture(scope="function", autouse=False)
    def prepare_new_repository_delete(self, browser):
        self.unique_repository_name = helper.generate_unique_name()
        header_section = HeaderSection(browser, browser.current_url)
        header_section.go_to_create_repository_page()
        create_repository_page = CreateRepositoryPage(browser, browser.current_url)
        create_repository_page.create_new_repository(self.unique_repository_name)
        yield self.unique_repository_name
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_repository_settings_page()
        repository_setting_page = RepositorySettingPage(browser, browser.current_url)
        repository_setting_page.delete_the_repository()

    @pytest.fixture(scope="function", autouse=False)
    def delete_repository_after_creating_test(self, browser):
        yield
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_repository_page(self.unique_repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_repository_settings_page()
        repository_setting_page = RepositorySettingPage(browser, browser.current_url)
        repository_setting_page.delete_the_repository()

    @pytest.fixture(scope="function", autouse=False)
    def create_repository_before_deleting_test(self, browser):
        self.unique_repository_name = helper.generate_unique_name()
        header_section = HeaderSection(browser, browser.current_url)
        header_section.go_to_create_repository_page()
        create_repository_page = CreateRepositoryPage(browser, browser.current_url)
        create_repository_page.create_new_repository(repository_name_=self.unique_repository_name)
        yield self.unique_repository_name

    @pytest.mark.create_repository
    def test_user_can_create_repository(self, browser, delete_repository_after_creating_test):
        self.unique_repository_name = helper.generate_unique_name()
        header_section = HeaderSection(browser, browser.current_url)
        header_section.go_to_create_repository_page()
        create_repository_page = CreateRepositoryPage(browser, browser.current_url)
        create_repository_page.create_new_repository(repository_name_=self.unique_repository_name)
        logger.info("Created new repository")
        repository_page = RepositoryPage(browser, browser.current_url)
        logger.info("on repository page")
        repository_page.should_have_repository_correct_name(expected_rep_name=self.unique_repository_name)
        header_section = HeaderSection(browser, browser.current_url)
        header_section.go_to_main_page()
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_repository_link_by_name(repository_name=self.unique_repository_name)
        res = delete_repository_after_creating_test

    @pytest.mark.delete_repository
    def test_user_can_delete_repository(self, browser, create_repository_before_deleting_test):
        repository_name = create_repository_before_deleting_test
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.go_to_repository_page(repository_name=repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_repository_settings_page()
        repository_setting_page = RepositorySettingPage(browser, browser.current_url)
        repository_setting_page.delete_the_repository()
        header_section = HeaderSection(browser, browser.current_url)
        header_section.go_to_main_page()
        main_page = MainPage(browser, browser.current_url)
        main_page.should_not_be_repository_link_by_name(repository_name=repository_name)

    @pytest.mark.rename_repository
    def test_user_can_rename_repository(self, browser, prepare_new_repository_delete):
        repository_name = prepare_new_repository_delete
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.go_to_repository_page(repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_repository_settings_page()
        repository_setting_page = RepositorySettingPage(browser, browser.current_url)
        new_repository_name = repository_setting_page.rename_repository(repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.should_have_repository_correct_name(new_repository_name)


class TestRepositoryFilling:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page_url = Urls.LOGIN_PAGE_URL
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        login_page.sign_in()

    @pytest.fixture(scope="function", autouse=False)
    def prepare_new_repository_delete(self, browser):
        self.unique_repository_name = helper.generate_unique_name()
        header_section = HeaderSection(browser, browser.current_url)
        header_section.go_to_create_repository_page()
        create_repository_page = CreateRepositoryPage(browser, browser.current_url)
        create_repository_page.create_new_repository(self.unique_repository_name)
        yield self.unique_repository_name
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_repository_settings_page()
        repository_setting_page = RepositorySettingPage(browser, browser.current_url)
        repository_setting_page.delete_the_repository()

    @pytest.mark.add_readme
    def test_user_can_add_readme_file(self, browser, prepare_new_repository_delete):
        repository_name = prepare_new_repository_delete
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_repository_page(repository_name=repository_name)
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_create_readme_file_page()
        editor_page = CodeEditorPage(browser, browser.current_url)
        editor_page.create_file()
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.should_be_file_link("README.md")
