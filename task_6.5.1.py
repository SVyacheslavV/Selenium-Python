"""Прокрутка к элементу."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')  # открываем url
    element = browser.find_element(By.ID, 'target')  # ищем элемент с id='target'
    time.sleep(2)  # делаем паузу для наглядности
    # прокручиваем страницу пока элемент не будет виден
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    time.sleep(2)  # делаем паузу для наглядности
    element.click()  # кликаем на кнопку
    time.sleep(2)  # делаем паузу для наглядности
    # ищем элемент с id="secret-key-container" и выводим на экран
    print(browser.find_element(By.ID, "secret-key-container").text)
