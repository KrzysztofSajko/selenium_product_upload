from selenium.webdriver import Chrome

from pages.pageSet import PageSet


class Executor:
    def __init__(self, driver: Chrome, pages: PageSet):
        self.driver: Chrome = driver
        self.pages: PageSet = pages

    def login(self, email: str, password: str) -> None:
        self.pages.https.wait_loaded()
        self.pages.https.skip()
        self.pages.login.enter_email(email)
        self.pages.login.enter_password(password)
        self.pages.login.submit()
        self.pages.main.wait_loaded()

    def import_products(self, path: str, category: str) -> None:
        self.pages.main.goto_imports()
        self.pages.imp.wait_loaded()
        self.pages.imp.select_import_category(category)
        self.pages.imp.import_file(path)
        self.pages.imp.set_delete_products()
        self.pages.imp.next_step()
        self.pages.imp.accept_alert()
        self.pages.imp.wait_step_2()
        self.pages.imp.import_settings()
        self.pages.imp.confirm_load()
