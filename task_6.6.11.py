import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from task_data import cookies


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.6/1/index.html') # открываем страницу
    age_res = 100
    skills_res = 0
    cookie_res = {}

    for cookie in cookies:
        browser.add_cookie(cookie) # добавляем cookie
        browser.refresh() # Обновляем страницу
        age = int(browser.find_element(By.ID, 'age').text.split()[-1]) # получаем возраст
        skills = len(browser.find_elements(By.TAG_NAME, 'li')) # получаем количество навыков
        if age < age_res and skills > skills_res:
            age_res = age
            skills_res = skills
            cookie_res = cookie
        browser.delete_all_cookies() # Удаление всех cookies
    print(f'Самый молодой и опытный: {cookie_res['value']}') # выводим на экран значение 'value'

    browser.add_cookie(cookie_res) # добавляем cookie для наглядности
    browser.refresh() # Обновляем страницу
    cookies = browser.get_cookies()
    print(cookies[0]['value'])

    time.sleep(5) # делаем паузу для наглядности работы кода
