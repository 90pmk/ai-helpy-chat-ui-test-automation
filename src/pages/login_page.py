from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.constants.urls import BASE_URL
from src.locators.login_locators import LoginLocators
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def open_login_page(self):
        self.open(BASE_URL)
        return self

    def enter_email(self, email):
        self.type(LoginLocators.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        self.type(LoginLocators.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)
        return self

    def login(self, email, password):
        return self.enter_email(email).enter_password(password).click_login()

    def toggle_password_visibility(self):
        password_input = self.find(LoginLocators.PASSWORD_INPUT)
        self.driver.execute_script(
            """
            const input = arguments[0];
            const root = input.closest('div');
            const button = root ? root.querySelector('button') : null;
            if (!button) {
                throw new Error('Password toggle button not found');
            }
            button.click();
            """,
            password_input,
        )
        return self

    def click_forgot_password(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)
        return self

    def click_signup(self):
        self.click(LoginLocators.SIGNUP_LINK)
        return self

    def get_error_message(self):
        return self.text_of(LoginLocators.ERROR_MESSAGE)

    def try_get_error_message(self):
        if self.is_visible(LoginLocators.ERROR_MESSAGE):
            return self.visible_text(LoginLocators.ERROR_MESSAGE).strip()
        return ""

    def get_field_error_message(self, field_locator):
        def _helper_text(driver):
            field = self.find(field_locator)
            helper_id = field.get_attribute("aria-describedby")
            if not helper_id:
                return False
            helper = driver.find_element(By.ID, helper_id)
            text = helper.text.strip()
            return text or False

        return WebDriverWait(self.driver, self.timeout).until(_helper_text)

    def get_email_error_message(self):
        return self.get_field_error_message(LoginLocators.EMAIL_INPUT)

    def get_password_error_message(self):
        return self.get_field_error_message(LoginLocators.PASSWORD_INPUT)

    def get_password_input_type(self):
        return self.find(LoginLocators.PASSWORD_INPUT).get_attribute("type")

    def get_entered_email(self):
        return self.find(LoginLocators.EMAIL_INPUT).get_attribute("value")

    def get_entered_password(self):
        return self.find(LoginLocators.PASSWORD_INPUT).get_attribute("value")

    def is_email_input_visible(self):
        return self.find(LoginLocators.EMAIL_INPUT).is_displayed()

    def is_password_input_visible(self):
        return self.find(LoginLocators.PASSWORD_INPUT).is_displayed()

    def is_login_button_visible(self):
        return self.find(LoginLocators.LOGIN_BUTTON).is_displayed()

    def is_forgot_password_link_visible(self):
        return self.find(LoginLocators.FORGOT_PASSWORD_LINK).is_displayed()

    def is_signup_link_visible(self):
        return self.find(LoginLocators.SIGNUP_LINK).is_displayed()

    def wait_for_url_contains(self, text, timeout=None):
        WebDriverWait(self.driver, timeout or self.timeout).until(EC.url_contains(text))
        return self
