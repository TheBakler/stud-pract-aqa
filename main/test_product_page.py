import pytest

from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import faker



@pytest.mark.old
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_for_test_guest()
    page.should_not_be_success_message()

@pytest.mark.old
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_for_test_guest()
    page.should_disappeared()

@pytest.mark.old
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_click_button_see_basket()
    backet_page = BasketPage(browser, browser.current_url)
    backet_page.should_not_be_product_in_basket()
    backet_page.should_be_text_basket_is_empty()

@pytest.mark.new
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True, scope='function')
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        password = f.password()
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()



    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    # @pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6",
    #                                   pytest.param("7", marks=pytest.mark.xfail),
    #                                   "8", "9"])
    def test_user_can_add_product_to_basket(self, browser):
        # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart_for_test_guest()
        #page.solve_quiz_and_get_code()
        page.product_name_matches_the_one_added()
        page.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()