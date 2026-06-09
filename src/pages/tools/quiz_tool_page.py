from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.components.dialog_component import DialogComponent
from src.pages.tools.tools_home_page import ToolsHomePage


class QuizToolPage(ToolsHomePage):
    """Quiz generation tool workflows."""

    DROPDOWN_LABELS = {
        "quiz_configs.0.option_type": {
            "0": "\uac1d\uad00\uc2dd (\ub2e8\uc77c \uc120\ud0dd)",
            "1": "\uac1d\uad00\uc2dd (\ubcf5\uc218 \uc120\ud0dd)",
            "3": "\uc8fc\uad00\uc2dd",
        },
        "quiz_configs.0.difficulty": {
            "Level1": "\uc0c1",
            "Level2": "\uc911",
            "Level3": "\ud558",
        },
    }

    def _get_select_trigger(self, hidden_input):
        trigger = self.driver.execute_script(
            """
            const input = arguments[0];
            return input.closest('.MuiInputBase-root')?.querySelector('[role="combobox"]')
                || input.previousElementSibling;
            """,
            hidden_input,
        )
        if not trigger:
            raise AssertionError("Select trigger not found.")
        return trigger

    def _label_candidates(self, input_name, value):
        candidates = [value]
        label = self.DROPDOWN_LABELS.get(input_name, {}).get(value)
        if label:
            candidates.insert(0, label)
        return [candidate for candidate in candidates if candidate]

    def get_dropdown_display_text(self, input_name):
        input_locator = (By.CSS_SELECTOR, f"input[name='{input_name}']")
        hidden_input = self.find(input_locator)
        trigger = self._get_select_trigger(hidden_input)
        return (trigger.text or "").strip()

    def select_dropdown_value(self, input_name, value):
        input_locator = (By.CSS_SELECTOR, f"input[name='{input_name}']")
        hidden_input = self.find(input_locator)
        trigger = self._get_select_trigger(hidden_input)
        label_candidates = self._label_candidates(input_name, value)
        current_text = (trigger.text or "").strip()
        if any(candidate == current_text for candidate in label_candidates):
            return self

        self.driver.execute_script(
            """
            const trigger = arguments[0];
            trigger.scrollIntoView({block: 'center'});
            trigger.click();
            """,
            trigger,
        )
        self.wait_for(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']")), timeout=5)
        items = self.find_all((By.CSS_SELECTOR, "ul[role='listbox'] li"))
        for item in items:
            item_value = (item.get_attribute("data-value") or "").strip()
            item_text = (item.text or "").strip()
            if item_value == value or any(candidate == item_text for candidate in label_candidates):
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                    item,
                )
                return self
        raise AssertionError(f"Dropdown option was not found for input={input_name!r}, value={value!r}")

    def input_content(self, text):
        self.type((By.NAME, "content"), text)
        return self

    def start_generation(self, form_id="tool-factory-create_quiz_from_context"):
        self.js_click((By.CSS_SELECTOR, f"button[form='{form_id}']"))
        if self.exists((By.CSS_SELECTOR, "div[role='dialog']")):
            DialogComponent(self.driver, timeout=self.timeout, locale=self.locale).submit_first_dialog()
        return self

    def stop_generation(self):
        self.click((By.CSS_SELECTOR, "[data-testid='stopIcon']"))
        return self

    def has_success_icon(self):
        return self.exists((By.CSS_SELECTOR, "[data-testid='circle-checkIcon']"))
