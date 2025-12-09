import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/expectations/3/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # ожидаем когда кнопка с id='btn' станет кликабельной и кликаем её
    wait.until(EC.element_to_be_clickable((By.ID, 'btn'))).click()

    # ожидаем когда заголовок будет '345FDG3245SFD'
    wait.until(EC.title_is('345FDG3245SFD'))

    # получаем пароль из элемента с id='result'
    password = wait.until(EC.presence_of_element_located((By.ID, 'result'))).text

    print(password)

    time.sleep(5)  # делаем паузу для наглядности
