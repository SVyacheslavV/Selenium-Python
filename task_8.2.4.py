import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')  # открываем ссылку

    # выводим на экран текущий размер окна с помощью генератора
    [print(f'{key}: {value}') for key, value in browser.get_window_size().items()]

    time.sleep(2)  # делаем паузу для наглядности

    browser.set_window_size(1200, 720)  # задаём новый размер окна

    time.sleep(2)  # делаем паузу для наглядности

    print(f'Высота после изменения: {browser.get_window_size().get('height')}')  # выводим на экран высоту
    print(f'Ширина после изменения: {browser.get_window_size().get('width')}')  # выводим на экран ширину

    # [print(f'{key}: {value}') for key, value in browser.get_window_size().items()]

    browser.find_element(By.ID, 'checkSizeBtn').click()  # находим кнопку с id='checkSizeBtn'

    time.sleep(2)  # делаем паузу для наглядности

    password = browser.find_element(By.ID, 'secret').text  # находим пароль

    print(password)
    time.sleep(2)  # делаем паузу для наглядности
