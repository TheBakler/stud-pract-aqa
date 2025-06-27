from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")  # кнопка добавления продукта в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")  # название продукта
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")  # цена продукта
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")  # цена продукта в алерте
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR,
                          ".alert-safe:nth-of-type(1) .alertinner strong")  # название продукта в алерте
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")



class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CLASS_NAME, "icon-user")
    BTN_VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group>a.btn-default")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items .row")
    TXT_MSG_EMPTY_BUCKET = (By.CSS_SELECTOR, "#content_inner>p")
