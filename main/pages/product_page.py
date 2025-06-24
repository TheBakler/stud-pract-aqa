from main.pages.base_page import BasePage
from main.pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def adding_to_basket(self):
        btn_product = self.browser.find_element(*ProductPageLocators.BTN_ADD_BUCKET)
        btn_product.click()

    def should_be_product_link(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_BUCKET), "Adding in bucket product link is not presented!"

    def should_be_product_current_name_matches_name_alert(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Name product is not presented!"
        assert self.is_element_present(*ProductPageLocators.ALERT_NAME_PRODUCT), "Alert name product is not presented!"
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT).text
        assert name in alert_name, "Alert name and product name do not match!"

    def should_be_product_current_price_matches_price_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Price is not presented!"
        assert self.is_element_present(*ProductPageLocators.ALERT_PRICE_PRODUCT), "Alert price is not presented!"
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_PRODUCT).text
        assert price in alert_price, "Alert price and product price do not match!"
