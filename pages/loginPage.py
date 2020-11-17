from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from locators import LoginPageLocators
from utility.actions import Actions
from utility.myTypes import Locator
from utility.waiter import Waiter


class LoginPage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def __enter_to_input(self, locator: Locator, text: str) -> None:
        Actions.input_text(self.driver, Waiter.found(self.driver, locator), text)

    def enter_email(self, email: str) -> None:
        self.__enter_to_input(LoginPageLocators.EMAIL, email)

    def enter_password(self, password: str) -> None:
        self.__enter_to_input(LoginPageLocators.PASSWORD, password)

    def submit(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, LoginPageLocators.SUBMIT))