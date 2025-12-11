import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:  # Инициализация и запуск браузера в конструкции with

    browser.get('https://parsinger.ru/draganddrop/1/index.html')  # Открываем страницу

    element = browser.find_element(By.ID, 'draggable')  # Находим исходный элемент, который будем перемещать

    target = browser.find_element(By.ID, 'field2')  # Находим элемент, куда будем перемещать element

    actions = ActionChains(browser)  # Создаём экземпляр класса ActionChains

    # actions.drag_and_drop(element, target).perform() # Выполняем действие перетаскивания

    actions.click_and_hold(element).move_to_element(target).release().perform()  # Выполняем действие перетаскивания

    password = browser.find_element(By.ID, 'result').text  # получаем пароль из элемента с id='result'
    print(password)

    time.sleep(3)  # делаем паузу для наглядности
