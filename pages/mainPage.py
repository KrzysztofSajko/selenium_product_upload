from selenium.webdriver import Chrome

from locators import MainPageLocators
from utility.actions import Actions
from utility.waiter import Waiter


class MainPage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def wait_loaded(self, timeout: int = 120) -> None:
        Waiter.clickable(self.driver, MainPageLocators.ADVANCED, timeout=timeout)

    def goto_imports(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, MainPageLocators.ADVANCED))
        Actions.click(self.driver, Waiter.clickable(self.driver, MainPageLocators.IMPORT))
