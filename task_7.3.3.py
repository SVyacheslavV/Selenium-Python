import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.1/index.html')

    # Вариант 1. Идём пешком )
    # Найти элемент на странице с использованием локатора By
    # draggable = browser.find_element(By.ID, "draggable") # начальное положение

    # Использование ActionChains для выполнения перетаскивания элемента
    # actions = ActionChains(browser)
    # for _ in range(10):
        # Переместить блок вверх на 200px
        # actions.drag_and_drop_by_offset(draggable, 0, -20).perform() # передвигаем на 20px
        # time.sleep(1)

    # Вариант 2. Прыгаем сразу )
    # Найти элемент на странице с использованием локатора By
    draggable = browser.find_element(By.ID, "draggable") # начальное положение
    target = browser.find_element(By.ID, "target") # финальное положение

    # Использование ActionChains для выполнения перетаскивания элемента
    actions = ActionChains(browser)
    actions.drag_and_drop(draggable, target).perform()
    password = browser.find_element(By.ID, 'password').text
    print(password)

    time.sleep(5)