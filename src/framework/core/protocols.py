from typing import Protocol, runtime_checkable
from selenium.webdriver.common.by import By

@runtime_checkable
class Page(Protocol):
    def open(self) -> None:
        ...

    def get_title(self) -> str:
        ...

@runtime_checkable
class Interactable(Protocol):
    def click(self, locator: tuple[By, str], timeout: int | None = None) -> None:
        ...

    def send_keys(self, locator: tuple[By, str], text: str, timeout: int | None = None) -> None:
        ...
        
    def find_element(self, locator: tuple[By, str], timeout: int | None = None):
        ...
