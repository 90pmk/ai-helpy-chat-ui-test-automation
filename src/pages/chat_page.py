from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.constants.messages import get_message_candidates
from src.locators.chat_locators import ChatLocators
from src.pages.app_shell_page import AppShellPage


class ChatPage(AppShellPage):
    """Chat page object with navigation, search, and message helpers."""

    def open_chat_page(self):
        self.go_to_chats()
        return self

    def open_new_chat(self):
        self.js_click(ChatLocators.NEW_CHAT_LINK)
        return self

    def open_search_panel(self):
        candidates = self.find_all((By.CSS_SELECTOR, "aside [role='button'], aside a, aside button"))
        for element in candidates:
            text = (element.text or "").strip()
            if any(label in text for label in get_message_candidates("nav.search", self.locale)):
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                    element,
                )
                return self
        raise AssertionError("Search panel trigger was not found.")

    def search_chat(self, keyword):
        self.type(ChatLocators.SEARCH_PANEL_INPUT, keyword)
        return self

    def select_search_result(self, title):
        for link in self.find_all(ChatLocators.CHAT_LINKS):
            text = (link.text or "").strip()
            if title in text:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                    link,
                )
                return self
        raise AssertionError(f"Search result was not found for title={title!r}")

    def enter_message(self, text):
        self.type(ChatLocators.MESSAGE_TEXTAREA, text)
        return self

    def open_plus_menu(self):
        plus_icon = self.find(ChatLocators.PLUS_ICON)
        self.driver.execute_script(
            "const button = arguments[0].closest('button'); if (!button) { throw new Error('Plus button not found'); } button.scrollIntoView({block: 'center'}); button.click();",
            plus_icon,
        )
        self.find(ChatLocators.ADVANCED_MENU)
        return self

    def select_plus_menu_option(self, key):
        self.open_plus_menu()
        labels = get_message_candidates(key, self.locale)
        items = self.find_all((By.CSS_SELECTOR, "ul[role='menu'] li[role='menuitem']"))
        for item in items:
            text = (item.text or "").strip()
            if any(label in text for label in labels):
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                    item,
                )
                return self
        raise AssertionError(f"Advanced menu option was not found for key={key!r}")

    def select_file_upload(self):
        return self.select_plus_menu_option("actions.upload_file")

    def select_image_generation(self):
        return self.select_plus_menu_option("actions.image_generate")

    def select_ppt_generation(self):
        return self.select_plus_menu_option("actions.ppt_generate")

    def select_web_search(self):
        return self.select_plus_menu_option("actions.web_search")

    def has_selected_mode_chip(self, key):
        labels = get_message_candidates(key, self.locale)
        try:
            self.wait_for(lambda driver: self._selected_mode_chip_matches(labels), timeout=5)
            return True
        except TimeoutException:
            return False

    def _selected_mode_chip_matches(self, labels):
        icons = self.find_all(ChatLocators.SELECTED_MODE_CLOSE_ICONS)
        if not icons:
            return False

        for icon in icons:
            text_candidates = []
            for script in (
                "return arguments[0].closest('button');",
                "return arguments[0].parentElement;",
                "return arguments[0].closest('div');",
            ):
                container = self.driver.execute_script(script, icon)
                if container:
                    text_candidates.append((container.text or "").strip())

            aria_label = icon.get_attribute("aria-label") or ""
            text_candidates.append(aria_label.strip())

            combined = " ".join(value for value in text_candidates if value).strip()
            if any(label in combined for label in labels):
                return True

        visible_text = ""
        try:
            visible_text = self.visible_text((By.CSS_SELECTOR, "form, main"))
        except Exception:
            visible_text = self.driver.find_element(By.TAG_NAME, "body").text

        return any(label in visible_text for label in labels)

    def send_message(self):
        self.js_click(ChatLocators.SEND_BUTTON)
        return self

    def send_message_with_text(self, text):
        return self.enter_message(text).send_message()

    def get_chat_titles(self):
        return [item.text.strip() for item in self.find_all(ChatLocators.CHAT_LINKS) if item.text.strip()]

    def has_chat_title(self, title):
        return any(title in text for text in self.get_chat_titles())

    def clear_search_input(self):
        search_input = self.find(ChatLocators.SEARCH_PANEL_INPUT)
        search_input.click()
        search_input.send_keys(Keys.CONTROL, "a")
        search_input.send_keys(Keys.DELETE)
        return self
