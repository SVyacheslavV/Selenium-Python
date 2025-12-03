"""Учимся получать текст из элемента."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')  # Открываем URL
    button = browser.find_element(By.ID, "showTextBtn")  # ищем кнопку для клика с id="showTextBtn"
    button.click()  # кликаем кнопку
    text = browser.find_element(By.ID, "text1").text  # получаем текст элемента с id="text1"
    placeholder = browser.find_element(By.ID, "userInput")  # ищем окно для вставки текста с id="userInput"
    placeholder.send_keys(text)  # вставляем текст в окно
    button_check = browser.find_element(By.ID, "checkBtn")  # ищем кнопку для клика с id="checkBtn"
    button_check.click()  # кликаем кнопку
    code = browser.find_element(By.ID, "text2").text  # получаем текст элемента с id="text2"
    print(f'Ваш код: {code}')
