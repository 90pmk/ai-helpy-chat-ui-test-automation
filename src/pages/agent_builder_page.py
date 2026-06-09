from selenium.webdriver.common.by import By

from src.constants.messages import get_message_candidates
from src.locators.agent_builder_locators import AgentBuilderLocators
from src.pages.agents_page import AgentsPage


class AgentBuilderPage(AgentsPage):
    """Agent builder flows for chat mode and form mode creation."""

    MODE_INDEX_BY_KEY = {
        "actions.chat_builder": 0,
        "actions.form_builder": 1,
    }

    def _click_first_button_matching(self, labels):
        self.wait_for(lambda _driver: self._visible_mode_candidates() or False, timeout=15)
        candidates = self.find_all(AgentBuilderLocators.MODE_TRIGGERS)
        for element in candidates:
            attrs = self._mode_candidate_summary(element)
            if any(label in attrs for label in labels):
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                    element,
                )
                return self
        raise AssertionError(f"Builder mode trigger was not found for labels={labels!r}.")

    def choose_chat_builder_mode(self):
        if self.exists(AgentBuilderLocators.CHAT_MODE_BUTTON):
            self.js_click(AgentBuilderLocators.CHAT_MODE_BUTTON)
            self.wait_for(
                lambda _driver: self.is_chat_builder_mode_selected() and self.has_chat_builder_prompt(),
                timeout=10,
            )
            return self
        return self._choose_builder_mode("actions.chat_builder")

    def choose_form_builder_mode(self):
        if self.exists(AgentBuilderLocators.FORM_MODE_BUTTON):
            self.js_click(AgentBuilderLocators.FORM_MODE_BUTTON)
            self.wait_for(
                lambda _driver: self.is_form_builder_mode_selected() and self.has_form_builder_fields(),
                timeout=10,
            )
            return self
        return self._choose_builder_mode("actions.form_builder")

    def _choose_builder_mode(self, key):
        labels = get_message_candidates(key, self.locale)
        try:
            return self._click_first_button_matching(labels)
        except AssertionError:
            fallback = self._visible_mode_candidates()
            index = self.MODE_INDEX_BY_KEY[key]
            if len(fallback) > index:
                element = fallback[index]
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                    element,
                )
                return self
            raise

    def _mode_candidate_summary(self, element):
        return " ".join(
            filter(
                None,
                [
                    (element.text or "").strip(),
                    element.get_attribute("aria-label"),
                    element.get_attribute("title"),
                    element.get_attribute("href"),
                    element.get_attribute("data-testid"),
                ],
            )
        ).strip()

    def _visible_mode_candidates(self):
        visible = []
        for element in self.find_all(AgentBuilderLocators.MODE_TRIGGERS):
            try:
                if not element.is_displayed() or not element.is_enabled():
                    continue
            except Exception:
                continue

            summary = self._mode_candidate_summary(element)
            if summary:
                visible.append(element)
        return visible

    def fill_text_field(self, labels, value, multiline=False):
        candidates = self.find_all(AgentBuilderLocators.TEXTAREAS if multiline else AgentBuilderLocators.TEXT_INPUTS)
        normalized_labels = [label.strip() for label in labels]

        for element in candidates:
            attrs = " ".join(
                filter(
                    None,
                    [
                        element.get_attribute("name"),
                        element.get_attribute("placeholder"),
                        element.get_attribute("aria-label"),
                        element.get_attribute("id"),
                    ],
                )
            )
            if any(label in attrs for label in normalized_labels):
                locator = (By.ID, element.get_attribute("id")) if element.get_attribute("id") else None
                if locator:
                    self.type(locator, value)
                else:
                    element.click()
                    element.clear()
                    element.send_keys(value)
                return self

        fallback_locator = AgentBuilderLocators.TEXTAREAS if multiline else AgentBuilderLocators.TEXT_INPUTS
        if self.exists(fallback_locator):
            self.type(fallback_locator, value)
            return self

        raise AssertionError(f"Input field was not found for labels={labels!r}")

    def has_chat_builder_prompt(self):
        return self.exists(AgentBuilderLocators.CHAT_INPUT)

    def has_form_builder_fields(self):
        return self.exists(AgentBuilderLocators.AGENT_NAME_INPUT) or bool(
            self.find_all(AgentBuilderLocators.TEXT_INPUTS) or self.find_all(AgentBuilderLocators.TEXTAREAS)
        )

    def is_chat_builder_mode_selected(self):
        return self.attribute_of(AgentBuilderLocators.CHAT_MODE_BUTTON, "aria-pressed") == "true"

    def is_form_builder_mode_selected(self):
        return self.attribute_of(AgentBuilderLocators.FORM_MODE_BUTTON, "aria-pressed") == "true"
