import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')  # открываем ссылку
    time.sleep(1)  # делаем паузу для наглядности
    iframes = browser.find_elements(By.TAG_NAME, 'iframe')  # находим все фреймы
    for iframe in iframes:
        browser.switch_to.frame(iframe)  # переключаемся на фрейм
        time.sleep(.2)  # делаем паузу для наглядности
        browser.find_element(By.TAG_NAME, 'button').click()  # кликаем элемент с тегом 'button'
        time.sleep(.2)  # делаем паузу для наглядности
        num = browser.find_element(By.ID, 'numberDisplay').text  # получаем число из элемента с id='numberDisplay'
        browser.switch_to.default_content()  # переключаемся на основное окно
        time.sleep(.2)  # делаем паузу для наглядности
        window = browser.find_element(By.ID, 'guessInput')  # находим элемент с id='guessInput'
        window.send_keys(num)  # вставляем число
        browser.find_element(By.ID, 'checkBtn').click()  # кликаем кнопку с id='checkBtn'
        time.sleep(.2)  # делаем паузу для наглядности

        try:
            alert = browser.switch_to.alert  # пробуем переключится на модальное окно
            print(alert.text)
        except:
            window.clear()  # если модального окна нет очищаем элемент с id='guessInput'

    time.sleep(2)  # делаем паузу для наглядности
