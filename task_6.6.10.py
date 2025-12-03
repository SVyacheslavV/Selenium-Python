"""Операция: Секретные печеньки"""
from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/methods/3/index.html')  # открываем url
    cookies = browser.get_cookies() # получаем все cookies
    pprint(cookies) # выводим на экран для наглядности
    # суммируем все значения int(cookie['value']) если cookie['name'] начинается с secret_cookie
    total = sum(
        [int(cookie['value']) for cookie in cookies if cookie if cookie.get('name').startswith('secret_cookie')])
    print(total)