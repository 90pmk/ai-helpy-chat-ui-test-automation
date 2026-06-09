from src.pages.base_page import BasePage


class BehaviorPage(BasePage):
    """Behavior-related tool workflows."""

    PROMPT_TIMEOUT = 20

    PROMPT_INPUTS = (
        ("css selector", "textarea[name='content']"),
        ("css selector", "input[name='content']"),
        ("css selector", "[contenteditable='true']"),
        ("css selector", "[role='textbox']"),
        ("css selector", "textarea[placeholder]"),
        ("css selector", "input[placeholder]"),
        ("css selector", "textarea"),
    )

    def input_prompt(self, text):
        element = self.find_first_editable(self.PROMPT_INPUTS, timeout=self.PROMPT_TIMEOUT)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self._clear_input_element(element)
        element.send_keys(text)
        return self

    def get_prompt_value(self):
        return self.value_of_first_editable(self.PROMPT_INPUTS)
        return self
