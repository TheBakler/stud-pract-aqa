from .base_page import BasePage
from main.locators import MainPageLocators, ProductPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_BUCKET), "Adding in bucket product link is not presented!"

