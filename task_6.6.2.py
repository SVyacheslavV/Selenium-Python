"""Операция: Чистый Лист"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Создаем объект настроек для Chrome
options_chrome = webdriver.ChromeOptions()
# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome.add_argument('--headless=new')


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--window-size=1920,1080')

# with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    time.sleep(2)
    # elements = browser.find_elements(By.CLASS_NAME, 'text-field')
    element = browser.find_element(By.CLASS_NAME, 'text-field')
    element.clear()
    # all_field = browser.find_elements(By.TAG_NAME, 'input')
    # count = 0
    time.sleep(10)
    # for field in elements:
    #     browser.execute_script("arguments[0].value = ''", field)
        # count += 1
        # print(f'count = {count}: {field.text}')
        # field.clear()

    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
