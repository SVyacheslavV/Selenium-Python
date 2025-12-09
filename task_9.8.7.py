import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

code = []

with webdriver.Chrome() as browser:  # Инициализация и запуск браузера в конструкции with

    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')  # Открываем страницу

    wait = WebDriverWait(browser, 10)  # устанавливаем явное ожидание

    elements = browser.find_elements(By.CLASS_NAME, 'box_button')  # находим все элементы class='box_button'

    for element in elements:
        element.click()  # кликаем элемент

        # кликаем элемент с id='close_ad'
        # browser.find_element(By.ID, 'close_ad').click()

        # ожидаем когда элемент с id='close_ad' станет кликабельным и кликаем его
        wait.until(EC.element_to_be_clickable((By.ID, 'close_ad'))).click()

        wait.until(lambda _: element.text != '')  # ожидаем когда в значении элемента появится текст

        code.append(element.text)  # получаем текст и добавляем его в список

    print(*code, sep='-')  # собираем список в строку (вариант 1)
    print('-'.join(code))  # собираем список в строку (вариант 2)

    time.sleep(5)  # делаем паузу для наглядности
