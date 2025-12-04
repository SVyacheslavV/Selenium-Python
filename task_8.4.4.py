from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/8/8.4.1/') # открываем ссылку

    iframe_element = browser.find_element(By.TAG_NAME, 'iframe') # находим фрейм
    browser.switch_to.frame(iframe_element) # переключаемся на фрейм
    text = browser.page_source # получаем текст из фрейма
    word = ''
    for i in range(len(text)):
        if text[i-1] == '*' and text[i+1] == '*': # ищем *буква*
            word += text[i]
    print(word)