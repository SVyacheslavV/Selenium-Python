import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html') # открываем ссылку

    for i in range(4):
        iframe_element = browser.find_element(By.TAG_NAME, 'iframe') # находим фрейм
        browser.switch_to.frame(iframe_element) # переключаемся на фрейм
        time.sleep(2)  # делаем паузу для наглядности
        browser.find_element(By.TAG_NAME, 'button').click() # кликаем кнопку
        time.sleep(2) # делаем паузу для наглядности

    # получаем пароль из='password-container'
    password = browser.find_element(By.CLASS_NAME, 'password-container').text
    print(password)
    time.sleep(2) # делаем паузу для наглядности