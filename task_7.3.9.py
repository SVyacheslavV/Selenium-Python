import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.5/index.html')
    action = ActionChains(browser) # Создаём экземпляр класса ActionChains

    # находим левый элемент с id='scrollable-container-left'
    left_element = browser.find_element(By.ID, 'scrollable-container-left')
    # left_element.click() # кликаем по нему
    # action.key_down(Keys.END, left_element).perform() # прокручиваем вниз элемент

    action.click(left_element).key_down(Keys.END).perform() #  в одну строку
    time.sleep(2) # делаем паузу для наглядности

    # находим левый элемент с id='scrollable-container-right'
    right_element = browser.find_element(By.ID, 'scrollable-container-right')
    # right_element.click() # кликаем по нему
    # action.key_down(Keys.END, right_element).perform() # прокручиваем вниз элемент

    action.click(right_element).key_down(Keys.END).perform()  # в одну строку
    time.sleep(2) # делаем паузу для наглядности

    # находим элемент с id='passwordContainer' (найдёт вместе с текстом "Поздравляем! Ваш пароль:")
    # password = browser.find_element(By.ID, 'passwordContainer')

    # находим элемент по селектору key="access-code" (найдёт только пароль)
    password = browser.find_element(By.CSS_SELECTOR, '[key="access_code"]')

    # скролим страницу вниз до видимости элемента
    browser.execute_script("return arguments[0].scrollIntoView(true);", password)
    time.sleep(2) # делаем паузу для наглядности
    print(password.text)