import time

from selenium.webdriver.remote.webdriver import WebDriver
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_cart_total(expected_total="£9.99")
    page.check_added_product_name(expected_name="The shellcoder's handbook")


