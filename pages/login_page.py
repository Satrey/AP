import time

# from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    """Класс для аутентификации пользователя в интернет магазине"""

    # URL тестируемой страницы
    base_url = "https://www.saucedemo.com/"

    # Локаторы спользуемые на странице
    login = "user-name"
    password = "password"
    login_button = "login-button"
    word_locator = "//span[@class='title']"

    # Геттеры
    def get_input_login(self):
        print("Получение локатора логина")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.login))
        )

    def get_input_password(self):
        print("Получение локатора пароля")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.password))
        )

    def get_login_button(self):
        print("Получение локатора кнопки")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.login_button))
        )

    def get_cart_word(self):
        print("Получение локатора текстового поля")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.word_locator))
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
