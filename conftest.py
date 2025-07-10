import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# -------------------------------
# Fixture: WebDriver Setup/Teardown
# -------------------------------

@pytest.fixture
def driver():
    path = ChromeDriverManager().install()
    print(f"Resolved ChromeDriver path: {path}")  
    if not path.endswith("chromedriver"):
        raise RuntimeError(f"Unexpected driver path: {path}")
    service = Service(path)
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")  
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# -------------------------------
# Hook: Screenshot on Test Failure
# -------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(file_name)
            print(f"\nScreenshot saved to: {file_name}")