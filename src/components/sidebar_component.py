from src.locators.app_shell_locators import AppShellLocators
from src.pages.base_page import BasePage


class SidebarComponent(BasePage):
    """Sidebar navigation shared across the application shell."""

    def go_to_chats(self):
        self.js_click(AppShellLocators.CHATS_LINK)
        return self

    def go_to_tools(self):
        self.js_click(AppShellLocators.TOOLS_LINK)
        return self

    def go_to_agents(self):
        self.js_click(AppShellLocators.AGENTS_LINK)
        return self
