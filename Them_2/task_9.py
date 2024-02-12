import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(3)
    browser.quit()
