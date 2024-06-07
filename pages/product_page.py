from .base_page import BasePage
from .locators import ProductLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ProductLocators.ADD_TO_CART_BUTTON).click()

    def check_cart_total(self, expected_price):
        total = self.browser.find_element(*ProductLocators.CART_TOTAL_ALERT).text
        assert total == expected_price, f"Expected total {expected_price} but got {total}"

    def check_added_product_name(self, expected_name):
        name = self.browser.find_element(*ProductLocators.ADDED_PRODUCT_ALERT).text
        assert name == expected_name, f"Expected text {expected_name} but got {name}"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductLocators.ADDED_PRODUCT_ALERT), \
            "Success message is presented"

    def success_message_disappear(self):
        assert self.is_disappeared(*ProductLocators.ADDED_PRODUCT_ALERT)

    def get_price(self):
        return self.browser.find_element(*ProductLocators.PRODUCT_PRICE).text

    def get_name(self):
        return self.browser.find_element(*ProductLocators.PRODUCT_NAME).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")