"""Операция: Освобождение пути"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()
# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    total = 0  # для нахождения суммы
    for button in buttons:
        # прокручиваем страницу пока кнопка станет видна на экране
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()  # кликаем кнопку
        # находим значение в элементе с id='result' и суммируем его
        total += int(browser.find_element(By.ID, 'result').text)
    print(f'total: {total}')  # выводим на экран сумму элементов
