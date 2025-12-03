"""Учимся вводить текст в поле."""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL = "https://parsinger.ru/selenium/3/3.2.2/index.html" # ссылка где будем искать

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("id", "codeInput").send_keys("Дрогон") # вставляем текст в окно с id="codeInput"
#     driver.find_element("id", "clickButton").click() # кликаем кнопку id="clickButton"
#     time.sleep(5)
#     code = driver.find_element("id", "codeOutput").text # получаем текст элемента id="codeOutput"
#     print("Result is:", code)

# вариант 2
# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')  # Открываем URL
    placeholder = browser.find_element(By.ID, "codeInput")  # ищем окно для вставки текста id="codeInput"
    placeholder.send_keys('Дрогон')  # вставляем 'Дрогон' в окно
    time.sleep(1)  # делаем паузу для наглядности работы
    button = browser.find_element(By.ID, "clickButton")  # ищем кнопку для клика id="clickButton"
    button.click()  # кликаем кнопку
    time.sleep(5)  # делаем паузу для наглядности работы
    code = browser.find_element(By.ID, "codeOutput").text  # получаем текст элемента id="codeOutput"
    print(f'Ваш код: {code}')
