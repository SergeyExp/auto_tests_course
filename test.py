from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # список вкладок
    list_window = browser.window_handles
    print(list_window)
    # присвоение новой вкладки и переход на нее
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value_1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(value_1)
    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y) 

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as err:
    print(err)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()