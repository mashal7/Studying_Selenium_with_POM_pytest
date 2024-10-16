from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ClientInfoPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    # Getters

    @property
    def get_first_name(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    @property
    def get_last_name(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    @property
    def get_postal_code(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    @property
    def get_continue_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name.send_keys(first_name)
        print('Input username')

    def input_last_name(self, last_name):
        self.get_last_name.send_keys(last_name)
        print('Input password')

    def input_postal_code(self, postal_code):
        self.get_postal_code.send_keys(postal_code)
        print('Input password')

    def click_continue_button(self):
        self.get_continue_button.click()
        print('Click continue_button')

    # Methods

    # авторизация в системе
    def input_info(self):
        self.input_first_name('Ivan')
        self.input_last_name('Ivanov')
        self.input_postal_code('1234')
        self.click_continue_button()

