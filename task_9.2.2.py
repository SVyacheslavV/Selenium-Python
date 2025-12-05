import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 30)  # создаём явное ожидание

    browser.find_element(By.ID, 'startScan').click()  # кликаем кнопку с id='startScan'

    wait.until(EC.title_is('Access Granted'))  # ждём пока title не совпадёт с 'Access Granted'

    # получаем пароль из элемента с id='passwordValue' с использованием явного ожидания
    password = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'passwordValue')))

    print(password.text)
    time.sleep(3)  # делаем паузу для наглядности
