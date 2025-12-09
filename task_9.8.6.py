import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser: # Инициализация и запуск браузера в конструкции with

    browser.get('https://parsinger.ru/selenium/5.9/4/index.html') # Открываем страницу

    browser.execute_script(f"document.body.style.zoom = '75%'") # уменьшаем масштаб чтобы кнопка была видна на экране

    wait = WebDriverWait(browser, 10) # устанавливаем явное ожидание

    # ожидаем когда кнопка с id='closeBtn' станет кликабельна и кликаем её
    wait.until(EC.element_to_be_clickable((By.ID, 'closeBtn'))).click()

    # Ждем, пока рекламный баннер полностью исчезнет (будет удалён из DOM)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ad-content')))

    # ожидаем когда кнопка onclick = "showSecretNumber()" станет кликабельной и кликаем её
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick = "showSecretNumber()"]'))).click()

    # выводим на экран значение из элемента с id='message'
    print(wait.until(EC.visibility_of_element_located((By.ID, 'message'))).text)

    time.sleep(5) # делаем паузу для наглядности