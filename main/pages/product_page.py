from .base_page import BasePage
from main.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_for_test_guest(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def should_be_newyear_url(self):
        assert '?promo=newYear' in self.browser.current_url, 'newYear missing from url'

    def product_name_matches_the_one_added(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), 'Message about adding is not presented'
        message = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message, 'There is no such product in the message'

    def the_price_of_the_cart_is_the_same_as_the_price_of_the_product(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), 'Cart value not shown'
        basket_value = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        cost_of_good = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert cost_of_good == basket_value, 'The price of the cart does not match the price of the product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"