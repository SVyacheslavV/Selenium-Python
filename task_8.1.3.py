from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("about:blank")
    time.sleep(5)

    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site1/')
    time.sleep(2)
    num1 = browser.title.replace('4', '').replace('3', '').replace('9', '')
    print(num1)
    time.sleep(5)
    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site2/')
    time.sleep(2)
    num2 = browser.title.replace('7', '').replace('8', '').replace('0', '')
    print(num2)
    print(int(num1) + int(num2))
