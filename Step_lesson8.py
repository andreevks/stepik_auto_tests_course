from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

url = "http://suninjuly.github.io/file_input.html"
EXE_PATH = r'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome(executable_path=EXE_PATH)
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys('Kirill')
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys('Andreev')
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys('andreevks@mail.ru')
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(15)
finally:
     browser.quit()