import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/9/9.6.2/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    browser.find_element(By.ID, 'ask-jaskier').click()  # кликаем кнопку с id='ask-jaskier'

    # ожидаем когда значение в элементе с id='recipe_field' будет равно 'Селениумий'
    wait.until(EC.text_to_be_present_in_element_value((By.ID, 'recipe_field'), 'Селениумий'))

    # ожидаем когда появится пароль в элементе с id='password'
    password = wait.until(EC.visibility_of_element_located((By.ID, 'password'))).text
    print(password)

    time.sleep(5)
