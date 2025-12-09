import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# список id кубиков которые нужно нажать когда они будут видны
ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
               'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I', 'jolHZqD1', 'ZM6Ms3tw',
               '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, закроется после завершения работ
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')  # открываем ссылку

    wait = WebDriverWait(browser, 20)  # устанавливаем явное ожидание

    # вариант 1
    # start = time.time()

    # elements = browser.find_elements(By.CLASS_NAME, 'box')  # находим все элементы class='box'

    # for element in elements:
        # если атрибут id элемента есть в списке ids_to_find
        # if (id := element.get_attribute('id')) in ids_to_find:
            # ожидаем когда элемент станет видимым и кликаем его
            # wait.until(EC.visibility_of_element_located((By.ID, f'{id}'))).click()
        # try:
        #     alert = browser.switch_to.alert  # пробуем переключится на модальное окно
        #     print(alert.text)
        #     time.sleep(1)
        #     break
        # except:  # если окно не открыто продолжаем перебирать элементы
        #     continue
    # end = time.time() # 27.1289484500885

    # вариант 2
    start = time.time()
    for id in ids_to_find:
        # ожидаем когда элемент станет видимым и кликаем его
        wait.until(EC.visibility_of_element_located((By.ID, f'{id}'))).click()

    alert = browser.switch_to.alert  # пробуем переключится на модальное окно
    print(alert.text)
    time.sleep(1)
    end = time.time() # 32.52655386924744

    time.sleep(5)  # делаем паузу для наглядности
    print(end - start)
