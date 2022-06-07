import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# link = "http://suninjuly.github.io/simple_form_find_task.html"
# link = 'http://suninjuly.github.io/registration1.html'
link = 'http://suninjuly.github.io/registration2.html'
EXE_PATH = r'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get(link)

input1 = driver.find_element(by='tag name',value='input')
input1.send_keys("Ivan")
input2 = driver.find_element(by='name', value='last_name')
input2.send_keys("Petrov")
input3 = driver.find_element(by='class name', value='city')
input3.send_keys("Smolensk")
input4 = driver.find_element(by='id',value='country')
input4.send_keys("Russia")
button = driver.find_element(by='css selector', value="button.btn")
button.click()

time.sleep(10)
driver.quit()

