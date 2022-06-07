import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

EXE_PATH = 'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'
# url = 'http://suninjuly.github.io/math.html'
url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome(EXE_PATH)
    browser.get(url)
    sleep(2)

    x = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute('valuex')

    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # # assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"

    # x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    # x = x_element.text
    y = calc(x)
    label = browser.find_element(By.CSS_SELECTOR, '#answer')
    label.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    sleep(15)
finally:
    browser.quit()