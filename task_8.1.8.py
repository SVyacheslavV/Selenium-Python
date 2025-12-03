import time
from selenium import webdriver
from selenium.webdriver.common.by import By

total = 0 # сумма чисел

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/8/8.1.2/index.html') # открываем ссылку
    time.sleep(1) # делаем паузу для загрузки страницы
    # получаем ссылки из тегов 'a'
    links = [link.get_attribute('href') for link in browser.find_elements(By.TAG_NAME, 'a')]

    for link in links:
        browser.switch_to.new_window('tab') # переключаем фокус на новую вкладку
        browser.get(link) # открываем ссылку
    time.sleep(3) # делаем паузу для появления чисел

    handles = browser.window_handles # получаем список всех дескрипторов

    for i in range(1, len(handles)):

        browser.switch_to.window(handles[i]) # переключаем фокус на вкладку
        time.sleep(.3) # делаем паузу для наглядности

        numbers = browser.find_elements(By.CLASS_NAME, 'number') # получаем все элементы с числами
        for number in numbers:
            total += int(number.text)

    print(total)

    browser.switch_to.window(handles[0]) # переключаем фокус на первую вкладку
    time.sleep(.3) # делаем паузу для наглядности
    browser.find_element(By.ID, 'sumInput').send_keys(total) # вставляем total в элемент с id='sumInput'
    browser.find_element(By.ID, 'checkButton').click() # кликаем кнопку с id='checkButton'
    password = browser.find_element(By.ID, 'passwordDisplay').text # получаем пароль из id='passwordDisplay'
    print(password)
    time.sleep(5) # делаем паузу для наглядности