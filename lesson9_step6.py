from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    y = str(math.log(abs(12*math.sin(int(x)))))
    
    print(y)

    element = browser.find_element(By.TAG_NAME, "input")
    element.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
