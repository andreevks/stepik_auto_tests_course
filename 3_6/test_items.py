from selenium.webdriver.common.by import By
#from time import sleep

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_user_should_see_button_add_basket(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), \
        'Кнопка добавления в корзину не найдена'
    #sleep(15)
    # btn_title = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").text
    # assert btn_title == 'Ajouter au panier', \
    #     f'Надпись не на том языке: {btn_title}'

# команда для запкска
# pytest --language=es test_items.py