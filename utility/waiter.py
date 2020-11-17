from typing import Union, List

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utility.myTypes import Locator


class Waiter:
    @classmethod
    def clickable(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> WebElement:
        return WebDriverWait(element, timeout).until(EC.element_to_be_clickable(locator))

    @classmethod
    def all_found(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> List[WebElement]:
        return WebDriverWait(element, timeout).until(EC.presence_of_all_elements_located(locator))

    @classmethod
    def found(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> WebElement:
        return WebDriverWait(element, timeout).until(EC.presence_of_element_located(locator))

    @classmethod
    def visible(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> WebElement:
        return WebDriverWait(element, timeout).until(EC.visibility_of_element_located(locator))

    @classmethod
    def not_in_dom(cls, container: Union[WebElement, Chrome], element: WebElement, timeout: int = 10):
        return WebDriverWait(container, timeout).until(EC.staleness_of(element))

    @classmethod
    def enabled(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10):
        return WebDriverWait(element, timeout).until(EC.element_to_be_clickable(locator))

    @classmethod
    def alert(cls, element: Union[WebElement, Chrome], timeout: int = 10):
        WebDriverWait(element, timeout).until(EC.alert_is_present())
