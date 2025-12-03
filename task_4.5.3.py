"""Кодекс охотников за цифрами"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
#     browser.get("https://parsinger.ru/selenium/3/3.html") # Открываем URL
#     all_element = browser.find_elements(By.TAG_NAME, "p") # находим все теги "p"
#     total = sum(int(element.text) for element in all_element) # находим сумму всех элементов
#     print(total)


# кластерный поиск
with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get("https://parsinger.ru/selenium/3/3.html")  # Открываем URL
    elements = browser.find_elements(By.CLASS_NAME, "text")  # находим все элементы "text"
    total = 0
    for element in elements:  # перебираем элементы
        p_element_all = element.find_elements(By.TAG_NAME, "p")  # находим все теги "p" в элементе
        sum_p = sum(int(p_element.text) for p_element in p_element_all)  # находим сумму всех тегов "p" в элементе
        total += sum_p  # находим сумму всех тегов "p" в элементах
    print(f'Сумма всех тегов "p": {total}')
