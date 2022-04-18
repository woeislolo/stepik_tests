from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    SUCCESSFUL_REGISTRATION = (By.CSS_SELECTOR, "#messages .alert-success")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_BOOK = (By.CSS_SELECTOR, '#messages :nth-child(1) strong')
    BOOK_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '#content_inner .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, '.basket_summary')
