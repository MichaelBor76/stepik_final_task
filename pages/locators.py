from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_AFTER_ADD_ITEM = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    TITLE_OF_THE_ITEM = (By.CSS_SELECTOR, "h1")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email"), "Registration email is not presented"
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password1"), "Registration password is not presented"
    REG_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")

class BasketPageLocators(object):
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#content_inner")
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

