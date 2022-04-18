from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty, but should be"
