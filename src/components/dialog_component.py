from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class DialogComponent(BasePage):
    """Common dialog and modal interactions."""

    def submit_first_dialog(self):
        dialog = self.find((By.CSS_SELECTOR, "div[role='dialog']"))
        submit = dialog.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit.click()
        return self

    def cancel_first_dialog(self):
        dialog = self.find((By.CSS_SELECTOR, "div[role='dialog']"))
        buttons = dialog.find_elements(By.CSS_SELECTOR, "button")
        if not buttons:
            raise AssertionError("Dialog buttons were not found.")
        buttons[0].click()
        return self
