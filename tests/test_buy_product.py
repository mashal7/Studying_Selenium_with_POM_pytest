import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage





def test_buy_product():
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    options = webdriver.ChromeOptions()
    #options.add_experimental_option('detach', True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    print('Start Test')

    login = LoginPage(driver)
    login.authorization()

    catalog = CatalogPage(driver)
    catalog.add_product()
    time.sleep(5)


    # wait = WebDriverWait(driver, 10)
    # select_product = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')))
    # select_product.click()
    # print('click select product')
    #
    # enter_shopping_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
    # enter_shopping_cart.click()
    # print('Click shopping cart')

