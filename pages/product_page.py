from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        btn_add_to_basket.click()

    def check_name_of_product(self):
        name_of_product_on_page = \
            self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ON_PAGE).text
        name_of_product_on_message = \
            self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ON_MESSAGE).text
        assert name_of_product_on_page == name_of_product_on_message, "Name of product not equal"

    def check_price_of_product(self):
        price_of_product = \
            self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_of_basket = \
            self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text
        assert price_of_product == price_of_basket, "Price of product not equal price of basket"



