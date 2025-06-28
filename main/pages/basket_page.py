from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in the basket!"

    def should_be_text_basket_is_empty(self):
        text_inf = self.browser.find_element(*BasketPageLocators.TXT_MSG_EMPTY_BUCKET).text
        empty_text_inf = text_inf.split("Continue shopping")[0].strip()
        assert empty_text_inf == "Your basket is empty.", "Text is not presented!"