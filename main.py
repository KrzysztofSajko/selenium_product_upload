import json
from typing import Dict, Any

from selenium.webdriver import Chrome

from executor import Executor
from pages.pageSet import PageSet

with open("config.json", encoding="utf-8") as config_json:
    config: Dict[str, Any] = json.load(config_json)

driver_path: str = config["driverPath"]
shop_address: str = config["shopAddress"]

driver: Chrome = Chrome(driver_path)
driver.implicitly_wait(10)
driver.get(shop_address)

executor: Executor = Executor(driver, PageSet(driver))

email: str = config["adminEmail"]
password: str = config["adminPassword"]

executor.login(email, password)

products: str = config["productsPath"]
category: str = config["importCategory"]

executor.import_products(products, category)
