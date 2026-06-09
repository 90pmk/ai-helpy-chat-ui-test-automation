from selenium.webdriver.common.by import By


class ToolsHomeLocators:
    TOOLS_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/tools']")
    TOOL_LINKS = (By.CSS_SELECTOR, "a[href*='/ai-helpy-chat/tools/']")
