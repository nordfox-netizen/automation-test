import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    # Эти настройки нужны для работы в Docker (без графического интерфейса)
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  # Ждем элементы до 10 секунд
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

from page.login_page import LoginPage
# 2. Неверный пароль
def test_wrong_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    assert "Username and password do not match" in page.get_error_text()

# 3. Заблокированный пользователь
def test_locked_user(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out" in page.get_error_text()

# 4. Пустые поля
def test_empty_fields(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert "Username is required" in page.get_error_text()

# 5. Performance glitch user (проверка задержки)
def test_performance_glitch(driver):
    page = LoginPage(driver)
    page.open()
    page.login("performance_glitch_user", "secret_sauce")
    # Проверяем, что в итоге попали на страницу товаров
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"




