import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--force-device-scale-factor=0.75")
options_chrome.add_argument('--headless')
# options_chrome.add_argument("--start-fullscreen")

with webdriver.Chrome(options=options_chrome) as browser: # Инициализация и запуск браузера в конструкции with
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html') # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    actions = ActionChains(browser) # Создаём экземпляр класса ActionChains

    time.sleep(2)

    # находим все элементы которые нужно перенести
    balls = browser.find_elements(By.CLASS_NAME, 'piece')

    # находим все корзины куда нужно перенести
    baskets = browser.find_elements(By.CLASS_NAME, 'range')

    for ball in balls: # перебираем элементы которые нужно перенести

        # получаем цвет элемента который нужно перенести
        distance_ball = int(ball.get_attribute('id').split('_')[1])

        # переносим на расстояние полученное из атрибута 'id'
        actions.drag_and_drop_by_offset(ball, distance_ball, 0).perform()

    # ожидаем когда появится элемент с id='message' и получаем пароль
    password = wait.until(EC.visibility_of_element_located((By.ID, 'message')))

    browser.execute_script("return arguments[0].scrollIntoView(true);", password)

    print(password.text)

    time.sleep(5)