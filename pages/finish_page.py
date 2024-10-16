from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class FinishPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators

    # Getters

    # Actions


    # Methods
    # выбор товара
    def finish(self):
        self.get_current_url()
        self.get_screenshot()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')