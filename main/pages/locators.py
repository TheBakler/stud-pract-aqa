from selenium.webdriver.common.by import By

from main.pages.base_page import BasePage


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(BasePage):
    FORM_LOG_ON = (By.ID, "login_form")
    FORM_SIGN_IN = (By.ID, "register_form")
