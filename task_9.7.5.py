import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.7.2/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # вставляем в элемент class='search-box' слово 'test'
    browser.find_element(By.CLASS_NAME, 'search-box').send_keys('test')
    time.sleep(0.3)  # делаем паузу для наглядности

    browser.find_element(By.ID, 'search-button').click()  # кликаем кнопку с id='search-button'

    # ожидаем пока элемент с id='old-result' станет видимым и сохраняем его в переменную
    element = wait.until(EC.visibility_of_element_located((By.ID, 'old-result')))

    wait.until(EC.staleness_of(element)) # ждём когда переменная исчезнет из DOM
    time.sleep(0.3)  # делаем паузу для наглядности

    # ждём когда кнопка с id='secret-button' станет кликабельной и кликаем её
    wait.until(EC.element_to_be_clickable((By.ID, 'secret-button'))).click()
    time.sleep(0.3)  # делаем паузу для наглядности

    # ждём когда элемент с id='result' станет видимым и получаем из него пароль
    password = wait.until(EC.visibility_of_element_located((By.ID, 'result'))).text
    print(password)

    time.sleep(5)  # делаем паузу для наглядности
