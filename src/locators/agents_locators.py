from selenium.webdriver.common.by import By


class AgentsLocators:
    AGENTS_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/agents']")
    MY_AGENTS_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/agents/mine']")
    BUILDER_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/agents/builder']")
    BUILDER_LINK_FALLBACK = (By.CSS_SELECTOR, "a[href*='/ai-helpy-chat/agents/builder'], a[href*='/agents/builder']")
    AGENT_CARD_LINKS = (By.CSS_SELECTOR, "a[href*='/ai-helpy-chat/agents/']")
