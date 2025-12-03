"""Поход за сокровищами в цифровом лабиринте"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
#     browser.get('https://parsinger.ru/selenium/3/3.html')  # Открываем URL
#     elements = browser.find_elements(By.CLASS_NAME, 'text')  # находим все элементы "text"
#     total = 0
#     for element in elements:  # перебираем элементы
#         total += int(element.find_elements(By.TAG_NAME, 'p')[1].text)  # суммируем каждый второй элемент с тегом 'p'
#     print(f'Сумма каждого второго тега "p": {total}')


# второй способ с использованием XPATH
with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/3/3.html')  # Открываем URL
    # находим все вторые элементы "p" в "text"
    elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    total = sum(int(element.text) for element in elements) # суммируем все элементы
    print(f'Сумма каждого второго тега "p": {total}')