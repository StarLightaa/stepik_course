from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element(By.ID, "button")
finally:
    time.sleep(10)
    browser.quit()