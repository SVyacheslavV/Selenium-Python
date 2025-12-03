import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')  # открываем ссылку

    """Вариант 1 -  сначала скроллинг всей страницы до появления всех необходимых элементов"""

    # # находим объект для скроллинга, с id='main_container'
    # scrollable_element = browser.find_element(By.ID, 'main_container')
    #
    # count = 0  # будем считать количество элементов
    #
    # # скроллинг страницы до конца вниз
    # while count < 100:
    #     browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", scrollable_element)
    #
    #     # считаем количество элементов после прокрутки
    #     count = len(scrollable_element.find_elements(By.CLASS_NAME, 'child_container'))
    #     time.sleep(.3)
    #     print(f'count: {count}') # вывод для наглядности
    #
    # # скроллинг страницы вверх
    # browser.execute_script("arguments[0].scrollTo(arguments[0].scrollHeight, 0)", scrollable_element)
    # time.sleep(.3)
    #
    # # перебираем все элементы class='child_container'
    # for child_container in scrollable_element.find_elements(By.CLASS_NAME, 'child_container'):
    #
    #     # находим теги 'input'
    #     input_elements = child_container.find_elements(By.TAG_NAME, 'input')
    #     for input_element in input_elements:
    #         if int(input_element.get_attribute('value')) % 2 == 0:
    #             input_element.click()
    #             time.sleep(.3)
    # time.sleep(2)  # делаем паузу для наглядности
    #
    # # находим кнопку class='alert_button'
    # button = browser.find_element(By.CLASS_NAME, 'alert_button')
    #
    # # скроллинг экрана до видимости кнопки
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()  # кликаем кнопку
    # time.sleep(5)  # делаем паузу для наглядности
    #
    # alert = browser.switch_to.alert
    # print(alert.text)
    # time.sleep(5)  # делаем паузу для наглядности

    """Вариант 2 - сразу кликаем по нужным checkbox а потом скроллим"""

    total = 0  # сумма чисел
    last_card_count = 0  # количество карточек перед скроллом

    # находим объект для скроллинга, с id='main_container'
    scrollable_element = browser.find_element(By.ID, 'main_container')

    while True:
        # Получаем карточки заново после каждого скролла
        cards = browser.find_elements(By.CLASS_NAME, 'child_container')

        for i in range(last_card_count, len(cards)):
            # находим теги 'input'
            input_elements = cards[i].find_elements(By.TAG_NAME, 'input')
            for input_element in input_elements:
                if int(input_element.get_attribute('value')) % 2 == 0:
                    input_element.click()
                    time.sleep(.3)

        # Запоминаем количество карточек перед скроллом
        last_card_count = len(cards)

        # Скроллим вниз
        browser.execute_script("arguments[0].scrollBy(0, 600);", scrollable_element)
        time.sleep(1)  # Даём контенту подгрузиться

        # Получаем количество карточек после скролла
        new_card_count = len(browser.find_elements(By.CLASS_NAME, 'child_container'))

        # Если карточек не прибавилось – конец контейнера
        if new_card_count == last_card_count:
            print("Достигнут конец контейнера, скрипт завершён!")
            break  # выходим из цикла

    # находим кнопку class='alert_button'
    button = browser.find_element(By.CLASS_NAME, 'alert_button')

    # скроллинг экрана до видимости кнопки
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()  # кликаем кнопку
    time.sleep(5)  # делаем паузу для наглядности

    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(5)  # делаем паузу для наглядности

