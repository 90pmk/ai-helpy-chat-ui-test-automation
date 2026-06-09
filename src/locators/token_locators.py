from selenium.webdriver.common.by import By


class TokenLocators:
    ALERTS = (By.CSS_SELECTOR, "div[role='alert']")
    BODY = (By.TAG_NAME, "body")
