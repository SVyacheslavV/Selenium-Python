import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.implicitly_wait(6)  # устанавливаем неявное ожидание

    browser.get('https://parsinger.ru/selenium/9/9.3.1/index.html')  # открываем ссылку

    browser.find_element(By.ID, 'startButton').click()  # нажимаем кнопку с id='startButton'

    for _ in range(5):
        # нажимаем кнопку с id='dynamicButton' как только она станет доступна в диапазоне неявного ожидания
        browser.find_element(By.ID, 'dynamicButton').click()

    # получаем пароль из элемента с id='secretPassword'
    password = browser.find_element(By.ID, 'secretPassword').text
    print(password)
    time.sleep(3)  # делаем паузу для наглядности
