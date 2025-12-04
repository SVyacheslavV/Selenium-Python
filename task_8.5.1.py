import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')  # открываем ссылку

    buttons = browser.find_elements(By.TAG_NAME, 'input')  # находим все кнопки с тегом 'input'

    for button in buttons:  # проходим по всем кнопкам
        button.click()  # кликаем кнопку
        time.sleep(.2)  # делаем паузу для наглядности
        browser.switch_to.alert.accept()  # закрываем модальное окно

        # если в элементе с id='result' находятся цифры
        if (password := browser.find_element(By.ID, 'result').text).isdigit():
            break  # останавливаем цикл
        time.sleep(.2)
    print(password)
