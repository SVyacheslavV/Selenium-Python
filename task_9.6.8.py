import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.6.4/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # ожидаем появления атрибута 'confirmed' в элементе с id='booking-number'
    wait.until(EC.element_attribute_to_include((By.ID, 'booking-number'), 'confirmed'))

    # получаем номер из элемента с id='booking-number'
    number = browser.find_element(By.ID, 'booking-number').text

    # вставляем номер в элемент с id='booking-input'
    browser.find_element(By.ID, 'booking-input').send_keys(number)

    # кликаем кнопку с id='check-button'
    browser.find_element(By.ID, 'check-button').click()

    # получаем пароль из элемента с id='secret-password'
    password = wait.until(EC.visibility_of_element_located((By.ID, 'secret-password'))).text

    print(password)

    time.sleep(5)  # делаем паузу для наглядности
