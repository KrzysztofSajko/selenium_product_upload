from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

from locators import ImportPageLocators
from pages.mainPage import MainPage
from utility.actions import Actions
from utility.waiter import Waiter


class ImportPage(MainPage):
    def wait_loaded(self, timeout: int = 120) -> None:
        Waiter.clickable(self.driver, ImportPageLocators.NEXT, timeout=timeout)

    def select_import_category(self, category: str) -> None:
        Select(Waiter.found(self.driver, ImportPageLocators.CATEGORY_SELECT)).select_by_visible_text(category)

    def import_file(self, path: str) -> None:
        Actions.input_text(self.driver,
                           Waiter.found(self.driver, ImportPageLocators.FILE_IMPORT),
                           path)

    def set_delete_products(self, delete: bool = True) -> None:
        if delete:
            Actions.click(self.driver, Waiter.clickable(self.driver, ImportPageLocators.OPTIONS_DELETE_YES))
        else:
            pass

    def next_step(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, ImportPageLocators.NEXT))

    def accept_alert(self) -> None:
        # Waiter.alert(self.driver)
        self.driver.switch_to.alert.accept()

    def wait_step_2(self, timeout: int = 120) -> None:
        Waiter.clickable(self.driver, ImportPageLocators.LOAD, timeout=timeout)

    def confirm_load(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, ImportPageLocators.LOAD))
