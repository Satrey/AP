import datetime
import os

BASE_DIR = "/home/alex/VSCodeProjects/AP/"


class Base:
    """Базовый класс, который содержит универсальные методы"""

    def __init__(self, driver):
        self.driver = driver
        self.products_amount = 6

    """ Метод получает текущий URL """

    def get_current_url(self):
        current_url = self.driver.current_url
        print(f"Текущий URL - {current_url}")
        return current_url

    """ Метод проверки значения текста """

    def assert_word(self, word_locator, result):
        word_value = word_locator.text
        assert word_value == result
        print("Значение тектового поля совпадает с ожидаемым результатом!")

    """ Метод проверки соответствия URL """

    def assert_url(self, result_url):
        assert self.get_current_url() == result_url, (
            "Неудача! URL не совпадает с ожидаемым!"
        )
        print(f"Успешно! Выполнен переход по ожидаемому url: {result_url}")

    """ Метод отбражения времени """

    def print_test_time(begin_text):
        print("\n************************************************")
        print(f"{begin_text} {datetime.datetime.now().time().strftime('%H:%M:%S')} !!!")
        print("************************************************\n")

    """ Метод получения скриншота текущей страницы """

    def get_screenshot(self, filename):
        path = os.path.join(BASE_DIR, "screens", filename)
        print(f"Скриншот сохранен в каталог - {path}")
        self.driver.save_screenshot(path)
