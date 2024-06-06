import time
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.product_page import ProductPage


@pytest.mark.parametrize("promo", ["0", "1", "2", "3", "4", "5", "6",
                                   pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser: WebDriver, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    expected_price = page.get_price()
    expected_name = page.get_name()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_cart_total(expected_price=expected_price)
    page.check_added_product_name(expected_name=expected_name)


