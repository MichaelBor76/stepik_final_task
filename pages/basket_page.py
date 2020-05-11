from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_link()

    def should_be_basket_link(self):
        # Реализуйте проверку на корректный url адрес
        assert "/basket" in self.browser.current_url, "It isn't basket url"

    def should_be_empty_basket(self): # Проверка на пустую корзину
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Backet isn't empty"

    def should_be_message_empty(self): # Проверка: есть сообщение корзина пуста
        text_message_in_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_IN_BASKET).text
        assert "Your basket is empty" in text_message_in_basket, \
            "The basket not exist the message that basket is empty"

        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text
        assert message == "Your basket is empty. Continue shopping" or message == "Ваша корзина пуста Продолжить покупки", "Message about empty basket incorrect"