import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
    for i in range(1, 5):
        iframe_element = browser.find_element(By.ID, f'frame{i}')  # находим фрейм
        browser.switch_to.frame(iframe_element)  # переключаемся на фрейм
        time.sleep(2)  # делаем паузу для наглядности
        try:
            browser.find_element(By.TAG_NAME, 'button').click()  # кликаем кнопку
            time.sleep(2)  # делаем паузу для наглядности
        except:
            password = browser.find_element(By.TAG_NAME, 'h2').text  # получаем пароль из тега 'h2'
            time.sleep(2)  # делаем паузу для наглядности
            print(password)

        browser.switch_to.default_content()
