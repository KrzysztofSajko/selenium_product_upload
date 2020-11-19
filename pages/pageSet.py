from selenium.webdriver import Chrome

from pages.httpsPage import HttpsPage
from pages.importPage import ImportPage
from pages.loginPage import LoginPage
from pages.mainPage import MainPage


class PageSet:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver
        self.login: LoginPage = LoginPage(driver)
        self.main: MainPage = MainPage(driver)
        self.imp: ImportPage = ImportPage(driver)
        self.https: HttpsPage = HttpsPage(driver)
