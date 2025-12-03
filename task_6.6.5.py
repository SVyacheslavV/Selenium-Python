"""Операция: Бессмертный Печенюшка"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()
# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/methods/5/index.html') # открываем url
    elements = browser.find_elements(By.CLASS_NAME, 'urls') # находим все элементы class='urls'
    nums = {} # словарь
    for element in elements: # перебираем элементы
        element.click() # кликаем элемент
        cookies = browser.get_cookies() # получаем cookies страницы
        key = cookies[0]['expiry'] # значением ключа выбираем 'expiry'
        value = browser.find_element(By.ID, 'result').text # получаем значение из id='result'
        nums[key] = value # добавляем в словарь
        print(nums) # выводим на экран для наглядности
        browser.back()
    print(nums[max(nums)]) # выводим на экран значение у максимального ключа словаря nums
