from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")
    # browser.get("https://suninjuly.github.io/selects1.html")
    num1 = browser.find_element(By.ID, 'num1')
    x = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    y = num2.text
    suma = int(x) + int(y)
    print(suma)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(suma))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
