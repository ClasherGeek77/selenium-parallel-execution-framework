import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """
    Creates a new thread-safe Selenium WebDriver instance per test function.
    This enables true parallel execution when running pytest -n.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Ideally connect to Grid, but defaulting to local Chrome for CI compatibility
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
