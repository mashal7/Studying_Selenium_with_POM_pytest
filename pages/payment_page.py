from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class PaymentPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators
    finish_button = '//button[@id="finish"]'

    # Getters

    @property
    def get_finish_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))


    # Actions
    def click_finish_button(self):
        self.get_finish_button.click()
        print('Click add_product1')


    # Methods

    # выбор товара
    def do_payment(self):
        with allure.step('do payment'):
            Logger.add_start_step(method='do_payment')
            self.get_current_url()
            self.click_finish_button()
            Logger.add_end_step(url=self._driver.current_url, method='do_payment')
