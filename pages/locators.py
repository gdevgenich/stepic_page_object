from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.PARTIAL_LINK_TEXT, "basket")


class MainPageLocators(object):
    pass


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    CART_TOTAL_ALERT = (By.CSS_SELECTOR, "#messages .alert-info strong")
    ADDED_PRODUCT_ALERT = (By.CSS_SELECTOR, "#messages .alert-success strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")


class BasketPageLocators(object):
    INNER_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
    CART_ITEMS = (By.ID, "basket_formset")

