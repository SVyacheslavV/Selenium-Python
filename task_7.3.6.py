import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.2/index.html')
    element = browser.find_element(By.ID, 'dblclick-area')
    action = ActionChains(browser)
    action.double_click(element).perform() # двойной клик на элементе
    time.sleep(2)
    password = browser.find_element(By.ID, 'passwordContainer').text
    print(password.split()[-1])
    time.sleep(2)
