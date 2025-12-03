"""Каскадный поиск."""

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.1/index.html'

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
# with webdriver.Chrome() as browser:
    # Открываем URL
    # browser.get(url)
    # parent = browser.find_element(By.ID, "parent_id") # Ищем родительский элемент id="parent_id"
    # child = parent.find_element(By.CLASS_NAME, "child_class") # Ищем дочерний элемент внутри родительского
    # child.click()
    # password = parent.find_element(By.CLASS_NAME, "child_class").get_attribute("password")
    # print(password)

# Вариант 2
# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    # Открываем URL
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    # применяем методы в одну строку
    child = browser.find_element(By.ID, "parent_id").find_element(By.CLASS_NAME, "child_class")
    child.click()
    print(child.get_attribute("password"))
