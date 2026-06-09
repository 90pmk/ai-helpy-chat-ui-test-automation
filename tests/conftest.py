import pytest

from src.data.accounts import TEST_ACCOUNTS
from src.pages.agent_builder_page import AgentBuilderPage
from src.pages.agents_page import AgentsPage
from src.pages.app_shell_page import AppShellPage
from src.pages.chat_page import ChatPage
from src.pages.login_page import LoginPage
from src.pages.token_page import TokenPage
from src.pages.tools.quiz_tool_page import QuizToolPage
from src.pages.tools.tools_home_page import ToolsHomePage
from src.utils.auth import login_with_default_account
from src.utils.config import get_env
from src.utils.driver_factory import create_chrome_driver
from src.utils.screenshot import capture_screenshot


@pytest.fixture
def driver():
    driver = create_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open_login_page()
    return page


@pytest.fixture
def credentials():
    return {
        "username": get_env("USERNAME_1", ""),
        "password": get_env("PASSWORD_1", ""),
    }


@pytest.fixture
def accounts():
    return TEST_ACCOUNTS


@pytest.fixture
def authenticated_login(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Authentication requires USERNAME_1/PASSWORD_1 environment variables.")
    return login_with_default_account(driver)


@pytest.fixture
def app_shell(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("App shell requires USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return AppShellPage(driver)


@pytest.fixture
def chat_page(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Chat tests require USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return ChatPage(driver)


@pytest.fixture
def tools_page(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Tools tests require USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return ToolsHomePage(driver)


@pytest.fixture
def quiz_tool_page(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Quiz tests require USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return QuizToolPage(driver)


@pytest.fixture
def agents_page(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Agent tests require USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return AgentsPage(driver)


@pytest.fixture
def agent_builder_page(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Agent builder tests require USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return AgentBuilderPage(driver)


@pytest.fixture
def token_page(driver, credentials):
    if not credentials["username"] or not credentials["password"]:
        pytest.skip("Token checks require USERNAME_1/PASSWORD_1 environment variables.")
    login_with_default_account(driver)
    return TokenPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.passed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    screenshots_dir = "screenshots"
    filename = (
        f"{item.nodeid.replace('::', '__').replace('/', '_').replace('\\\\', '_')}"
        f"__{report.when}.png"
    )
    capture_screenshot(driver, f"{screenshots_dir}\\{filename}")
