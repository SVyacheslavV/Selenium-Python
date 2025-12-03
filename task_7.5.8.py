import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/7/7.5/index.html')  # открываем ссылку

    """Вариант 1 - сначала скроллинг всей страницы до появления всех необходимых элементов"""

    # # находим объект для скроллинга, с id='main_container'
    # scrollable_element = browser.find_element(By.ID, 'container')
    #
    # count = 0  # будем считать количество элементов
    #
    # # скроллинг страницы до конца вниз
    # while count < 100:
    #     browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", scrollable_element)
    #
    #     # считаем количество элементов после прокрутки
    #     count = len(scrollable_element.find_elements(By.CLASS_NAME, 'card'))
    #     time.sleep(.3)
    #     print(f'count: {count}') # вывод для наглядности
    #
    # # скроллинг страницы вверх
    # browser.execute_script("arguments[0].scrollTo(arguments[0].scrollHeight, 0)", scrollable_element)
    # time.sleep(.3)
    #
    # total = 0 # сумма чисел
    #
    # cards = browser.find_elements(By.CLASS_NAME, 'card')
    # print(len(cards))
    # for card in cards:
    #     card.find_element(By.CLASS_NAME, 'like-btn').click()
    #     total += int(card.find_element(By.CLASS_NAME, 'big-number').text)
    #     time.sleep(.3)
    # print(f'Сумма чисел: {total}')

    """Вариант 2 - сразу считаем а потом скроллим"""

    total = 0 # сумма чисел
    last_card_count = 0 # количество карточек перед скроллом

    # находим объект для скроллинга, с id='container'
    scrollable_element = browser.find_element(By.ID, 'container')

    while True:
        # Получаем карточки заново после каждого скролла
        cards = browser.find_elements(By.CLASS_NAME, 'card')

        for i in range(last_card_count, len(cards)):
            cards[i].find_element(By.CLASS_NAME, 'like-btn').click() # Лайкаем только новые карточки
            total += int(cards[i].find_element(By.CLASS_NAME, 'big-number').text) # Считаем числа
            time.sleep(.3)

        # Запоминаем количество карточек перед скроллом
        last_card_count = len(cards)

        # Скроллим вниз
        browser.execute_script("arguments[0].scrollBy(0, 600);", scrollable_element)
        time.sleep(1)  # Даём контенту подгрузиться

        # Получаем количество карточек после скролла
        new_card_count = len(browser.find_elements(By.CLASS_NAME, "card"))

        # Если карточек не прибавилось – конец контейнера
        if new_card_count == last_card_count:
            print("Достигнут конец контейнера, скрипт завершён!")
            break # выходим из цикла

    print(f"Общее число лайков: {total}")
