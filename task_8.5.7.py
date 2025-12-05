import time

from selenium import webdriver
from selenium.webdriver.common.by import By

total = 0  # переменная для суммирования чисел

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/blank/3/index.html')  # открываем ссылку

    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')  # находим кнопки class='buttons'
    time.sleep(1)  # делаем паузу для наглядности

    """Вариант 1 будут открыты все вкладки"""

    # for i, button in enumerate(buttons, 1):  # перебираем кнопки
    #
    #     button.click()  # кликаем кнопку
    #     time.sleep(1)  # делаем паузу для наглядности
    #     window_list = browser.window_handles  # получаем список дескрипторов
    #
    #     browser.switch_to.window(window_list[i])  # переключаемся на открытое окно
    #     num = browser.title  # находим title страницы
    #     total += int(num)  # суммируем значение
    #     time.sleep(1)  # делаем паузу для наглядности
    #
    #     browser.find_element(By.TAG_NAME, 'a').click()  # кликаем по элементу с тегом 'a'
    #     browser.switch_to.window(window_list[0])
    # time.sleep(5)
    #
    # print(f'Сумма чисел: {total}')

    """Вариант 2 каждая вкладка будет закрываться после открытия и получения данных"""

    current_handle = browser.current_window_handle # основная вкладка
    for button in buttons: # перебираем кнопки
        button.click()  # кликаем кнопку
        time.sleep(1)  # делаем паузу для наглядности
        window_list = browser.window_handles  # получаем список дескрипторов

        browser.switch_to.window(window_list[1])  # переключаемся на открытое окно
        total += int(browser.execute_script('return document.title;'))  # суммируем значение
        browser.close() # закрываем текущую вкладку
        time.sleep(1)  # делаем паузу для наглядности
        browser.switch_to.window(current_handle) # переключаемся на основную вкладку
    print(f'Сумма чисел: {total}')