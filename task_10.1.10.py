import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color

options_chrome = webdriver.ChromeOptions()

# options_chrome.add_argument('--headless')

# options_chrome.add_argument('--window-size=1920,1080')  # запуск с установленным разрешением экрана

# уменьшаем масштаб чтобы были видны все элементы на экране
options_chrome.add_argument("--force-device-scale-factor=0.75")

with webdriver.Chrome(options=options_chrome) as browser:  # Инициализация и запуск браузера в конструкции with

    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')  # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    actions = ActionChains(browser)  # Создаём экземпляр класса ActionChains

    """Вариант 1 - учитывая что исходный элемент и элемент куда нужно 
    перенести находятся в DOM последовательно друг за другом"""

    # находим все элементы с тегом 'div' в элементе с id='main_container'
    # elements = browser.find_element(By.ID, 'main_container').find_elements(By.TAG_NAME, 'div')

    # for i in range(0, len(elements), 2):
    #     element = elements[i] # элемент который нужно перенести

        # target = elements[i+1] #  элемент куда нужно перенести

        # actions.drag_and_drop(element, target).perform()  # Выполняем действие перетаскивания
        # actions.click_and_hold(element).move_to_element(target).release().perform()

    # ожидаем когда элемент с id='message' станет видимым и получаем из него пароль
    # password = wait.until(EC.visibility_of_element_located((By.ID, 'message'))).text

    # print(password)
    # time.sleep(5) # делаем паузу для наглядности

    """Вариант 2 используем zip"""

    # получаем все элементы которые нужно перенести
    # elements = browser.find_elements(By.CLASS_NAME, "draganddrop")

    # получаем все элементы куда нужно перенести
    # targets = browser.find_elements(By.CLASS_NAME, "draganddrop_end")

    # for element, target in zip(elements, targets):

    # переносим элемент
    # actions.click_and_hold(element).move_to_element(target).release().perform()

    # ожидаем когда найдётся текст в элементе id='message'
    # wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')

    # print(browser.find_element(By.ID, 'message').text)

    """Вариант 3 - используем Color для получения значения цвета"""

    # получаем все элементы которые нужно перенести
    elements = browser.find_elements(By.CLASS_NAME, 'draganddrop')

    # получаем все элементы куда нужно перенести
    elements_end = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')

    for element in elements:  # перебираем элементы которые нужно перенести

        # получаем значение цвета из 'background-color'
        element_color = Color.from_string(element.value_of_css_property('background-color')).rgb

        for element_end in elements_end:  # перебираем элементы куда нужно перенести

            # получаем значение цвета из 'border-color'
            element_end_color = Color.from_string(element_end.value_of_css_property('border-color')).rgb

            if element_color == element_end_color:  # если цвета равны

                # переносим элемент
                actions.click_and_hold(element).move_to_element(element_end).release().perform()

                break  # останавливаем перебор элементов куда нужно перенести

    # ожидаем когда элемент с id='message' станет видимым и получаем из него пароль
    password = wait.until(EC.visibility_of_element_located((By.ID, 'message'))).text

    print(password)
    time.sleep(5)  # делаем паузу для наглядности
