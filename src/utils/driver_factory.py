from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.utils.config import get_env


def _env_is_truthy(key, default=False):
    value = get_env(key)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}


def create_chrome_driver():
    options = webdriver.ChromeOptions()
    is_headless = _env_is_truthy("HEADLESS", default=_env_is_truthy("CI"))
    use_incognito = _env_is_truthy("INCOGNITO", default=True)

    if is_headless:
        options.add_argument("--headless=new")

    if use_incognito:
        options.add_argument("--incognito")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(60)
    return driver
