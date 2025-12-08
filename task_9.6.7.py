import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # ожидаем когда в значении атрибута 'src' элемента с id='main-image' появится 'success'
    wait.until(
        EC.text_to_be_present_in_element_attribute((By.ID, 'main-image'), 'src', 'success'))

    browser.find_element(By.ID, 'main-image').click()  # кликаем элемент с id='main-image'

    # ожидаем когда появится элемент с id='password'
    password = wait.until(EC.visibility_of_element_located((By.ID, 'password'))).text
    print(password)

    time.sleep(5)  # делаем паузу для наглядности
