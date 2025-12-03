"""Операция: Охота на скрытые сокровища"""
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/methods/1/index.html')  # открываем url
    count = 0  # количество попыток
    while True:
        count += 1  # прибавляем попытку
        number = browser.find_element(By.ID, 'result').text  # ищем элемент с id='result'
        if number.isdigit():  # если это число
            print(f'Попытка {count}, искомое число: {number}')  # выводим на экран попытку и число
            break
        else:  # иначе
            browser.refresh()  # обновляем страницу
