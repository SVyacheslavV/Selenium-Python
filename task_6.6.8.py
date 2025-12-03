"""Операция: Цветовая Синхронизация"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')  # открываем url
    elements = browser.find_elements(By.CLASS_NAME, 'parent')
    for element in elements:
        # Извлекаем текст из <textarea> с атрибутом color="gray"
        gray = element.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]')
        # gray = element.find_elements('xpath', '//textarea[@color="gray"]')
        # Вставляем извлеченный текст в <textarea> с атрибутом color="blue"
        element.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(gray.text)
        gray.clear()  # Очищаем содержимое <textarea> с атрибутом color="gray"
        element.find_element(By.TAG_NAME, 'button').click()  # Нажимаем на кнопку внутри текущего блока
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)
