"""Операция: Ад цветовых шифров"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')

    # Вариант 1
    # elements = browser.find_element(By.ID, 'main-container').find_elements(By.TAG_NAME, 'div')
    # for ind, element in enumerate(elements):
    #     if ind % 2 == 0:
    #         color = element.find_element(By.TAG_NAME, 'span').text
    #
    #         # Выбираем соответствующий цвет в выпадающем списке
    #         select_color = element.find_element(By.TAG_NAME, 'select')
    #         select_color.click()
    #         all_color = select_color.find_elements(By.TAG_NAME, 'option')
    #         for color_ in all_color:
    #             if color_.get_attribute('value') == color:
    #                 color_.click()
    #                 break
    #
    #         buttons = element.find_elements(By.TAG_NAME, 'button')
    #         for color_ in buttons:
    #             if color_.get_attribute('data-hex') == color:
    #                 color_.click()
    #                 break
    #         element.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    #         element.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(color)
    #         buttons[-1].click()
    #     # time.sleep(2)
    # browser.find_elements(By.TAG_NAME, 'button')[-1].click()
    # alert = browser.switch_to.alert
    # answer = alert.text
    # print(answer)
    # time.sleep(2)
    # alert.accept()
    #
    # time.sleep(2)

    # Вариант 2

    wait = WebDriverWait(browser, 10)
    containers = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[style*="background-color"]')))
    for container in containers:
        # Получаем HEX цвет из <span>
        hex_color = container.find_element(By.TAG_NAME, 'span').text

        # Выбираем соответствующий цвет в выпадающем списке
        Select(container.find_element(By.TAG_NAME, 'select')).select_by_value(hex_color)

        # Нажимаем на кнопку с атрибутом data-hex равным HEX цвету
        container.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]').click()

        # Ставим галочку в чек-боксе
        container.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()

        # Вставляем HEX-цвет в текстовое поле
        container.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(hex_color)

        # Нажимаем кнопку "Проверить"
        container.find_element(By.XPATH, './/button[text()="Проверить"]').click()

    # Нажимаем кнопку "Проверить все элементы" внизу страницы
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Проверить все элементы"]'))).click()

    alert = browser.switch_to.alert
    answer = alert.text
    print(answer)

    """Часть 2. Отправка решения на сайт"""

    # # Переходим на главную страницу, авторизуемся, затем на страницу с заданием
    # browser.get("https://stepik.org/catalog")
    # time.sleep(3)  # делаем паузу для наглядности
    # # кликаем кнопку Вход class='ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button'
    # browser.find_element(
    #     By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button').click()
    # time.sleep(2)  # делаем паузу для наглядности
    # s_username = browser.find_element(By.ID, "id_login_email")  # ищем поле для ввода логина
    # s_username.send_keys(os.getenv('login'))  # вводим логин из файла .env
    # time.sleep(2)  # делаем паузу для наглядности
    # s_password = browser.find_element(By.ID, "id_login_password")  # ищем поле для ввода пароля
    # s_password.send_keys(os.getenv('password'))  # вводим пароль из файла .env
    # time.sleep(2)  # делаем паузу для наглядности
    #
    # # Ищем кнопку для авторизации
    # browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()
    # time.sleep(5)  # делаем паузу для наглядности
    #
    # browser.get("https://stepik.org/lesson/732063/step/9")  # переходим на страницу с задачей
    # time.sleep(10)  # делаем паузу для наглядности
    #
    # # Находим поле для ввода ответа
    #
    # textarea = browser.find_element(By.CLASS_NAME, "number-quiz__input.number-input")
    #
    # time.sleep(5)
    # # Скролл до текстового поля, иначе элемент не находится
    # browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    # time.sleep(5)  # делаем паузу для наглядности
    # # Вставляем текст ответа в найденное поле
    # textarea.send_keys(answer)
    #
    # # Отправляем ответ
    # browser.find_element(By.CLASS_NAME, "submit-submission").click()
    #
    # time.sleep(3)  # делаем паузу для наглядности
    # print('Ответ успешно отправлен!')

