class Base:
    """Базовый класс, который содержит универсальные методы"""

    def __init__(self, driver):
        self.driver = driver

    """ Метод получает текущий URL """

    def get_current_url(self):
        current_url = self.driver.current_url
        print(f"Текущий URL - {current_url}")

    """ Метод проверки значения текста """

    def assert_word(self, word_locator, result):
        word_value = word_locator.text
        assert word_value == result
        print("Значение тектового поля совпадает")

    """ Метод проверки соответствия URL """

    def assert_url(self, current_url, result_url):
        assert current_url == result_url, "Неудача! URL не совпадает с ожидаемым!"
        print(f"Успешно! Выполнен переход по ожидаемому url: {current_url}")
