from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.NAME, "loginId")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.MuiFormHelperText-root.Mui-error")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href*='recover/password']")
    SIGNUP_LINK = (By.CSS_SELECTOR, "a[href*='signup']")
