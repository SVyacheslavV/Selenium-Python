import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--force-device-scale-factor=0.75")
# options_chrome.add_argument('--headless')
# options_chrome.add_argument("--start-fullscreen")


with webdriver.Chrome(options=options_chrome) as browser:  # Инициализация и запуск браузера в конструкции with
    browser.get('https://parsinger.ru/draganddrop/4/index.html')  # Открываем страницу

    wait = WebDriverWait(browser, 15)  # устанавливаем явное ожидание

    actions = ActionChains(browser)  # Создаём экземпляр класса ActionChains

    time.sleep(2)  # делаем паузу для загрузки страницы

    # получаем слово из элемента с id='target-word'
    word = browser.find_element(By.ID, 'target-word').text

    # получаем все буквы алфавита
    alphabet = browser.find_elements(By.CLASS_NAME, 'draggable-letter')

    # элементы куда будем вставлять буквы
    target = browser.find_elements(By.CLASS_NAME, 'letter-slot')

    for ind, letter_word in enumerate(word):  # перебираем буквы слова
        for letter in alphabet:  # перебираем алфавит
            if letter_word == letter.text:  # если буква слова совпала с буквой алфавита

                # переносим букву алфавита в элемент с таким же индексом как у буквы слова
                # actions.drag_and_drop(letter, target[ind]).perform() # переносим элемент
                actions.click_and_hold(letter).move_to_element(target[ind]).release().perform()

    # ожидаем появления пароля в элементе с id='password'
    password = wait.until(EC.visibility_of_element_located((By.ID, 'password')))

    # скролим окно до видимости пароля на экране
    browser.execute_script("return arguments[0].scrollIntoView(true);", password)

    print(password.text)

    time.sleep(2)  # делаем паузу для наглядности
