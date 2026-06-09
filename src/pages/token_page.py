from src.locators.token_locators import TokenLocators
from src.pages.app_shell_page import AppShellPage


class TokenPage(AppShellPage):
    """Token status and token-related checks."""

    def get_alert_texts(self):
        return [item.text.strip() for item in self.find_all(TokenLocators.ALERTS) if item.text.strip()]

    def get_page_text(self):
        return self.text_of(TokenLocators.BODY)
