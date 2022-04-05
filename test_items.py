import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_can_add_to_cart(browser):
    browser.get(link)
    btn_add_to_cart = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    btn_add_to_cart.click()

    # Если ничего не нашло, вернет пустой массив[]
    label_successful_add_to_cart = browser.find_elements(By.CLASS_NAME, "alertinner")
    assert label_successful_add_to_cart, "Не найден элемент об успешном добавлении"