import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 10)  # устанавливаем явное ожидание

    # кликаем кнопку с id='showProducts'
    browser.find_element(By.ID, 'showProducts').click()

    # локатор поиска элементов
    locator = (By.CLASS_NAME, 'product')

    # ждём пока все элементы будут видны
    goods = wait.until(EC.visibility_of_all_elements_located(locator))

    # находим сумму стоимостей всех элементов ($ удаляем срезом)
    total = sum([int(good.find_element(By.CLASS_NAME, 'price').text[1:]) for good in goods])

    # вставляем сумму в элемент с id='sumInput'
    browser.find_element(By.ID, 'sumInput').send_keys(total)

    # кликаем кнопку с id='checkSum'
    browser.find_element(By.ID, 'checkSum').click()

    # получаем пароль из элемента с id='secretMessage'
    password = wait.until(EC.visibility_of_element_located((By.ID, 'secretMessage'))).text
    print(password)

    time.sleep(5)  # делаем паузу для наглядности
