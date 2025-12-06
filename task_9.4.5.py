import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 10)  # устанавливаем явное ожидание

    browser.find_element(By.CLASS_NAME, 'btn').click()  # нажимаем кнопку class='btn'

    current_url = browser.current_url  # получаем текущий url

    wait.until(EC.url_changes(current_url))  # ждём пока изменится url

    password = browser.find_element(By.ID, 'password').text  # получаем пароль из элемента с id='password'
    print(password)

    time.sleep(3)  # делаем паузу для наглядности
