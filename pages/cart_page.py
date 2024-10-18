from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators
    checkout_button = '//button[@id="checkout"]'


    # Getters

    @property
    def get_checkout_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions
    def click_checkout_button(self):
        self.get_checkout_button.click()
        print('Click checkout')

    # Methods

    # подтверждение товара
    def confirm_product(self):
        with allure.step('confirm product'):
            Logger.add_start_step(method='confirm_product')
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self._driver.current_url, method='confirm_product')
