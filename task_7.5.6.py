import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, закроется после завершения работы
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html') # открываем ссылку
    buttons = browser.find_elements(By.CLASS_NAME, 'timer_button')
    action = ActionChains(browser)  # Создаём экземпляр класса ActionChains

    for button in buttons:
        # скроллинг страницы до видимости элемента button в данном случае для наглядности работы
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        time_pause = float(button.get_attribute('value'))  # получаем значение времени в атрибуте value
        action.click_and_hold(button).perform()  # нажимаем кнопку
        action.pause(time_pause).perform()  # делаем паузу на значение value
        action.release(button).perform()  # отпускаем кнопку

        # action.click_and_hold(button).pause(time_pause).release(button).perform() # все действия в одной строке

    alert = browser.switch_to.alert  # переключаемся на модальное окно
    print(alert.text)
    time.sleep(3)
