from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from src.constants.messages import get_message_candidates
from src.constants.urls import AGENTS_BUILDER_PATH, AGENTS_MINE_PATH, AGENTS_PATH, BASE_URL
from src.locators.agents_locators import AgentsLocators
from src.pages.app_shell_page import AppShellPage


class AgentsPage(AppShellPage):
    """Agents list and agent entry navigation."""

    def open_agents_page(self):
        self.go_to_agents()
        self.wait_for_url_contains(AGENTS_PATH)
        return self

    def open_my_agents_page(self):
        self.open_agents_page()
        self.js_click(AgentsLocators.MY_AGENTS_LINK)
        self.wait_for_url_contains(AGENTS_MINE_PATH)
        return self

    def open_builder(self):
        self.open_agents_page()
        builder_href = self._resolve_builder_href()
        if builder_href:
            self.open(builder_href)
        else:
            self.open(f"{BASE_URL}{AGENTS_BUILDER_PATH}")
        self.wait_for_url_contains(AGENTS_BUILDER_PATH, timeout=20)
        return self

    def get_agent_links(self):
        return self.find_all(AgentsLocators.AGENT_CARD_LINKS)

    def _resolve_builder_href(self):
        for locator in (AgentsLocators.BUILDER_LINK, AgentsLocators.BUILDER_LINK_FALLBACK):
            if self.exists(locator):
                href = self.find(locator).get_attribute("href")
                if href:
                    return href

        labels = get_message_candidates("actions.create", self.locale)
        for element in self.find_all((By.CSS_SELECTOR, "a[href], button, [role='button']")):
            text = (element.text or "").strip()
            href = element.get_attribute("href") or ""
            if AGENTS_BUILDER_PATH in href:
                return href
            if any(label in text for label in labels):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                try:
                    self.driver.execute_script("arguments[0].click();", element)
                    self.wait_for_url_contains(AGENTS_BUILDER_PATH, timeout=5)
                    return self.driver.current_url
                except TimeoutException:
                    continue

        return None
