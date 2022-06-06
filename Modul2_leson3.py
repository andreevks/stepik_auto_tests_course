from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

EXE_PATH = 'D:\Рабочий стол\Selenium_project\chromedriver\chromedriver.exe'
url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome(executable_path=EXE_PATH)
    browser.get(url)
   #price = browser.find_element(By.ID, "price")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, "book").click()
    # browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '#solve').click()
    time.sleep(15)
finally:
    browser.quit()

