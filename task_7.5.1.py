import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


with webdriver.Chrome() as browser:
    """Решение задачи"""
    browser.get('https://parsinger.ru/scroll/2/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'item')
    total = 0
    for element in elements:
        element.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        res = element.find_element(By.TAG_NAME, 'span').text
        if res.isdigit():
            total += int(res)
        time.sleep(.3)
    print(total)

    """Часть 2. Отправка решения на сайт"""
    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием
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

    browser.get("https://stepik.org/lesson/732069/step/1")  # переходим на страницу с задачей
    time.sleep(6)  # делаем паузу для наглядности

    # Находим поле для ввода ответа
    textarea = browser.find_element(By.CLASS_NAME, "number-quiz__input.number-input")
    # textarea = browser.find_element(By.CSS_SELECTOR, '[placeholder="Введите число"]')

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    time.sleep(5)  # делаем паузу для наглядности
    # Вставляем текст ответа в найденное поле
    textarea.send_keys(total)

    # Отправляем ответ
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    time.sleep(3)  # делаем паузу для наглядности
    print('Ответ успешно отправлен!')