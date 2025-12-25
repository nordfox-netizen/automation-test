import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from page.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Проверка: URL изменился на страницу товаров
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
