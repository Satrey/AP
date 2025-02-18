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
