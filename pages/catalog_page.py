import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class CatalogPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators
    button_add_product1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    button_add_product2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    button_add_product3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//div[@id="shopping_cart_container"]'


    # Getters

    @property
    def get_add_product1(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_add_product1)))

    @property
    def get_add_product2(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_add_product2)))

    @property
    def get_add_product3(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_add_product3)))

    @property
    def get_cart (self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions
    def click_add_product1(self):
        self.get_add_product1.click()
        print('Click add_product1')

    def click_add_product2(self):
        self.get_add_product2.click()
        print('Click add_product2')

    def click_add_product3(self):
        self.get_add_product3.click()
        print('Click add_product3')

    def click_cart(self):
        self.get_cart.click()
        print('Click cart')


    # Methods

    # выбор товара
    def add_product1(self):
        with allure.step('add product1'):
            Logger.add_start_step(method='add_product1')
            self.get_current_url()
            self.click_add_product1()
            self.click_cart()
            Logger.add_end_step(url=self._driver.current_url, method='add_product1')

        def add_product2(self):
            self.get_current_url()
            self.click_add_product2()
            self.click_cart()

        def add_product3(self):
            self.get_current_url()
            self.click_add_product3()
            self.click_cart()