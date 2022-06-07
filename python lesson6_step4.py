from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"
EXE_PATH = r'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'

try:
    browser = webdriver.Chrome(executable_path=EXE_PATH)
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Kirill")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Andreev")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Saint-Petersburg")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# не забываем оставить пустую строку в конце файла