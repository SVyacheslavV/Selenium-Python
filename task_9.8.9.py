import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация и запуск браузера в конструкции with

    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')  # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    # находим все элементы class='container'
    elements = browser.find_elements(By.CLASS_NAME, 'container')

    for element in elements:
        box = element.find_element(By.TAG_NAME, 'input')  # в элементе находим чекбокс с тегом 'input'

        wait.until(EC.element_to_be_selected(box))  # ожидаем кода чекбокс будет выбран

        element.find_element(By.TAG_NAME, 'button').click()  # кликаем кнопку с тегом 'button'

    password = browser.find_element(By.ID, 'result').text  # получаем пароль из элемента с id='result'
    print(password)

    time.sleep(5)  # делаем паузу для наглядности
