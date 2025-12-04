import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')  # находим все кнопки с тегом 'input'

    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')  # находим все кнопки 'buttons'

    for button in buttons:  # перебираем кнопки
        button.click()  # кликаем кнопки

        alert = browser.switch_to.alert  # переключаемся на модальное окно
        pin_code = alert.text  # получаем pin_code
        time.sleep(.2)  # делаем паузу для наглядности
        alert.accept()  # кликаем кнопку

        browser.find_element(By.ID, 'input').send_keys(pin_code)  # вставляем pin_code в элемент с id='input'
        browser.find_element(By.ID, 'check').click()  # кликаем кнопку с id='check'
        time.sleep(.2)  # делаем паузу для наглядности

        # получаем пароль из элемента с id='result', если password != 'Неверный пин-код'
        if (password := browser.find_element(By.ID, 'result').text) != 'Неверный пин-код':
            print(password)
            break
