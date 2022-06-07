from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

EXE_PATH = r'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

try:
    driver = webdriver.Chrome(executable_path=EXE_PATH)

    url = 'https://youtube.com'
    driver.get(url)
    # search = driver.find_element_by_class_name('gLFyf gsfi')
    # search = driver.find_element_by_tag_name('input')
    #search = driver.find_element(By.TAG_NAME, 'input')
    # search = driver.find_element(By.CLASS_NAME, 'gLFyf.gsfi')
    # search.send_keys('Найди что-нибудь')
    # search.send_keys(Keys.ENTER)
    # driver.find_elements(By.CLASS_NAME,'gNO89b')[1].click()
    # sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.fullscreen_window()
    sleep(5)
    driver.execute_script("window.scrollTo(0, 2000);")
    # html = driver.find_element_by_tag_name('html')
    # for _ in range(10):
    #     html.send_keys(Keys.END)
    #     sleep(1)
    driver.implicitly_wait(3)
    search = driver.find_element_by_class_name('gLFyf.gsfi')
    search.п
    # button
finally:
    # print(driver.page_source)
    # driver.close()
    driver.quit()
