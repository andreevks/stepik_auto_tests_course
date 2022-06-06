import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EXE_PATH = 'D:\Рабочий стол\Selenium_project\chromedriver\chromedriver.exe'


class test_class_name(unittest.TestCase):
    def test_1(self):
        url_1 = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome(executable_path=EXE_PATH)
        browser.get(url_1)
        # Заполняем поля
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys('Kirill')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys('Andreev')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys('andreevks@mail.ru')
        time.sleep(1)
        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # находим элемент, содержащий текст и
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "test_1 not passed")

    def test_2(self):
        url_2 = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome(executable_path=EXE_PATH)
        browser.get(url_2)
        # Заполняем поля
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys('Kirill')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys('Andreev')
        browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys('andreevks@mail.ru')
        time.sleep(1)
        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # находим элемент, содержащий текст и
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "test_1 not passed")


if __name__ == "__main__":
    unittest.main()
