from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '#solve').click()
    time.sleep(15)
finally:
    browser.quit()

