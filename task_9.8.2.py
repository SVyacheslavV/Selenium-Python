import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/expectations/4/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20, 0.1)  # устанавливаем явное ожидание

    # ожидаем когда кнопка с id='btn' станет кликабельной и кликаем её
    wait.until(EC.element_to_be_clickable((By.ID, 'btn'))).click()

    if wait.until(EC.title_contains('JK8HQ')):  # ожидаем когда в заголовке будет 'JK8HQ'

        print(browser.title)  # выводим заголовок на экран

    time.sleep(5)  # делаем паузу для наглядности
