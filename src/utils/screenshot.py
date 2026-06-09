from pathlib import Path


def capture_screenshot(driver, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(path)
