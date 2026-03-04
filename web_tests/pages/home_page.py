from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.julo.co.id/"

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
