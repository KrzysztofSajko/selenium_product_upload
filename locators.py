from selenium.webdriver.common.by import By

from utility.myTypes import Locator


class LoginPageLocators:
    EMAIL: Locator = (By.CSS_SELECTOR, "#email")
    PASSWORD: Locator = (By.CSS_SELECTOR, "#passwd")
    SUBMIT: Locator = (By.CSS_SELECTOR, "#submit_login")


class MainPageLocators:
    ADVANCED: Locator = (By.CSS_SELECTOR, "#subtab-AdminAdvancedParameters > a")
    IMPORT: Locator = (By.CSS_SELECTOR, "#subtab-AdminImport > a")


class ImportPageLocators:
    CATEGORY_SELECT: Locator = (By.CSS_SELECTOR, "#entity")
    FILE_IMPORT: Locator = (By.CSS_SELECTOR, "#file")
    IMPORT: Locator = (By.CSS_SELECTOR, "#loadImportMatchs")
    OPTIONS_DELETE_YES: Locator = (By.CSS_SELECTOR, "#main-div > div.content-div > div.row > div > div.row.row.justify-content-center > div > div > div.col-12.col-md-8 > form > div > div.card-body > div.form-group.js-truncate-form-group > div > span > label:nth-child(4)")
    NEXT: Locator = (By.CSS_SELECTOR, "#main-div > div.content-div > div.row > div > div.row.row.justify-content-center > div > div > div.col-12.col-md-8 > form > div > div.card-footer > div > button")
    LOAD: Locator = (By.CSS_SELECTOR, "#import")


class HttpsPageLocators:
    ADVANCED: Locator = (By.CSS_SELECTOR, "#details-button")
    LINK: Locator = (By.CSS_SELECTOR, "#proceed-link")
