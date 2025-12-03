import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.4/index.html')
    element = browser.find_element(By.ID, 'context-area')  # находим элемент с id='context-area'
    action = ActionChains(browser)  # Создаём экземпляр класса ActionChains
    action.context_click(element).perform()  # кликаем правой кнопкой по элементу для открытия контекстного меню
    time.sleep(2)  # делаем паузу для наглядности

    # находим элемент по селектору data-action="get_password" и кликаем его
    browser.find_element(By.CSS_SELECTOR, '[data-action="get_password"]').click()
    time.sleep(2)  # делаем паузу для наглядности

    # получаем пароль из элемента с id='passwordContainer' (вместе со всем текстом)
    # password = browser.find_element(By.ID, 'passwordContainer').text

    # вариант получения только пароля по селектору key="access_code"
    password = browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text

    print(password)
    time.sleep(2)  # делаем паузу для наглядности
