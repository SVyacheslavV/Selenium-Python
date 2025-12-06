import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работ

    link = 'https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure' # ссылка, которую будем ждать

    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html') # открываем ссылку
    wait = WebDriverWait(browser, 10) # устанавливаем явное ожидание

    buttons = browser.find_elements(By.CLASS_NAME, 'btn') # находим все кнопки class='btn'

    buttons[-1].click() # кликаем последнюю из списка (по заданию)

    wait.until(EC.url_to_be(link)) # ожидаем пока ссылка совпадёт с заданной по условию

    password = browser.find_element(By.ID, 'password').text # получаем пароль из элемента с id='password'
    print(password)

    time.sleep(3) # делаем паузу для наглядности