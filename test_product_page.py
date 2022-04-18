import time
import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


# @pytest.mark.parametrize('promo_offer', ["0", "1",
#                         "3", "4", "5", "6", 
#                         "8", "9",
#                         pytest.param("7", marks=pytest.mark.xfail),
#                         ])
def test_guest_can_add_product_to_basket(browser,
                                        # promo_offer
                                        ):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_be_equal_book_name_and_added_book()
    page.should_be_equal_book_price_and_basket_price()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_view_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_be_disappered_success_message()


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        login_page = LoginPage(browser, self.link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(str(time.time()) + "@fakemail.org", 'Babushka123')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.should_be_equal_book_name_and_added_book()
        page.should_be_equal_book_price_and_basket_price()
