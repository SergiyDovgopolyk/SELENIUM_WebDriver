import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("John")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Doe")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("johnd@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
