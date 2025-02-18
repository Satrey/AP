from selenium import webdriver

from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.login_page import LoginPage
from pages.market_page import MarketPage
from pages.summary_page import SummaryPage


def test_base_functionality():
    # Количество добавляемых товаров в корзину
    products_amount = 2

    # Данные для аутентификации пользователя
    login = "standard_user"
    password = "secret_sauce"

    # Данные для заполнения информации о покупателе
    first_name = "Alex"
    last_name = "Pokrashenko"
    zip_code = 625034

    with webdriver.Chrome() as driver:
        # Экземпляры классов страниц
        login_page = LoginPage(driver)
        market_page = MarketPage(driver)
        cart_page = CartPage(driver)
        info_page = InfoPage(driver)
        summary_page = SummaryPage(driver)

        # Тесткейс
        login_page.autentification(login, password)
        market_page.add_products_to_cart(products_amount)
        cart_page.checkout(products_amount)
        info_page.set_user_info(first_name, last_name, zip_code)
        summary_page.cart_finish(products_amount)
