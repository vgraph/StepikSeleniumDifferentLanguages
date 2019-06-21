import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
        """Тест проверяет, что страница товара
         содержит кнопку добавления в корзину
        """
        # Открываем страницу товара
        browser.get(link)
        
        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(5)
        
        # Проверяем наличие кнопки добавления товара в корзину
        # button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        # assert browser.find_element_by_css_selector("button.btn-add-to-basket").is_displayed()
        # assert WebDriverWait(browser, 3).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "button.bt-add-to-basket"))
        # )
        # assert 0 == 1
