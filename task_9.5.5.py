import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 10)  # устанавливаем явное ожидание

    # ждём когда кнопка id='ghost-button' появится в DOM и будет видна на экране и кликаем её
    wait.until(EC.visibility_of_element_located((By.ID, 'ghost-button'))).click()

    # ждём когда элемент id='password-display' появится в DOM и будет виден на экране, получаем значение
    password = wait.until(EC.visibility_of_element_located((By.ID, 'password-display'))).text
    print(password)

    time.sleep(5)
