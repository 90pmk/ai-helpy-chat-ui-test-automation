from selenium.webdriver.common.by import By


class ChatLocators:
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "textarea[name='input']")
    SEARCH_PANEL_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Search'], input[placeholder*='검색']")
    SEARCH_PANEL_CLOSE_ICON = (By.CSS_SELECTOR, "button svg[data-testid='xmarkIcon']")
    CHAT_LINKS = (By.CSS_SELECTOR, "a[href*='/ai-helpy-chat/chats/']")
    SEND_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Send'], button[aria-label='보내기']")
    NEW_CHAT_LINK = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat']")
    PLUS_ICON = (By.CSS_SELECTOR, "[data-testid*='plusIcon']")
    ADVANCED_MENU = (By.CSS_SELECTOR, "ul[role='menu']")
    SELECTED_MODE_CLOSE_ICONS = (By.CSS_SELECTOR, "[data-testid*='CloseIcon']")
    MESSAGE_ACTION_BUTTONS = (By.CSS_SELECTOR, "button")
