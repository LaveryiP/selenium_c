from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    
    z = int(x)+int(y)
    print(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
