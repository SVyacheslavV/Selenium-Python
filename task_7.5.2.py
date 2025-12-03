import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    total = 0

    while True:
        span_tags = browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')
        for span_tag in span_tags:
            input_tag = span_tag.find_element(By.TAG_NAME, 'input')
            id = span_tag.get_attribute('id')
            if id not in list_input:
                list_input.append(id)
                total += int(span_tag.text)
                input_tag.click()
                time.sleep(.3)
                browser.execute_script("return arguments[0].scrollIntoView(true);", span_tag)
                # input_tag.send_keys(Keys.DOWN)
        if span_tag.get_attribute('class'):
            break
    print(total)
    print(list_input)



