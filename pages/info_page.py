import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class InfoPage(Base):
    """Класс страницы корзины интернет магазина (шаг-1)"""

    # URL тестируемой страницы
    base_url = "https://www.saucedemo.com/checkout-step-one.html"

    # Локаторы спользуемые на странице
    first_name_locator = '//input[@id="first-name"]'
    last_name_locator = '//input[@id="last-name"]'
    zip_code_locator = '//input[@id="postal-code"]'
    button_continue = '//input[@id="continue"]'

    # Геттеры

    # Получение поля first_name
    def get_first_name_field(self):
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.first_name_locator))
        )
        return first_name_field

    # Получение поля last_name
    def get_last_name_field(self):
        wait = WebDriverWait(self.driver, 10)
        last_name_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.last_name_locator))
        )
        return last_name_field

    # Получение поля zip_code
    def get_zip_code_field(self):
        wait = WebDriverWait(self.driver, 10)
        zip_code_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.zip_code_locator))
        )
        return zip_code_field

    # Получение кнопки Continue
    def get_button_continue(self):
        wait = WebDriverWait(self.driver, 10)
        zip_code_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.button_continue))
        )
        return zip_code_field

    # Действия

    # Заполнение поля имя формы оформления заказа
    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)
        print("Заполнение поля 'имя' формы выполнено успешно!!!")

    # Заполнение поля фамилия формы оформления заказа
    def input_last_name(self, last_name):
        self.get_last_name_field().send_keys(last_name)
        print("Заполнение поля 'фамилия' формы выполнено успешно!!!")

    # Заполнение поля почтовый индекс формы оформления заказа
    def input_zip_code(self, zip_code):
        self.get_zip_code_field().send_keys(zip_code)
        print("Заполнение поля 'почтовый индекс' формы выполнено успешно!!!")

    # Нажатие на кнопку Continue
    def button_continue_click(self):
        self.get_button_continue().click()
        print("Нажатие на кнопку Continue выполнено!")

    # Проверка перехода на страницу оформления заказа (шаг-2)
    def check_url_step_2(self):
        c_url = self.get_current_url()
        print(c_url)
        self.assert_url("https://www.saucedemo.com/checkout-step-two.html")

    # Методы
    def set_user_info(self, first_name, last_name, zip_code):
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_zip_code(zip_code)
        self.button_continue_click()
        time.sleep(2)
        self.check_url_step_2()
        time.sleep(2)
        self.get_screenshot("info_page.png")
