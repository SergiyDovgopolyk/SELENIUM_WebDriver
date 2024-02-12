from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, 'input_value').text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()


button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# # browser.execute_script("alert('Robots at work');")
# # browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
#
# time.sleep(5)
#     # закрываем браузер после всех манипуляций
# browser.quit()
