import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.4.1/index.html')
    action = ActionChains(browser)
    element = browser.find_element(By.CLASS_NAME, 'long-page')
    # прокручиваем страницу на 1000px
    ActionChains(browser).move_to_element(element).scroll_by_amount(1, 1000).perform()
    time.sleep(4) # делаем паузу для ожидания отсчёта таймера

    # получаем пароль из элемента class='countdown'
    password = browser.find_element(By.CLASS_NAME, 'countdown').text.split()[-1]
    print(password)
    time.sleep(3) # делаем паузу для наглядности

    # прокручиваем страницу на 1000px
    ActionChains(browser).move_to_element(element).scroll_by_amount(1, 1100).perform()
    time.sleep(3) # делаем паузу для наглядности

    # находим элемент с тегом 'input' и вставляем в него пароль
    # browser.find_element(By.TAG_NAME, 'input').send_keys(password)

    # вариант нахождения элемента по селектору placeholder="Введите код"
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Введите код"]').send_keys(password)
    time.sleep(3) # делаем паузу для наглядности

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)  # делаем паузу для наглядности
    answer = browser.find_element(By.ID, 'final-key').text
    print(answer.split()[-1])
    time.sleep(3)  # делаем паузу для наглядности