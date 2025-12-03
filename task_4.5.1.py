"""Мастер заполнения форм"""
from selenium import webdriver
from selenium.webdriver.common.by import By

data = ['Иванов', 'Иван', 'Иванович','45','Иваново', 'ivanIvan@mail.ru'] # данные для заполнения

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://parsinger.ru/selenium/1/1.html') # Открываем URL
    # Используем метод .find_elements() для поиска всех элементов class='form'
    forms = browser.find_elements(By.CLASS_NAME, 'form')
    for i, form in enumerate(forms): # перебираем элементы
        form.send_keys(data[i]) # вставляем data[i] в каждый элемент
    browser.find_element(By.CLASS_NAME, "btn").click() # ищем кнопку class="btn" и кликаем её
    print(browser.find_element(By.ID, 'result').text) # ищем элемент id='result' и выводим на экран
