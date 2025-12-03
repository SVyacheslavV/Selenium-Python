"""Операция: Выпадающие списки"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/7/7.html')  # Открываем URL
    elements = browser.find_elements(By.TAG_NAME, 'option')  # ищем все элементы с тегом 'option'
    total = sum(int(element.text) for element in elements)  # суммируем все значения
    # ищем все элемент id='input_result' и вставляем в него total
    browser.find_element(By.ID, 'input_result').send_keys(total)
    time.sleep(2)  # делаем паузу для наглядности работы
    browser.find_element(By.CLASS_NAME, 'btn').click()  # ищем кнопку class='btn'  и кликаем её
    time.sleep(2)  # делаем паузу для наглядности работы
    print(f'Ваш код: {browser.find_element(By.ID, 'result').text}')  # ищем и выводим на экран id='result'
