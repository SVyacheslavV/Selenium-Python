import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ

    browser.get('https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')  # открываем ссылку

    wait = WebDriverWait(browser, .6)  # устанавливаем явное ожидание

    while True:
        try:
            wait.until(EC.url_contains('qLChv49'))  # проверяем нахождение подстроки в ссылке
            browser.find_element(By.ID, 'checkButton').click()  # нажимаем кнопку с id='checkButton'
            print(browser.find_element(By.ID, 'result').text)  # получаем пароль из элемента с id='result'
            break
        except:
            browser.find_element(By.ID, 'searchLink').click()  # нажимаем кнопку с id='checkButton'
    time.sleep(3)  # делаем паузу для наглядности
