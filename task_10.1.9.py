import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:  # Инициализация и запуск браузера в конструкции with
    browser.get('https://parsinger.ru/draganddrop/2/index.html')  # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    actions = ActionChains(browser)  # Создаём экземпляр класса ActionChains

    # Находим исходный элемент, который будем перемещать
    element = browser.find_element(By.ID, 'draggable')

    for i in range(1, 5):
        # Находим элемент, куда будем перемещать element
        target = browser.find_element(By.ID, f'box{i}')

        actions.drag_and_drop(element, target).perform()  # Выполняем действие перетаскивания
        # actions.click_and_hold(element).move_to_element(target).release().perform()

        time.sleep(.2)  # делаем паузу для наглядности

    # ожидаем когда появится пароль в элементе с id='message' и запоминаем его
    password = wait.until(EC.visibility_of_element_located((By.ID, 'message')))

    print(password.text)
    time.sleep(5)  # делаем паузу для наглядности
