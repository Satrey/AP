import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MarketPage(Base):
    """Класс главной страницы интернет магазина"""

    # URL тестируемой страницы
    base_url = "https://www.saucedemo.com/inventory.html"

    # Локаторы используемые на странице
    button_cart = '//*[@id="shopping_cart_container"]/a'
    button_cart_bage = '//*[@id="shopping_cart_container"]/a'

    # Геттеры
    def get_button_cart(self):
        print("Получение локатора кнопки перехода в корзину")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cart))
        )

    def get_button_cart_bage(self):
        print("Получение значения бэйджа с количеством товара у кнопки корзина")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cart_bage))
        )

    def get_inventory_list(self):
        print("Получение списка элементов на главной странице магазина")
        inventory_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        return inventory_list

    def get_burger_button(self):
        wait = WebDriverWait(self.driver, 20)
        bm_button = wait.until(
            (EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        )
        return bm_button

    def get_burger_logout_link(self):
        wait = WebDriverWait(self.driver, 20)
        logout_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))
        )
        return logout_link

    # Действия
    def processing_cart(self, items, num: int, text: str):
        print("Обработка корзины")
        item_list = {}
        for i, item in enumerate(items, start=1):
            if i <= num:
                product_name = item.find_element(By.CLASS_NAME, "inventory_item_name")
                product_price = item.find_element(By.CLASS_NAME, "inventory_item_price")
                if text == "Add to cart":
                    item.find_element(By.TAG_NAME, "button").click()
                    print(
                        f"Добавили товар {product_name.text} с ценой {product_price.text} в корзину"
                    )
                    item_list[product_name.text] = product_price.text.strip("$")
                else:
                    item_list[product_name.text] = product_price.text.strip("$")
                    print(
                        f"Добавили товар {product_name.text} с ценой {product_price.text} в список"
                    )
        return item_list

    def add_to_cart(self, num: int):
        inventory_list = self.get_inventory_list()
        items_list = self.processing_cart(inventory_list, num, "Add to cart")
        print("Товар добавлен в корзину - ", items_list)
        return items_list

    def button_cart_click(self):
        self.get_button_cart().click()
        print("Нажатие на кнопку перехода в корзину!")

    def burger_button_click(self):
        print("Нажатие на кнопку ")
        self.get_burger_button().click()

    def burger_logout_link_click(self):
        self.get_burger_logout_link().click()

    # Методы
    def add_products_to_cart(self, products_amount):
        self.add_to_cart(products_amount)
        time.sleep(2)
        self.button_cart_click()
        time.sleep(2)
        self.assert_url("https://www.saucedemo.com/cart.html")
        time.sleep(2)

        # Выход пользователя из магазина

    def log_out(self):
        if self.get_current_url() == "https://www.saucedemo.com/inventory.html":
            print("Успешно!!! Пользователь находится в магазине")
            self.burger_button_click()
            print("Нажатие на кнопку меню!")
            time.sleep(2)
            self.burger_logout_link_click()
            print("Нажатие на пункт меню 'Logout'!")
            self.assert_url("https://www.saucedemo.com/")
