import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.3/index.html')
    action = ActionChains(browser) # Создаём экземпляр класса ActionChains
    # нажимаем комбинацию клавиш CONTROL + ALT + SHIFT + 'T'
    action.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('T').perform()
    # отпускаем комбинацию клавиш CONTROL + ALT + SHIFT + 'T'
    action.key_up(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('T').perform()
    time.sleep(2) # делаем паузу для наглядности

    # password = browser.find_element(By.ID, 'passwordContainer').text # получаем пароль по id='passwordContainer'
    # вариант получения пароля по CSS key="access_code"
    password = browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text
    print(password)
    time.sleep(2)