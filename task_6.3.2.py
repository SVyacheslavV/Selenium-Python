"""Поиск cookie."""
import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')  # открываем url
    all_cookies = browser.get_cookies()  # получаем все cookies
    pprint(all_cookies)  # выводим на экран для наглядности
    name_song = all_cookies[0]["name"]  # так как в списке один элемент сразу находим значение ключа "name"
    # for cookie in all_cookies: # если словарей в списке несколько, перебираем все
    #     name_song = cookie.get("name")
    print(name_song)  # выводим на экран для наглядности
    time.sleep(2)  # делаем паузу для наглядности
    # находим элемент с id='phraseInput' и вставляем название песни
    browser.find_element(By.ID, 'phraseInput').send_keys(name_song)
    time.sleep(2)  # делаем паузу для наглядности
    # находим элемент с id='checkButton' и кликаем его
    browser.find_element(By.ID, 'checkButton').click()
    time.sleep(2)  # делаем паузу для наглядности
    # находим элемент с id='result' и выводим его на экран
    print(browser.find_element(By.ID, 'result').text)
