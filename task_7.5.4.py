import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')

    action = ActionChains(browser)  # Создаём экземпляр класса ActionChains

    total = 0
    list_id = []

    for i in range(1, 6):
        while True:
            span_elements = browser.find_element(
                By.CLASS_NAME, f'scroll-container_{i}').find_elements(By.TAG_NAME, 'span')
            for span_element in span_elements:
                id = span_element.get_attribute('id')
                if id not in list_id:
                    list_id.append(id)
                    total += int(span_element.text)
                    action.click(span_element).key_down(Keys.DOWN).perform()  # в одну строку
            time.sleep(.3)  # делаем паузу для наглядности

            if span_element.get_attribute('class'):
                break
    print(f'Сумма чисел: {total}')
    print(f'Длина списка list_id: {len(list_id)}')
