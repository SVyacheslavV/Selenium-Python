"""Добавьте cookie на сайт."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# словарь cookie
cookie_dict = {
    'name': 'secretKey',
    'value': 'selenium123',
}

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')  # открываем url
    time.sleep(2)  # делаем паузу для наглядности
    # Добавляет файл cookie в текущий контекст браузера.
    browser.add_cookie(cookie_dict)  # добавляем cookie
    time.sleep(2)  # делаем паузу для наглядности
    browser.refresh()  # обновляем страницу
    time.sleep(2)  # делаем паузу для наглядности
    print(browser.find_element(By.ID, "password").text)  # ищем и выводим на экран элемент с id="password"
