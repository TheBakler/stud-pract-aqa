from .base_page import BasePage
from .locators import LoginPageLocators
import random

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "Incorrect url, missing login path!"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form.is_displayed(), "Login form is not displayed"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form.is_displayed(), "Register form is not displayed"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        input_email.clear()
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        input_password.clear()
        input_password.send_keys(password)
        input_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONF_PASSWORD_INPUT)
        input_confirm.clear()
        input_confirm.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PUSH).click()
