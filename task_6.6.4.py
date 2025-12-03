"""Операция: Минное поле"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'text-field')
    for element in elements:
        if element.get_attribute('disabled'):
            continue
        else:
            element.clear()
    browser.find_element(By.ID, 'checkButton').click()
    time.sleep(3)
