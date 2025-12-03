import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.2/index.html')

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода


    while True:  # Начинаем бесконечный цикл
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = browser.find_elements(By.TAG_NAME, 'input')

        # Обходим каждый элемент input в списке
        for ind, tag_input in enumerate(input_tags, 1):
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys(f'I by here, step {ind}')
                tag_input.send_keys(Keys.ENTER)
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                time.sleep(.3)
                list_input.append(tag_input)  # Добавляем элемент в список обработанных элементов
        if ind == 100:
            break

    answer = browser.find_element(By.ID, "hidden-password").text
    print(answer)
