"""Операция кодовый замок"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/4/4.html') # Открываем URL
    # [x.click() for x in browser.find_elements(By.CLASS_NAME, 'check')]
    boxes = browser.find_elements(By.CLASS_NAME, 'check')
    for box in boxes:
        box.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(3)