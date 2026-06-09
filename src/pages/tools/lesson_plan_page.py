from src.pages.base_page import BasePage


class LessonPlanPage(BasePage):
    """Lesson plan generation workflows."""

    CONTENT_TIMEOUT = 20

    CONTENT_INPUTS = (
        ("css selector", "textarea[name='content']"),
        ("css selector", "input[name='content']"),
        ("css selector", "[contenteditable='true']"),
        ("css selector", "[role='textbox']"),
        ("css selector", "textarea[placeholder]"),
        ("css selector", "input[placeholder]"),
        ("css selector", "textarea"),
    )

    def input_content(self, text):
        element = self.find_first_editable(self.CONTENT_INPUTS, timeout=self.CONTENT_TIMEOUT)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self._clear_input_element(element)
        element.send_keys(text)
        return self

    def get_content_value(self):
        return self.value_of_first_editable(self.CONTENT_INPUTS)
        return self
