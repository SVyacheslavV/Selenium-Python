"""Учимся получать значение атрибута."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')  # Открываем URL
    button = browser.find_element(By.ID, "secret-key-button")  # ищем кнопку для клика с id="secret-key-button"
    button.click()  # кликаем кнопку
    data = button.get_attribute("data")  # получаем значение атрибута "data" у кнопки
    time.sleep(5)  # делаем паузу для наглядности работы
    print(data)
