import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class SummaryPage(Base):
    """
    Класс для тестирования страницы оформления заказа (шаг-2),
    проверки стоимости заказа и комиссии
    """

    # Локаторы для поиска элементов на странице 'SummaryPage'
    summary_list_locator = "cart_item"
    summary_tax_label_locator = "summary_tax_label"
    summary_total_locator = "summary_total_label"
    summary_subtotal_locator = "summary_subtotal_label"
    button_finish = "finish"

    # Геттеры

    # Метод для получения списка товаров на странице офформления (шаг-2)
    def get_summary_list(self):
        wait = WebDriverWait(self.driver, 10)
        summary_list = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, self.summary_list_locator)
            )
        )
        return summary_list

    def get_tax(self):
        wait = WebDriverWait(self.driver, 10)
        # Получение значения комиссии
        tax_in_cart = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, self.summary_tax_label_locator)
            )
        )
        return tax_in_cart

    def get_summary_total(self):
        total_in_cart = self.driver.find_element(
            By.CLASS_NAME, self.summary_total_locator
        )
        return total_in_cart

    def get_summary_subtotal(self):
        wait = WebDriverWait(self.driver, 10)
        # Получение общей стоимости товаров в корзине без комиссии
        subtotal_in_cart = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, self.summary_subtotal_locator)
            )
        )
        return subtotal_in_cart

    def get_button_finish(self):
        wait = WebDriverWait(self.driver, 10)
        button_finish = wait.until(
            EC.element_to_be_clickable((By.ID, self.button_finish))
        )
        return button_finish

    def get_button_home_page(self):
        wait = WebDriverWait(self.driver, 10)
        # Нажатие на кнопку возврата на домашнюю страницу
        back_home_page = wait.until(
            EC.element_to_be_clickable((By.ID, "back-to-products"))
        )
        return back_home_page

    # Действия

    # Метод добавления товаров в корзину и проверки товаров находящихся в корзине и summory
    def processing_cart(self, num: int, items, text: str):
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

    # Метод для обработки и проверки товаров на странице оформления (шаг-2)
    def products_in_summary(self, num: int):
        inventory_list = self.get_summary_list()
        summary_list = self.processing_cart(num, inventory_list, "finish")
        print("Проверка итогового списка")
        print("Товар в итоговом списке - ", summary_list)
        return summary_list

    # Метод рассчета общей стоимости товаров в корзине
    def calculate_total(self, items: dict):
        # Рассчет общей стоимости товаров в корзине
        total = self.cart_total(items)
        print(f"Общая стоимость товаров в корзине - {total}")
        return total

    # Метод для получения общей стоимости товаров в корзине
    def calculate_subtotal(self, subtotal_in_cart):
        subtotal = float(subtotal_in_cart.text.split("$")[1])
        print(f"Стоимость товаров без комиссии - {subtotal}")
        return subtotal

    # Метод для получения комиссии
    def calculate_tax(self, tax_in_cart):
        tax = float(tax_in_cart.text.split("$")[1])
        print(f"Комиссия составляет - {tax}")
        return tax

    # Метод получения полной стоимости заказа
    def calculate_summary_total(self, summary_total_in_cart):
        # Получение стоимости товаров включая комиссию
        summary_total = float(summary_total_in_cart.text.split("$")[1])
        print(f"Стоимость товаров включая комиссию составляет - {summary_total}")
        return summary_total

    # Метод для посчета общей стоимости корзины
    def cart_total(self, products: dict):
        cart_total = 0.0
        for price in products.values():
            cart_total += float(price)
        return round(cart_total, 2)

    def click_button_finish(self):
        self.get_button_finish().click()

    def click_button_home_page(self):
        self.get_button_home_page().click()
        print("Нажатие на кнопку возврата на домашнюю страницу!")

    # Проверки состояний

    def assert_total_subtotal(self, total, subtotal):
        # Проверка совпадения значений тотал и субтотал (перенести в асерты)
        # Проверка общей стоимости товаров без комиссии
        assert total == subtotal, (
            "Ошибка!!! Общая стоимость товаров без комиссии не совпадает!"
        )
        print("успешно!!! Общая стоимость товаров без комиссии совпадает!")

    def assert_tax_summary_total(self, total, tax, summary_total):
        # Проверка стоимости товаров включая комиссию
        assert round((total + tax), 2) == summary_total, (
            "Ошибка!!! Общая стоимость товаров включая комиссию не совпадает!"
        )
        print("Успешно!!! Общая стоимость товаров включая комиссию совпадает!")

    # Методы

    def cart_finish(self, products_amount):
        summary_list = self.products_in_summary(products_amount)

        # Расчитываем общую стоимость товаров в корзине без комиссии
        total = self.calculate_total(summary_list)
        subtotal = self.calculate_subtotal(self.get_summary_subtotal())
        # Проверка общей стоимости товаров в корзине без комиссии
        self.assert_total_subtotal(total, subtotal)

        # Получаем значение комиссии
        tax = self.calculate_tax(self.get_tax())
        summary_total = self.calculate_summary_total(self.get_summary_total())
        # Проверка общей стоимости товаров в корзине включая комиссию
        self.assert_tax_summary_total(total, tax, summary_total)

        # Нажатие на кнопку 'Finish'
        self.click_button_finish()
        # Проверка перехода на страницу завершения оформления заказа
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        time.sleep(5)

        # Нажатие на кнопку 'Back to home'
        self.click_button_home_page()
        # Проверка перехода на страницу завершения оформления заказа
        self.assert_url("https://www.saucedemo.com/inventory.html")
        time.sleep(5)
