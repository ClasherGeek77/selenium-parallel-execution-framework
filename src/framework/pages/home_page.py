from src.framework.components.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.julo.co.id/"

    def open(self):
        super().open(self.url)
