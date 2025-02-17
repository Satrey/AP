# import time

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.market_page import MarketPage


def test_select_product():
    with webdriver.Chrome() as driver:
        print("Start test")
        login_page = LoginPage(driver)
        login_page.autentification()


def test_add_product_to_cart():
    with webdriver.Chrome() as driver:
        login_page = LoginPage(driver)
        market_page = MarketPage(driver)
        login_page.autentification()
        market_page.add_products_to_cart()


def test_cart_step_1():
    with webdriver.Chrome() as driver:
        login_page = LoginPage(driver)
        market_page = MarketPage(driver)
        cart_step_1_page = CartPage(driver)
        login_page.autentification()
        market_page.add_products_to_cart()
        cart_step_1_page.checkout()
