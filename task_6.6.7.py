"""Операция: Чекбокс"""
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'parent')
    # elements = browser.find_elements(By.CLASS_NAME, "parent")
    # elements = browser.find_elements(By.TAG_NAME, "textarea")
    # for checkbox, text_field in zip(checkboxes, text_fields):
    #     print(checkbox, text_field.get_dom_attribute('value'))
    total = 0
    for element in elements:
        print(element.find_element(By.TAG_NAME, 'textarea').text)
        print(element.is_selected())
        if element.is_selected():
            print(element.find_element(By.TAG_NAME, "textarea"))
            # total += int(element.text)
    # print(total)
