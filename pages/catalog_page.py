from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CatalogPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators
    add_product1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'


    # Getters

    @property
    def get_add_product1(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.add_product1)))

    @property
    def get_cart (self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions
    def click_add_product1(self):
        self.get_add_product1.click()
        print('Click add_product1')

    def click_cart(self):
        self.get_cart.click()
        print('Click cart')


    # Methods

    # выбор товара
    def add_product(self):
        self.get_current_url()
        self.click_add_product1()
        self.click_cart()
