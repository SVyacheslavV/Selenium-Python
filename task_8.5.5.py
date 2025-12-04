import time

from selenium import webdriver
from selenium.webdriver.common.by import By

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/window_size/2/index.html') # открываем ссылку

    out_height = browser.get_window_size()['height']  # получаем значение высоты окна
    out_width = browser.get_window_size()['width']  # получаем значение ширины окна

    inner_height = browser.execute_script('return window.innerHeight')  # получаем значение высоты страницы
    inner_width = browser.execute_script('return window.innerWidth')  # получаем значение ширины страницы

    h = out_height - inner_height  # ширина рамки (верх + низ)
    w = out_width - inner_width  # ширина двух боковых рамок


    def get_code(size_x, size_y):
        for x in size_x:
            for y in size_y:
                browser.set_window_size(x + w, y + h)
                time.sleep(.2)
                if (password := browser.find_element(By.ID, 'result').text).isdigit():
                    return password


    print(get_code(window_size_x, window_size_y))
