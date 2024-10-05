from selenium.webdriver.common.by import By
import time



class TestButton:
    def test_find_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.implicitly_wait(5)
        browser.get(link)
        time.sleep(5)
        assert browser.find_element(By.CSS_SELECTOR, 'a[class="btn btn-default"]'), "Кнопка корзины не найдена"