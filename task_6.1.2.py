"""Делаем скриншот."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html') # открываем url
    time.sleep(5) # делаем паузу для наглядности
    # ищем элемент с id='this_pic' и сохраняем его в папке с проектом
    browser.find_element(By.ID, 'this_pic').screenshot('file_name.png')
