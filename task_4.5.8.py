"""Миссия: Загадочный след"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/6/6.html') # Открываем URL
    # получаем пример из id='text_box' и решаем его с помощью eval
    number = eval(browser.find_element(By.ID, 'text_box').text)
    browser.find_element(By.ID, 'selectId').click() # находим элемент id='selectId' и кликаем его
    elements = browser.find_elements(By.TAG_NAME, 'option') # получаем все элементы с тегом 'option'
    for element in elements: # перебираем элементы
        if int(element.text) == number: # если значение равно number
            element.click() # кликаем его
            break
    time.sleep(2) # делаем паузу для наглядности
    browser.find_element(By.CLASS_NAME, 'btn').click() # ищем кнопку class='btn' и кликаем её
    time.sleep(2)  # делаем паузу для наглядности
    print(browser.find_element(By.ID, 'result').text) # ищем элемент id='result' и выводим на экран