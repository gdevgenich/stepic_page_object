import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import uuid

@pytest.mark.need_review
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.success_message_disappear()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    cart_page = BasketPage(browser)
    cart_page.basket_is_empty()
    cart_page.check_text("Your basket is empty. Continue shopping")


class TestUserAddToBasketFromProductPage(object):

    browser = None

    @pytest.fixture(scope="function")
    def setup(self, browser: WebDriver):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = uuid.uuid4().hex
        page.register_new_user(email=email, password=password)
        page.wait_for_user_icon()

    def test_user_cant_see_success_message(self, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(self.browser, link)
        page.open()
        expected_price = page.get_price()
        expected_name = page.get_name()
        page.add_to_cart()
        page.check_cart_total(expected_price=expected_price)
        page.check_added_product_name(expected_name=expected_name)



