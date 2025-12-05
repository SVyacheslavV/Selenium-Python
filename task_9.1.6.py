import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html') # открываем ссылку

    buttons = browser.find_elements(By.TAG_NAME, 'button') # находим все элементы с тегом 'button'
    wait = WebDriverWait(browser, 10) # создаём явное ожидание

    for button in buttons:
        # как только элемент button становится кликабельным, делаем клик
        wait.until(EC.element_to_be_clickable(button)).click()
    time.sleep(2) # делаем паузу для наглядности

    password = browser.find_element(By.ID, 'message').text
    print(password)