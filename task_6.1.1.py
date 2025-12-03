""" Переход назад."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# первый способ
# with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
#     browser.get("https://parsinger.ru/selenium/6/6.2/index.html")  # Открываем URL
#     time.sleep(1)  # делаем паузу для наглядности
#     browser.find_element(By.LINK_TEXT, 'Страница 2').click()  # ищем элемент с текстом 'Страница 2' и кликаем его
#     time.sleep(1)  # делаем паузу для наглядности
#     # ищем элемент с текстом 'Перейти на страницу 3' и кликаем его
#     browser.find_element(By.LINK_TEXT, 'Перейти на страницу 3').click()
#     time.sleep(1)  # делаем паузу для наглядности
#     browser.back()  # возвращаемся на предыдущую страницу
#     time.sleep(1)  # делаем паузу для наглядности
#     browser.back()  # возвращаемся на предыдущую страницу
#     time.sleep(1)  # делаем паузу для наглядности
#     browser.find_element(By.ID, "getPasswordBtn").click()  # ищем элемент с id="getPasswordBtn"
#     time.sleep(2)  # делаем паузу для наглядности
#     print(browser.switch_to.alert.text)


# второй способ
with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get("https://parsinger.ru/selenium/6/6.2/index.html")  # Открываем URL
    time.sleep(1)  # делаем паузу для наглядности
    for _ in range(2):
        browser.find_element(By.TAG_NAME, 'a').click() # ищем элемент с тегом 'a' и кликаем его
        time.sleep(1)  # делаем паузу для наглядности
    for _ in range(2):
        browser.back()  # возвращаемся на предыдущую страницу
        time.sleep(1)  # делаем паузу для наглядности
    browser.find_element(By.ID, "getPasswordBtn").click()  # ищем элемент с id="getPasswordBtn"
    time.sleep(2)  # делаем паузу для наглядности
    print(browser.switch_to.alert.text)