import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 50)  # устанавливаем явное ожидание

    # Ожидаем, когда курс доллара достигнет целевого значения "75.50 ₽" (элемент с id='usd-rate')
    wait.until(EC.text_to_be_present_in_element((By.ID, 'usd-rate'), '75.50 ₽'))

    # ожидаем когда появится секретный код (элемент с id='secret-code')
    password = wait.until(EC.visibility_of_element_located((By.ID, 'secret-code'))).text

    time.sleep(2)  # делаем паузу для наглядности
    print(password)

    # кликаем кнопку с id='close-notification' чтобы закрыть окно с паролем
    browser.find_element(By.ID, 'close-notification').click()

    time.sleep(5)  # делаем паузу для наглядности
