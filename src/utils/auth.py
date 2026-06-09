from selenium.common.exceptions import TimeoutException

from src.constants.urls import APP_ROUTE_PREFIX
from src.pages.app_shell_page import AppShellPage
from src.pages.login_page import LoginPage
from src.utils.config import get_env


def login_with_default_account(driver, locale=None):
    page = LoginPage(driver, locale=locale)
    page.open_login_page()
    page.login(get_env("USERNAME_1", ""), get_env("PASSWORD_1", ""))
    try:
        page.wait_for(lambda current_driver: APP_ROUTE_PREFIX in current_driver.current_url, timeout=30)
        return page
    except TimeoutException:
        pass

    shell = AppShellPage(driver, locale=locale)
    try:
        shell.wait_until_loaded()
        return page
    except AssertionError:
        pass

    diagnostics = {
        "current_url": driver.current_url,
        "page_title": driver.title,
        "login_error": page.try_get_error_message(),
    }
    raise AssertionError(f"Login did not reach the app shell: {diagnostics}")
    return page
