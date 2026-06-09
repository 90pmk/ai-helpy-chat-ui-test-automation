from selenium.webdriver.common.by import By

from src.constants.messages import get_message_candidates
from src.locators.app_shell_locators import AppShellLocators
from src.pages.base_page import BasePage


class MenuComponent(BasePage):
    """Dropdown and contextual menu interactions."""

    def open_header_profile_menu(self):
        buttons = self.find_all(AppShellLocators.HEADER_BUTTONS)
        if not buttons:
            raise AssertionError("Header buttons were not found.")
        profile_button = buttons[-1]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
            profile_button,
        )
        self.find(AppShellLocators.MENU_CONTAINER)
        return self

    def click_menu_item(self, key):
        candidates = get_message_candidates(key, self.locale)
        items = self.find_all(AppShellLocators.MENU_ITEMS)

        for candidate in candidates:
            for item in items:
                text = (item.text or "").strip()
                if candidate in text:
                    self.driver.execute_script("arguments[0].click();", item)
                    return self

        raise AssertionError(f"Could not find menu item for key={key!r}")
