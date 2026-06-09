from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for(driver, condition, timeout=10):
    return WebDriverWait(driver, timeout).until(condition)


def wait_for_visible(driver, locator, timeout=10):
    return wait_for(driver, EC.visibility_of_element_located(locator), timeout)
