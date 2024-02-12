import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(3)
    browser.quit()
