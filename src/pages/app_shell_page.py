from src.components.header_component import HeaderComponent
from src.components.menu_component import MenuComponent
from src.components.sidebar_component import SidebarComponent
from src.constants.urls import AGENTS_PATH, CHAT_HOME_PATH, CHATS_PATH, TOOLS_PATH
from src.locators.app_shell_locators import AppShellLocators
from src.pages.base_page import BasePage


class AppShellPage(BasePage):
    """Shared authenticated layout actions such as navigation and logout."""

    def __init__(self, driver, timeout=10, locale=None):
        super().__init__(driver, timeout=timeout, locale=locale)
        self.header = HeaderComponent(driver, timeout=timeout, locale=self.locale)
        self.sidebar = SidebarComponent(driver, timeout=timeout, locale=self.locale)
        self.menu = MenuComponent(driver, timeout=timeout, locale=self.locale)

    def wait_until_loaded(self):
        candidates = (
            AppShellLocators.TOOLS_LINK,
            AppShellLocators.AGENTS_LINK,
            AppShellLocators.SEARCH_INPUT,
            AppShellLocators.SEARCH_INPUT_FALLBACK,
        )
        for locator in candidates:
            if self.exists(locator):
                return self

        raise AssertionError("App shell did not appear to load.")

    def go_to_chats(self):
        self.sidebar.go_to_chats()
        if CHAT_HOME_PATH not in self.driver.current_url and CHATS_PATH not in self.driver.current_url:
            self.wait_for(lambda driver: CHAT_HOME_PATH in driver.current_url or CHATS_PATH in driver.current_url)
        return self

    def go_to_tools(self):
        self.sidebar.go_to_tools()
        self.wait_for_url_contains(TOOLS_PATH)
        return self

    def go_to_agents(self):
        self.sidebar.go_to_agents()
        self.wait_for_url_contains(AGENTS_PATH)
        return self

    def logout(self):
        self.header.open_profile_menu()
        self.menu.click_menu_item("actions.logout")
        return self

    def has_search_input(self):
        return self.is_visible(AppShellLocators.SEARCH_INPUT) or self.is_visible(
            AppShellLocators.SEARCH_INPUT_FALLBACK
        )
