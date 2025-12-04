import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/window_size/1/') # открываем ссылку

    out_height = browser.get_window_size()['height'] # получаем значение высоты окна
    out_width = browser.get_window_size()['width'] # получаем значение ширины окна

    inner_height = browser.execute_script('return window.innerHeight') # получаем значение высоты страницы
    inner_width = browser.execute_script('return window.innerWidth') # получаем значение ширины страницы

    h = out_height - inner_height # ширина рамки (верх + низ)
    w = out_width - inner_width # ширина двух боковых рамок
    time.sleep(2)  # делаем паузу для наглядности

    browser.set_window_size(w + 555, h + 555)  # задаём новый размер окна, чтобы получить рабочую зону 555х555

    time.sleep(2)  # делаем паузу для наглядности

    password = browser.find_element(By.ID, 'result').text

    print(password)