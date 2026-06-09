from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from src.constants.urls import BASE_URL, TOOLS_PATH
from src.pages.app_shell_page import AppShellPage


class ToolsHomePage(AppShellPage):
    """Tools entry page and tool navigation."""

    TOOL_IDENTIFIERS = {
        "tools.quiz": "create_quiz_from_context",
        "tools.lesson_plan": "syllabus_generation",
        "tools.student_record": "student_evaluation",
        "tools.behavior": "student_record_generation",
        "tools.ppt": "create_pptx",
        "tools.deep_investigation": "do_deep_research",
    }

    def open_tools_page(self):
        self.go_to_tools()
        self.wait_for_url_contains(TOOLS_PATH)
        return self

    def open_tool_by_path_fragment(self, path_fragment):
        locator = (By.CSS_SELECTOR, f"a[href*='{path_fragment}']")
        self.js_click(locator)
        return self

    def open_tool_by_label(self, key):
        self.open_tools_page()
        tool_ident = self.TOOL_IDENTIFIERS.get(key)
        if tool_ident:
            icon_locator = (By.CSS_SELECTOR, f"[data-ai-tool-ident='{tool_ident}']")
            icon = self.find(icon_locator)
            current_url = self.driver.current_url
            link_href = self.driver.execute_script(
                """
                const link = arguments[0].closest('a');
                if (!link) {
                    throw new Error('Tool link not found');
                }
                link.scrollIntoView({block: 'center'});
                return link.href;
                """,
                icon,
            )
            self.driver.execute_script(
                """
                const link = arguments[0].closest('a');
                if (!link) {
                    throw new Error('Tool link not found');
                }
                link.click();
                """,
                icon,
            )
            try:
                self.wait_for(
                    lambda driver: driver.current_url != current_url and f"{TOOLS_PATH}/" in driver.current_url,
                    timeout=5,
                )
            except TimeoutException:
                if not link_href:
                    raise
                if link_href.startswith("/"):
                    link_href = f"{BASE_URL.rstrip('/')}{link_href}"
                self.open(link_href)
                self.wait_for(
                    lambda driver: f"{TOOLS_PATH}/" in driver.current_url,
                    timeout=10,
                )
            return self
        raise AssertionError(f"Tool link was not found for key={key!r}")

    def open_quiz_tool(self):
        return self.open_tool_by_label("tools.quiz")

    def open_lesson_plan_tool(self):
        return self.open_tool_by_label("tools.lesson_plan")

    def open_student_record_tool(self):
        return self.open_tool_by_label("tools.student_record")

    def open_student_info_tool(self):
        return self.open_tool_by_label("tools.student_info")

    def open_behavior_tool(self):
        return self.open_tool_by_label("tools.behavior")

    def open_ppt_tool(self):
        return self.open_tool_by_label("tools.ppt")

    def open_deep_investigation_tool(self):
        return self.open_tool_by_label("tools.deep_investigation")
