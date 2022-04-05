from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    valuex = x_element.text

    y = calc(valuex)
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    btnSubmit = browser.find_element(By.ID, "solve")
    btnSubmit.click()
finally:
    time.sleep(5)
    browser.quit()
