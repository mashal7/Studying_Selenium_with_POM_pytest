import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage


#@pytest.mark.run(order=2)
def test_buy_product1(set_group, set_up):
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    options = webdriver.ChromeOptions()
    #options.add_experimental_option('detach', True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    print('Start Test 1')

    # авторизация
    login = LoginPage(driver)
    login.authorization()

    # выбор товара
    catalog = CatalogPage(driver)
    catalog.add_product1()

    # действия в корзине
    cart = CartPage(driver)
    cart.confirm_product()

    # оформление заказа
    client_info = ClientInfoPage(driver)
    client_info.input_info()

    payment = PaymentPage(driver)
    payment.do_payment()

    finish_page = FinishPage(driver)
    finish_page.finish()

    time.sleep(4)

#@pytest.mark.run(order=3)
def test_buy_product2(set_up):
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    options = webdriver.ChromeOptions()
    #options.add_experimental_option('detach', True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    print('Start Test 2')

    # авторизация
    login = LoginPage(driver)
    login.authorization()

    # выбор товара
    catalog = CatalogPage(driver)
    catalog.add_product2()

    # действия в корзине
    cart = CartPage(driver)
    cart.confirm_product()

    time.sleep(4)

#@pytest.mark.run(order=1)
def test_buy_product3(set_up, set_group):
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    options = webdriver.ChromeOptions()
    #options.add_experimental_option('detach', True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    print('Start Test 3')

    # авторизация
    login = LoginPage(driver)
    login.authorization()

    # выбор товара
    catalog = CatalogPage(driver)
    catalog.add_product3()

    # действия в корзине
    cart = CartPage(driver)
    cart.confirm_product()

    time.sleep(4)