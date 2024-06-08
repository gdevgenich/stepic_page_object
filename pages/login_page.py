from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"{self.browser.current_url} don't have login in it"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def wait_for_user_icon(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(BasePageLocators.USER_ICON))
