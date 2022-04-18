from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        # self.solve_quiz_and_get_code()
        time.sleep(3)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*(ProductPageLocators.ADD_TO_BASKET_BTN)), "Add-to-basket button is not presented"

    def should_be_equal_book_name_and_added_book(self):
        added_book = self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert added_book == book_name, 'Not equal added book and book name'

    def should_be_equal_book_price_and_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert basket_price == book_price, 'Not equal basket price and book price'

    def should_be_disappered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappered, but should be"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
