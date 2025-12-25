Проект по автоматизации тестирования учебного сайта [SauceDemo](https://www.saucedemo.com/) с использованием Selenium и Pytest.

## Стек технологий
* **Language:** Python 3.10+
* **Framework:** Pytest
* **Pattern:** Page Object Model (POM)
* **Library:** Selenium WebDriver
* **Utilities:** webdriver-manager (автоматическая установка драйверов)
* **Infrastructure:** Docker

## Структура проекта
* `page/` — содержит описание элементов страниц и методы взаимодействия с ними (LoginPage).
* `test/` — содержит тестовые сценарии и конфигурационный файл `conftest.py`.
* `Dockerfile` — инструкции для сборки образа и запуска тестов в изолированной среде.
* `requirements.txt` — список необходимых зависимостей.

## Реализованные сценарии
В рамках проекта автоматизированы 5 кейсов авторизации:
1. Успешный вход (`standard_user`).
2. Вход заблокированного пользователя (`locked_out_user`).
3. Вход с неверным паролем.
4. Вход с пустыми полями.
5. Проверка работы при задержке системы (`performance_glitch_user`).

## Запуск проекта

### 1. Локально
Установите зависимости:
```bash
pip install -r requirements.txt
Запустите тесты:​
python -m pytest


2. Через Docker​
Соберите образ:​
docker build -t saucedemo-tests .
Запустите контейнер:​
docker run saucedemo-tests


Контакты​
Автор: Никита​

