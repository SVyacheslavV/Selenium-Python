import time

from selenium import  webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--force-device-scale-factor=0.75")
# options_chrome.add_argument('--headless')
# options_chrome.add_argument("--start-fullscreen")


with webdriver.Chrome(options=options_chrome) as browser: # Инициализация и запуск браузера в конструкции with
    browser.get('https://parsinger.ru/selenium/5.10/6/index.html') # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    actions = ActionChains(browser) # Создаём экземпляр класса ActionChains

    time.sleep(2)
    elements = browser.find_elements(By.CLASS_NAME, 'slider-container')

    for element in elements:

        # Получаем текущее значение слайдера
        current_value = int(element.find_element(By.CLASS_NAME, 'current-value').text)

        # Получаем требуемое значение слайдера
        target_value = int(element.find_element(By.CLASS_NAME, 'target-value').text)

        # находим слайдер который нужно двигать в элементе
        slider = element.find_element(By.CLASS_NAME, 'volume-slider')

        if target_value < current_value:

            # Уменьшаем значение имитируя нажимание стрелки влево
            [slider.send_keys(Keys.ARROW_LEFT) for _ in range(abs(current_value - target_value))]

        else:
            # Увеличиваем значение имитируя нажимание стрелки вправо
            [slider.send_keys(Keys.ARROW_RIGHT) for _ in range(abs(current_value - target_value))]

    # ожидаем появления пароля
    password = wait.until(EC.visibility_of_element_located((By.ID, 'message'))).text
    print(password)
    time.sleep(2)