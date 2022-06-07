from selenium import webdriver
from selenium.webdriver.common.by import By
import time


EXE_PATH = r'D:\Рабочий стол\IT Projects\Selenium_automation\chromedriver\chromedriver.exe'


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path=EXE_PATH)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    text_edit_1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    text_edit_1.send_keys('Kirill')

    text_edit_2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    text_edit_2.send_keys('Andreev')

    text_edit_3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    text_edit_3.send_keys('andreevks@mail.ru')

    text_edit_4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    text_edit_4.send_keys('8111111')

    text_edit_5 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']")
    text_edit_5.send_keys('SBb, Dalnevostochniy prospect')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

finally:

    # закрываем браузер после всех манипуляций
    browser.quit()