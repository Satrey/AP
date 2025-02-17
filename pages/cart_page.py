import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):
    """Класс страницы корзины интернет магазина (шаг-1)"""

    # URL тестируемой страницы
    base_url = "https://www.saucedemo.com/checkout-step-one.html"

    # Локаторы спользуемые на странице
    button_checkout = '//button[@id="checkout"]'

    # Геттеры

    # Получение кнопки Checkout
    def get_button_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        checkout_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.button_checkout))
        )
        return checkout_button

    # Метод для олучения списка элементов присутствующих в корзине
    def get_cart_list(self):
        wait = WebDriverWait(self.driver, 10)
        cart_list = wait.until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )
        return cart_list

    # Действия

    def processing_cart(self, items, num: int, text: str):
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

    # Метод для обработки и проверки товаров в корзине

    def products_in_cart(self, num: int):
        inventory_list = self.get_cart_list()
        cart_list = self.processing_cart(inventory_list, num, "checkout")
        print("Товар в корзине - ", cart_list)
        return cart_list

    # Метод поиска и проверки кнопки "checkout" и перехода на страницу оформления
    def buton_checkout_click(self):
        self.get_button_checkout().click()

    def check_url_step_2(self):
        c_url = self.get_current_url
        self.assert_url(c_url, "https://www.saucedemo.com/checkout-step-two.html")

    # Методы
    def checkout(self):
        self.products_in_cart(self.products_amount)
        time.sleep(2)
        self.buton_checkout_click()
        time.sleep(2)
        self.check_url_step_2()
        time.sleep(2)
