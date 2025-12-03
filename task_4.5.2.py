"""Охотник за сокровищами"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/2/2.html') # Открываем URL
    link = browser.find_element(By.LINK_TEXT, '16243162441624') # ищем ссылку с текстом '16243162441624'
    link.click() # кликаем по ссылке
    time.sleep(3) # делаем паузу для наглядности работы
    print(browser.find_element(By.ID, "result").text)  # ищем элемент id='result' и выводим на экран