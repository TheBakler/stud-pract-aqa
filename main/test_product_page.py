from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('num_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, num_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_current_name_matches_name_alert()
    page.should_be_product_current_price_matches_price_alert()
