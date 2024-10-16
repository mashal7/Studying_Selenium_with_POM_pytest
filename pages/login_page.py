from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        #super().__init__(driver)
        self._driver = driver

    # Locators
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    word_on_catalog_page = '//span[@class="title"]'

    # Getters

    @property
    def get_user_name(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    @property
    def get_password(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.password)))

    @property
    def get_login_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    @property
    def get_word_on_catalog_page(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.word_on_catalog_page)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name.send_keys(user_name)
        print('Input username')

    def input_password(self, password):
        self.get_password.send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button.click()
        print('Click login_button')

    # Methods

    # авторизация в системе
    def authorization(self):

        self._driver.get(self.url)
        #self._driver.maximize_window()
        self.get_current_url()
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()

        self.assert_word(self.get_word_on_catalog_page, 'Products')
