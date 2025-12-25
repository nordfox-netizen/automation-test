import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from page.login_page import LoginPage

# Список тестов
def test_standard_login(driver):
    driver.get("https://www.saucedemo.com/") # Гарантируем, что мы на логине
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_login_locked_out(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out" in login_page.get_error_message()

def test_login_wrong_password(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error_message()

def test_login_empty_fields(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("", "")
    assert "Username is required" in login_page.get_error_message()

def test_login_performance_glitch(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("performance_glitch_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

