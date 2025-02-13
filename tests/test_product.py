import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_select_product():
    with webdriver.Chrome() as driver:
        print("Start test")

        login_page = LoginPage(driver)
        login_page.autentification()
