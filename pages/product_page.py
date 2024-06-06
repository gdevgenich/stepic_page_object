from .base_page import BasePage
from .locators import ProductLocators
import math


class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ProductLocators.ADD_TO_CART_BUTTON).click()

    def check_cart_total(self, expected_total):
        total = self.browser.find_element(*ProductLocators.CART_TOTAL_ALERT).text
        assert total == expected_total, f"Expected total {expected_total} but got {total}"

    def check_added_product_name(self, expected_name):
        name = self.browser.find_element(*ProductLocators.ADDED_PRODUCT_ALERT).text
        assert name == expected_name, f"Expected total {expected_name} but got {name}"

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