import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage


@pytest.mark.old
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_for_test_guest()
    page.solve_quiz_and_get_code()
    page.product_name_matches_the_one_added()
    page.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

@pytest.mark.old
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_for_test_guest()
    page.should_not_be_success_message()

@pytest.mark.old
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.old
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_for_test_guest()
    page.should_disappeared()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_click_button_see_basket()
    backet_page = BasketPage(browser, browser.current_url)
    backet_page.should_not_be_product_in_basket()
    backet_page.should_be_text_basket_is_empty()


