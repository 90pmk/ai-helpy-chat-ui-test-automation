from selenium.webdriver.common.by import By


class AppShellLocators:
    CHATS_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat'], a[href='/ai-helpy-chat/chats']")
    TOOLS_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/tools']")
    AGENTS_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/agents']")
    HEADER_BUTTONS = (By.CSS_SELECTOR, "header button, [role='banner'] button")
    MENU_CONTAINER = (By.CSS_SELECTOR, "[role='menu']")
    MENU_ITEMS = (By.CSS_SELECTOR, "[role='menu'] [role='button'], [role='menu'] button, [role='menu'] a")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search'], input[placeholder*='검색']")
    SEARCH_INPUT_FALLBACK = (By.CSS_SELECTOR, "input[type='text']")
