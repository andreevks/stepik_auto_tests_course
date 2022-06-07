from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


EXE_PATH = 'D:\Рабочий стол\stepik_auto_tests_course\chromedriver\chromedriver.exe'
url_1 = 'http://suninjuly.github.io/registration1.html'
url_2 = 'http://suninjuly.github.io/registration2.html'

def test_1():
    try:
        browser = webdriver.Chrome(executable_path=EXE_PATH)
        browser.get(url_1)
        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys('Kirill')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys('Andreev')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys('andreevks@mail.ru')
        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_2():
    try:
        browser = webdriver.Chrome(executable_path=EXE_PATH)
        browser.get(url_2)
        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys('Kirill')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys('Andreev')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys('andreevks@mail.ru')
        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    pytest.main()