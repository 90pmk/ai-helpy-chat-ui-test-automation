from selenium.webdriver.common.by import By


class AgentBuilderLocators:
    CHAT_INPUT = (By.CSS_SELECTOR, "textarea[name='input']")
    CHAT_MODE_BUTTON = (By.CSS_SELECTOR, "button[value='chat']")
    FORM_MODE_BUTTON = (By.CSS_SELECTOR, "button[value='form']")
    AGENT_NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    TEXT_INPUTS = (By.CSS_SELECTOR, "input[type='text'], input:not([type])")
    TEXTAREAS = (By.CSS_SELECTOR, "textarea")
    MODE_TRIGGERS = (
        By.CSS_SELECTOR,
        "button, a[href], [role='button'], [role='link'], [data-testid], [class*='card'], [class*='Card']",
    )
