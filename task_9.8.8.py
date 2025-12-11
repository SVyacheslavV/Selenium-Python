import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:  # Инициализация и запуск браузера в конструкции with

    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')  # Открываем страницу

    wait = WebDriverWait(browser, 10)  # устанавливаем явное ожидание

    wait.until(EC.element_located_to_be_selected((By.ID, 'myCheckbox')))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)
