import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')  # открываем ссылку

    browser.find_element(By.ID, 'alertButton').click()  # нажимаем кнопку с id='alertButton'
    time.sleep(2)  # делаем паузу для наглядности
    alert = browser.switch_to.alert  # переключаемся на модальное окно
    alert.accept()  # закрываем модальное окно (OK)

    browser.find_element(By.ID, 'promptButton').click()  # нажимаем кнопку с id='promptButton'
    time.sleep(2)  # делаем паузу для наглядности
    prompt = browser.switch_to.alert  # переключаемся на модальное окно
    time.sleep(2)  # делаем паузу для наглядности
    prompt.send_keys('Alert')  # вставляем текст 'Alert' в модальное окно
    time.sleep(2)  # делаем паузу для наглядности
    prompt.accept()  # закрываем модальное окно (OK)

    browser.find_element(By.ID, 'confirmButton').click()  # нажимаем кнопку с id='confirmButton'
    time.sleep(2)  # делаем паузу для наглядности
    confirm = browser.switch_to.alert  # переключаемся на модальное окно
    confirm.accept()  # закрываем модальное окно (OK)
    time.sleep(2)  # делаем паузу для наглядности

    password = browser.find_element(By.ID, 'secretKey').text  # получаем пароль из элемента с id='secretKey'
    print(password)
