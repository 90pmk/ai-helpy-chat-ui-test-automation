from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.constants.messages import get_message_candidates
from src.pages.base_page import BasePage


class DetailSpecialPage(BasePage):
    """Detailed student remarks tool workflows."""

    SCHOOL_LEVEL_INPUT = (By.CSS_SELECTOR, "input[name='school_level']")
    GRADE_INPUT = (By.CSS_SELECTOR, "input[name='grade']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[role='combobox']")
    UNIT_INPUT = (By.CSS_SELECTOR, "input[name='unit']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button[type='submit'][form='student_evaluation']")
    STUDENT_SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='학생 이름'], input[placeholder*='Search student name']")
    ACTIVE_TAB = (By.CSS_SELECTOR, "button[role='tab'][aria-selected='true']")

    def _click_mui_select_from_hidden_input(self, locator):
        hidden_input = self.find(locator)
        trigger = self.driver.execute_script(
            """
            const input = arguments[0];
            return input.closest('.MuiInputBase-root')?.querySelector('[role="combobox"]')
                || input.previousElementSibling;
            """,
            hidden_input,
        )
        if not trigger:
            raise AssertionError("Select trigger was not found.")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", trigger)

        for action in (
            lambda element: element.click(),
            lambda element: self.driver.execute_script("arguments[0].click();", element),
            lambda element: element.send_keys(Keys.SPACE),
            lambda element: element.send_keys(Keys.ENTER),
        ):
            action(trigger)
            try:
                self.find((By.CSS_SELECTOR, "ul[role='listbox']"))
                return self
            except TimeoutException:
                continue
        raise AssertionError("Select listbox did not open.")
        return self

    def _select_visible_option(self, candidates):
        self.find((By.CSS_SELECTOR, "ul[role='listbox']"))
        options = self.find_all((By.CSS_SELECTOR, "ul[role='listbox'] li[role='option']"))
        normalized_candidates = [candidate.strip() for candidate in candidates if candidate and candidate.strip()]
        for option in options:
            option_value = (option.get_attribute("data-value") or "").strip()
            option_text = (option.text or "").strip()
            if option_value in normalized_candidates or option_text in normalized_candidates:
                self.driver.execute_script("arguments[0].click();", option)
                return self
        raise AssertionError(f"Select option was not found for candidates={normalized_candidates!r}")

    def select_school_level(self, level_text):
        self._click_mui_select_from_hidden_input(self.SCHOOL_LEVEL_INPUT)
        return self._select_visible_option([level_text])

    def select_school_level_by_key(self, key):
        self._click_mui_select_from_hidden_input(self.SCHOOL_LEVEL_INPUT)
        return self._select_visible_option(get_message_candidates(key, self.locale))

    def select_grade(self, grade_text):
        self._click_mui_select_from_hidden_input(self.GRADE_INPUT)
        return self._select_visible_option([grade_text])

    def input_subject(self, subject):
        inputs = self.find_all(self.SUBJECT_INPUT)
        target = next((item for item in inputs if item.get_attribute("name") is None and item.get_attribute("type") == "text"), None)
        if target is None:
            raise AssertionError("Subject input was not found.")
        target.click()
        target.clear()
        target.send_keys(subject)
        return self

    def input_unit(self, unit):
        self.type(self.UNIT_INPUT, unit)
        return self

    def go_next(self):
        self.js_click(self.NEXT_BUTTON)
        return self

    def input_student_keyword(self, keyword):
        candidates = self.find_all(self.STUDENT_SEARCH_INPUT)
        placeholder_candidates = get_message_candidates("fields.student_name_search", self.locale)
        target = next(
            (
                item
                for item in candidates
                if any(label in (item.get_attribute("placeholder") or "") for label in placeholder_candidates)
            ),
            None,
        )
        if target is None:
            raise AssertionError("Student search input was not found.")
        target.click()
        target.clear()
        target.send_keys(keyword)
        return self

    def get_active_tab_text(self):
        return (self.text_of(self.ACTIVE_TAB) or "").strip()

    def is_class_info_step_active(self):
        active_tab_text = self.get_active_tab_text()
        return "수업 정보 입력" in active_tab_text or "Class" in active_tab_text

    def is_student_info_step_active(self):
        active_tab_text = self.get_active_tab_text()
        return "학생 정보 입력 및 생성" in active_tab_text or "Student" in active_tab_text
