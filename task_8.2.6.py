import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')  # открываем ссылку

    # суммируем высоту и ширину окна
    total = browser.get_window_size().get('height') + browser.get_window_size().get('width')

    browser.find_element(By.ID, 'answer').send_keys(total)  # вставляем значение в элемент с id='answer'
    browser.find_element(By.ID, 'checkBtn').click()  # кликаем кнопку с id='checkBtn'
    time.sleep(2)

    # получаем пароль из элемента с id='resultMessage'
    password = browser.find_element(By.ID, 'resultMessage').text
    print(password)
