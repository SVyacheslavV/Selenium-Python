"""Selenium-миссия: Раскрытие численности войск"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.3/index.html'

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    browser.get(url)  # Открываем URL
    attack_planes = browser.find_elements(By.TAG_NAME, "a")  # Ищем все tag 'a'
    total = 0  # переменная для хранения суммы
    # Проходимся по каждому 'a'
    for attack_plane in attack_planes:
        # Получаем значение "stormtrooper"
        stormtrooper_value = attack_plane.get_attribute("stormtrooper")
        if stormtrooper_value.isdigit():
            total += int(stormtrooper_value)
    print(total)
    browser.find_element(By.ID, "inputNumber").send_keys(total)  # вставляем total в окно с id="InputNumber"
    browser.find_element(By.ID, "checkBtn").click()  # кликаем кнопку id = "checkBtn"
    time.sleep(5)  # делаем паузу для наглядности работы
    code = browser.find_element(By.ID, "feedbackMessage").text  # получаем текст элемента id="feedbackMessage"
    print("Result is:", code)
