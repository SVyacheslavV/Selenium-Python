import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

data = 'ул. Красивая, д. 25'

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.7.1/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # вставляем адрес в элемент с id='address'
    browser.find_element(By.ID, 'address').send_keys(data)
    time.sleep(0.3)  # делаем паузу для наглядности

    # находим элемент с id='payment'
    box = browser.find_element(By.ID, 'payment')
    box.click()  # кликаем элемент с id='payment'
    time.sleep(0.3)  # делаем паузу для наглядности

    # находим элемент value="cash" и кликаем его
    box.find_element(By.CSS_SELECTOR, '[value="cash"]').click()
    time.sleep(0.3)  # делаем паузу для наглядности

    # ожидаем когда элемент с id='submit-order' станет кликабельным и кликаем его
    wait.until(EC.element_to_be_clickable((By.ID, 'submit-order'))).click()

    # ожидаем когда исчезнет элемент с id='spinner'
    wait.until(EC.invisibility_of_element_located((By.ID, 'spinner')))

    # ожидаем появления модального окна
    modal_window = wait.until(EC.visibility_of_element_located((By.ID, 'modal')))
    time.sleep(0.3)  # делаем паузу для наглядности

    # в модальном окне кликаем элемент с id='confirm-address'
    modal_window.find_element(By.ID, 'confirm-address').click()

    # ожидаем когда исчезнет модальное окно
    wait.until(EC.invisibility_of_element_located(modal_window))
    time.sleep(0.3)  # делаем паузу для наглядности

    # кликаем кнопку с id='get-code'
    browser.find_element(By.ID, 'get-code').click()

    # ожидаем появления элемента с id='result' и получаем из него пароль
    password = wait.until(EC.visibility_of_element_located((By.ID, 'result'))).text
    print(password)

    time.sleep(5)
