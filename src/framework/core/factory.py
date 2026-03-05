import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from src.framework.core.config import settings, Environment, BrowserType

logger = logging.getLogger(__name__)

class DriverFactory:
    @staticmethod
    def create_driver():
        logger.info(f"Creating driver for environment: {settings.env}, browser: {settings.browser}")
        
        if settings.env == Environment.LOCAL:
            return DriverFactory._create_local_driver()
        elif settings.env == Environment.GRID:
            return DriverFactory._create_remote_driver()
        else:
            raise ValueError(f"Unsupported environment: {settings.env}")

    @staticmethod
    def _create_local_driver():
        if settings.browser == BrowserType.CHROME:
            options = ChromeOptions()
            if settings.headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(options=options)
        
        elif settings.browser == BrowserType.FIREFOX:
            options = FirefoxOptions()
            if settings.headless:
                options.add_argument("-headless")
            return webdriver.Firefox(options=options)
        
        elif settings.browser == BrowserType.EDGE:
            options = EdgeOptions()
            if settings.headless:
                options.add_argument("--headless")
            return webdriver.Edge(options=options)
        
        raise ValueError(f"Unsupported local browser: {settings.browser}")

    @staticmethod
    def _create_remote_driver():
        if settings.browser == BrowserType.CHROME:
            options = ChromeOptions()
        elif settings.browser == BrowserType.FIREFOX:
            options = FirefoxOptions()
        elif settings.browser == BrowserType.EDGE:
            options = EdgeOptions()
        else:
            raise ValueError(f"Unsupported remote browser: {settings.browser}")
            
        if settings.headless:
            options.add_argument("--headless")
            
        return webdriver.Remote(
            command_executor=settings.grid_url,
            options=options
        )
