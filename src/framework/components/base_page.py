from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

from src.framework.core.config import settings

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.implicit_wait)

    def find_element(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        try:
            return wait.until(EC.presence_of_element_id_located(locator))
        except TimeoutException:
            logger.error(f"Element {locator} not found within {timeout or settings.implicit_wait} seconds")
            raise

    def click(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {e}")
            raise

    def send_keys(self, locator, text, timeout=None):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)
