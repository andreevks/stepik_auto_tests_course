import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

links = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
]

@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nquit browser..")


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area').send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    message = browser.find_element(By.CSS_SELECTOR, 'pre.smart-hints__hint').text
    assert message == 'Correct!', message

# команда для запуска
# pytest -s -v 3_6_3.py