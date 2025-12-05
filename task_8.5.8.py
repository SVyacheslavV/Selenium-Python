import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

total = 0

with webdriver.Chrome() as browser:

    """Вариант 1 - открываем вкладки по очереди"""

    # for link in sites:
    #     browser.get(link)
    #     time.sleep(1)
    #     browser.find_element(By.TAG_NAME, 'input').click() # кликаем элемент с тегом 'input'
    #     time.sleep(1)
    #     total += math.sqrt(int(browser.find_element(By.ID, 'result').text))
    # print(round(total, 9))
    # time.sleep(3)

    """Вариант 2 - открываем все вкладки"""

    for link in sites:
        browser.switch_to.new_window('tab') # создаём новую вкладку и переключаемся на неё
        browser.get(link) # открываем ссылку
        time.sleep(1) # делаем паузу для наглядности

    window_list = browser.window_handles  # получаем список закладок

    for window in window_list[1:]:
        browser.switch_to.window(window)  # переключаемся на открытое окно
        time.sleep(1) # делаем паузу для наглядности
        browser.find_element(By.TAG_NAME, 'input').click() # кликаем элемент с тегом 'input'
        time.sleep(1) # делаем паузу для наглядности
        # суммируем квадратный корень числа из элемента с id='result'
        total += math.sqrt(int(browser.find_element(By.ID, 'result').text))

    print(round(total, 9))
    time.sleep(3) # делаем паузу для наглядности

