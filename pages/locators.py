from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT_ON_PAGE = (By.CSS_SELECTOR, ".breadcrumb > .active")
    NAME_OF_PRODUCT_ON_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] .price_color")
    PRICE_OF_BASKET = (By.CSS_SELECTOR, "#messages div:nth-of-type(3) strong")

