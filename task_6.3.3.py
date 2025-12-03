"""Удалите все cookies."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get("https://parsinger.ru/selenium/6/6.3.2/index.html")  # открываем url
    browser.delete_all_cookies()  # удаляем все cookies на странице
    time.sleep(1)  # делаем паузу для наглядности
    # print(browser.find_element(By.TAG_NAME, 'p').text)
    print(browser.find_element(By.ID, 'password').text)  # ищем элемент с id='password' и выводим на печать
    time.sleep(1)  # делаем паузу для наглядности
