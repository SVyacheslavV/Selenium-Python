import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

load_dotenv()

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    total = 0
    while len(list_input) < 100:
        p_tags = browser.find_element(By.CLASS_NAME, 'scroll-container').find_elements(By.TAG_NAME, 'p')
        for p_tag in p_tags:
            id = p_tag.get_attribute('id')
            if id not in list_input:
                total += int(p_tag.text)
                list_input.append(id)
                time.sleep(.3)
                browser.execute_script("return arguments[0].scrollIntoView(true);", p_tag)

    print(f'Сумма всех элементов: {total}')

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

    browser.get("https://stepik.org/lesson/732069/step/3")  # переходим на страницу с задачей
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