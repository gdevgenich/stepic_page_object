from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    CART_TOTAL_ALERT = (By.CSS_SELECTOR, "#messages .alert-info strong")
    ADDED_PRODUCT_ALERT = (By.CSS_SELECTOR, "#messages .alert-success strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")

