from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://ya.ru/')
    cookies = browser.get_cookies()
    pprint(cookies)