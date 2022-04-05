from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    # Ваш код, который заполняет обязательные поля
    #required_elements = browser.find_elements_by_css_selector('input[required]')
    #for element in required_elements:
    #    element.send_keys('required')

    required_block = browser.find_element(By.CLASS_NAME, "first_block")
    input1 = required_block.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    input2.send_keys("Ivanov")
    input3 = required_block.find_element(By.CLASS_NAME, "third")
    input3.send_keys("ivan@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
