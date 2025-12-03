from pprint import pprint
from selenium import webdriver


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html') # открываем url
    # получаем cookie где name='token_22' и значение выводим значение 'value' нп экран
    print(browser.get_cookie('token_22')['value'])

    # получаем все cookies на странице
    # cookies = browser.get_cookies()
    # pprint(cookies) # выводим на печать все cookies (список словарей) для наглядности
    # for cookie in cookies: # перебираем cookie
    #     if cookie['name'] == 'token_22': # если 'name'='token_22'
    #         print(cookie['value']) # выводим на печать
    #         break