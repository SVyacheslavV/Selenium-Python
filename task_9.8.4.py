import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # ожидаем появление элемента с id='qQm9y1rk' и кликаем его
    wait.until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()

    alert = wait.until(EC.alert_is_present())  # ожидаем появления модального окна и переключаемся на него
    print(alert.text)
    time.sleep(.5)  # делаем паузу для наглядности

    alert.accept()  # закрываем модальное окно (ОК)

    time.sleep(5)  # делаем паузу для наглядности
