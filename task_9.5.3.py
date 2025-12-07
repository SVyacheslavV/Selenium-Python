import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # ждём когда элемент id='order-number' появится в DOM и получаем его значение
    password = wait.until(EC.presence_of_element_located((By.ID, 'order-number'))).text
    print(password)
    time.sleep(5)  # делаем паузу для наглядности
