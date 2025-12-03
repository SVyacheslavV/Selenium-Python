"""Учимся кликать по кнопке."""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() # создаём соединение
browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')  # Открываем URL
button = browser.find_element(By.ID, "clickButton")  # ищем кнопку с id="clickButton"
button.click()  # кликаем кнопку
time.sleep(5)  # делаем паузу для наглядности работы
code = browser.find_element(By.ID, "codeOutput").text  # получаем текст элемента id="codeOutput"
print("Result is:", code)  # выводим на экран текст
browser.quit() # закрываем соединение
