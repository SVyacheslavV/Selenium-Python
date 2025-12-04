import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')  # открываем ссылку

    pin_codes = browser.find_elements(By.CLASS_NAME, 'pin')  # находим все элементы class='pin'

    for pin_cod in pin_codes:
        pin = pin_cod.text  # получаем текст из элемента
        time.sleep(.3)

        browser.find_element(By.ID, 'check').click()  # кликаем кнопку с id='check'

        alert = browser.switch_to.alert  # переключаемся на модальное окно
        alert.send_keys(pin)  # вставляем pin
        time.sleep(.3)
        alert.accept()  # Закрываем модальное окно (OK)
        # проверяем пароль в элементе с id='result'
        if (password := browser.find_element(By.ID, 'result').text) != 'Неверный пин-код':
            print(password)
            break
    time.sleep(3)
