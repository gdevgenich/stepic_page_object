from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.CART_ITEMS), \
            "Cart is not empty"

    def check_text(self, expected_text):
        text = self.browser.find_element(*BasketPageLocators.INNER_CONTENT).text
        assert expected_text == text, f"Expected {expected_text} but got {text}"
