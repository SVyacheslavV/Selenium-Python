""".find_element()и find_elements()"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL веб-страницы для парсинга
url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
# with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    # browser.get(url)

    # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
    # p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    # Проходимся по списку найденных элементов и выводим их текст
    # for i, p_element in enumerate(p_elements, 1):
    #     print(f"Текст второго p тега в {i}-м div с классом 'text': {p_element.text}")
    #     with open('elements.txt', 'a', encoding='utf-8') as f:  # открываем файл 'elements.txt'
    #         f.write(f"Текст второго p тега в {i}-м div с классом 'text': {p_element.text}\n")  # добавляем строку в файл

# Это можно сделать ещё проще с использованием относительного пути XPATH.

# first_p = div.find_element(By.XPATH, './p[1]')
# third_p = div.find_element(By.XPATH, './p[3]')


# Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
with webdriver.Chrome() as browser:
# Открываем URL
    browser.get(url)
    # Ищем все div с классом 'text'
    divs = browser.find_elements(By.CLASS_NAME, 'text')
    # Проходимся по каждому div
    for i, div in enumerate(divs, 1):
        # Получаем первый и третий теги <p> внутри каждого div
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')
        # Выводим их текст
        print(f"Для div #{i}, первый p: {first_p.text}, третий p: {third_p.text}")
        with open('elements1.txt', 'a', encoding='utf-8') as f:  # открываем файл 'elements.txt'
            f.write(f"Для div #{i}, первый p: {first_p.text}, третий p: {third_p.text}\n")  # добавляем строку в файл