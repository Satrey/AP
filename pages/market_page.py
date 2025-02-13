import time

# from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MarketPage(Base):
    """Класс главной страницы интернет магазина"""

    # URL тестируемой страницы
    base_url = "https://www.saucedemo.com/inventory.html"

    # Локаторы спользуемые на странице
    button_add_to_cart = ""
    button_cart = '//*[@id="shopping_cart_container"]/a'
    button_cart_bage = '//*[@id="shopping_cart_container"]/a'

    # Геттеры
    def get_button_cart(self):
        print("Получение локатора кнопки перехода в корзину")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.button_cart))
        )

    def get_button_cart_bage(self):
        print("Получение значения бэйджа с количеством товара у кнопки корзина")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.button_cart_bage))
        )

    def get_buton_add_to_cart(self):
        print("Получение локатора кнопки добавления товара в корзину")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.button_add_to_cart))
        )

    # Действия
    def input_user_name(self, user_name):
        self.get_input_login().send_keys(user_name)
        print("Ввод имени пользователя в поле Login")

    def input_password(self, password):
        self.get_input_password().send_keys(password)
        print("Ввод пароля в поле Password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Клик на кнопке Login")

    # Метод не используется в классе, оставлен для примера секции, удалить
    # после появления методов класса.
    # Методы
    def autentification(self):
        print("Запуск метода аутентификации пользователя")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()

        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_cart_word(), "Products")

        time.sleep(5)
