import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color

options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument("--force-device-scale-factor=0.75")
options_chrome.add_argument("--start-fullscreen")

with webdriver.Chrome(options=options_chrome) as browser: # Инициализация и запуск браузера в конструкции with
    browser.get('https://parsinger.ru/selenium/5.10/4/index.html') # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    actions = ActionChains(browser) # Создаём экземпляр класса ActionChains

    time.sleep(2)

    # находим все элементы которые нужно перенести
    balls = browser.find_elements(By.CLASS_NAME, 'ball_color')
    # balls = browser.find_element(By.CLASS_NAME, 'basket_with_toys').find_elements(By.TAG_NAME, 'div')

    # находим все корзины куда нужно перенести
    baskets = browser.find_elements(By.CLASS_NAME, 'basket_color')


    """Вариант 1 - с использованием Color"""

    # for ball in balls: # перебираем элементы которые нужно перенести

        # получаем цвет элемента который нужно перенести
        # color_ball = Color.from_string(ball.value_of_css_property('background-color')).rgb

        # for basket in baskets: # перебираем элементы куда нужно перенести

            # получаем цвет элемента куда нужно перенести
            # color_basket = Color.from_string(basket.value_of_css_property('background-color')).rgb

            # if color_ball == color_basket: # если цвет одинаковый

                # actions.click_and_hold(ball).move_to_element(basket).release().perform() # переносим элемент
                # break # останавливаем перебор элементов куда нужно перенести


    """Вариант 2 - будем получать цвет из значения атрибута"""

    for ball in balls: # перебираем элементы которые нужно перенести

        # получаем цвет элемента который нужно перенести
        color_ball = ball.get_attribute('class').split()[1].replace('_ball', '')

        for basket in baskets: # перебираем элементы куда нужно перенести

            color_basket = basket.get_attribute('class').split()[1] # получаем цвет элемента куда нужно перенести

            if color_ball == color_basket: # если цвет одинаковый

                actions.click_and_hold(ball).move_to_element(basket).release().perform()
                # actions.drag_and_drop(ball, basket).perform() # переносим элемент
                break # останавливаем перебор элементов куда нужно перенести

    password = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'message'))).text

    print(password)

    time.sleep(5)