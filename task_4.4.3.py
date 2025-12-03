"""Поиск внутри списка элементов"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.2/index.html' # ссылка с которой будем работать

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    browser.get(url) # Открываем URL
    # Используем метод .find_elements() для поиска всех элементов class='block'
    elements = browser.find_elements(By.CLASS_NAME, "block")
    for element in elements: # перебираем элементы
        element.find_element(By.CLASS_NAME, "button").click() # ищем кнопку class="button" и кликаем её
        time.sleep(1) # делаем паузу для наглядности работы
    print(browser.find_element(By.TAG_NAME, "password").text) # ищем элемент tag='result' и выводим на экран
