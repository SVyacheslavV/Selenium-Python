import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv


load_dotenv()
"""Часть 1. Решение задачи"""
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html') # открываем ссылку
    height = browser.execute_script("return document.body.scrollHeight") # получаем высоту страницы
    time.sleep(2) # делаем паузу для наглядности
    print(height)
    # browser.execute_script(f"window.scrollBy(0,{height})") # прокручиваем страницу на полученное значение
    # time.sleep(5) # делаем паузу для наглядности
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # прокручиваем страницу до конца
    time.sleep(2) # делаем паузу для наглядности
    answer = browser.find_element(By.ID, 'secret-container').text # получаем значение из id='secret-container'
    print(answer)

    """Часть 2. Отправка решения на сайт"""

    # # Переходим на главную страницу, авторизуемся, затем на страницу с заданием
    browser.get("https://stepik.org/catalog")
    time.sleep(3)  # делаем паузу для наглядности
    # кликаем кнопку Вход class='ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button'
    browser.find_element(
        By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button').click()
    time.sleep(2)  # делаем паузу для наглядности
    s_username = browser.find_element(By.ID, "id_login_email")  # ищем поле для ввода логина
    s_username.send_keys(os.getenv('login'))  # вводим логин из файла .env
    time.sleep(2)  # делаем паузу для наглядности
    s_password = browser.find_element(By.ID, "id_login_password")  # ищем поле для ввода пароля
    s_password.send_keys(os.getenv('password'))  # вводим пароль из файла .env
    time.sleep(2)  # делаем паузу для наглядности

    # Ищем кнопку для авторизации
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()
    time.sleep(5)  # делаем паузу для наглядности

    browser.get("https://stepik.org/lesson/732065/step/6")  # переходим на страницу с задачей
    time.sleep(5)  # делаем паузу для наглядности

    # Находим поле для ввода ответа

    # textarea = browser.find_element(By.CLASS_NAME, "cm-string")
    window = browser.find_element(By.CLASS_NAME, "CodeMirror-scroll")
    time.sleep(5)
    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", window)
    time.sleep(5)  # делаем паузу для наглядности
    textarea = browser.find_element(By.CLASS_NAME, "cm-string")
    print(textarea.text)
    # Вставляем текст ответа в найденное поле
    textarea.send_keys(f'"{answer.split()[-1]}"')

    # Отправляем ответ
    # browser.find_element(By.CLASS_NAME, "submit-submission").click()
    #
    # time.sleep(3)  # делаем паузу для наглядности
    # print('Ответ успешно отправлен!')