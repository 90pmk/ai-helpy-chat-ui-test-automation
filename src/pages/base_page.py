from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.constants.timeouts import DEFAULT_TIMEOUT
from src.utils.config import get_locale


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT, locale=None):
        self.driver = driver
        self.timeout = timeout
        self.locale = locale or get_locale()

    def open(self, url):
        self.driver.get(url)
        return self

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for(self, condition, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(condition)

    def click(self, locator):
        self.wait_for(EC.element_to_be_clickable(locator)).click()
        return self

    def js_click(self, locator):
        element = self.wait_for(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
            element,
        )
        return self

    def type(self, locator, value, clear_first=True):
        element = self.find(locator)
        if clear_first:
            self._clear_input_element(element)
        element.send_keys(value)
        return self

    def _clear_input_element(self, element):
        element.click()
        element.clear()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        # Some MUI/browser-autofill combinations keep stale values unless the DOM value is reset.
        self.driver.execute_script(
            """
            const el = arguments[0];
            el.value = '';
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            element,
        )
        return self

    def _is_editable_input(self, element):
        try:
            if not element.is_displayed() or not element.is_enabled():
                return False
        except Exception:
            return False

        input_type = (element.get_attribute("type") or "").strip().lower()
        if input_type == "hidden":
            return False
        if (element.get_attribute("readonly") or "").lower() in {"true", "readonly"}:
            return False
        if (element.get_attribute("aria-hidden") or "").lower() == "true":
            return False
        return True

    def _find_first_editable_now(self, locators):
        for locator in locators:
            for element in self.find_all(locator):
                if self._is_editable_input(element):
                    return element
        return None

    def find_first_editable(self, locators, timeout=None):
        timeout = timeout or self.timeout

        def _predicate(_driver):
            return self._find_first_editable_now(locators) or False

        try:
            return self.wait_for(_predicate, timeout=timeout)
        except TimeoutException as exc:
            raise TimeoutException(f"No editable element found for locators: {locators!r}") from exc

    def type_first_editable(self, locators, value, clear_first=True):
        element = self.find_first_editable(locators)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        if clear_first:
            self._clear_input_element(element)
        element.send_keys(value)
        return self

    def value_of_first_editable(self, locators):
        element = self.find_first_editable(locators)
        value = element.get_attribute("value")
        if value not in (None, ""):
            return value
        text = (element.text or "").strip()
        if text:
            return text
        return (
            self.driver.execute_script(
                "return (arguments[0].textContent || arguments[0].innerText || '').trim();",
                element,
            )
            or ""
        )

    def text_of(self, locator):
        return self.find(locator).text

    def attribute_of(self, locator, attribute_name):
        return self.find(locator).get_attribute(attribute_name)

    def exists(self, locator):
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator):
        try:
            return self.wait_for(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def visible_text(self, locator):
        return self.wait_for(EC.visibility_of_element_located(locator)).text

    def wait_for_url_contains(self, text, timeout=None):
        self.wait_for(EC.url_contains(text), timeout=timeout)
        return self

    def current_url_contains(self, text):
        return text in self.driver.current_url

    def first_visible(self, locators):
        for locator in locators:
            try:
                return self.wait_for(EC.visibility_of_element_located(locator), timeout=3)
            except TimeoutException:
                continue
        raise TimeoutException(f"No visible element found for locators: {locators!r}")

    def maybe_find_by_id(self, element_id):
        try:
            return self.driver.find_element("id", element_id)
        except NoSuchElementException:
            return None
