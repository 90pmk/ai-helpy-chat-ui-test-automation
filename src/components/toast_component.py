from src.pages.base_page import BasePage


class ToastComponent(BasePage):
    """Toast and alert message interactions."""

    def get_alert_texts(self):
        return [element.text.strip() for element in self.driver.find_elements("css selector", "div[role='alert']") if element.text.strip()]

    def has_alert_containing(self, expected_text):
        return any(expected_text in text for text in self.get_alert_texts())
