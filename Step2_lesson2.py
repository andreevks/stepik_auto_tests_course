from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/file_input.html"
EXE_PATH = r'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'


try:
    browser = webdriver.Chrome(executable_path=EXE_PATH)
    browser.get(url)

    # x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    # y = calc(x)
    # browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(y))
    # button = browser.find_element(By.TAG_NAME, 'button')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    # browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    # button.click()
    # time.sleep(15)
finally:
     browser.quit()


# try:
#     browser = webdriver.Chrome(executable_path=EXE_PATH)
#     browser.get(url)
#     num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
#     operation = browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap:nth-child(3)').text
#     num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
#     result = eval(f'{num1} {operation} {num2}')
#     select = Select(browser.find_element(By.TAG_NAME, 'select'))
#     select.select_by_value(str(result))
#     browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default').click()
#     time.sleep(15)
# finally:
#     browser.quit()



