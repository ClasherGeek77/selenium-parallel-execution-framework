import pytest
import logging
import allure
from src.framework.core.factory import DriverFactory
from src.framework.core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver(request):
    """
    Creates a new thread-safe Selenium WebDriver instance per test function.
    """
    driver = DriverFactory.create_driver()
    driver.implicitly_wait(settings.implicit_wait)
    
    yield driver
    
    # Optional: Attach browser logs on teardown
    try:
        browser_logs = driver.get_log('browser')
        if browser_logs:
            allure.attach(str(browser_logs), name="Browser Logs", attachment_type=allure.attachment_type.TEXT)
    except:
        pass

    logger.info("Quitting driver")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        try:
            # Check if 'driver' fixture is in the test item
            if 'driver' in item.fixturenames:
                driver = item.funcargs['driver']
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                logger.error(f"Captured screenshot for failing test: {item.name}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
