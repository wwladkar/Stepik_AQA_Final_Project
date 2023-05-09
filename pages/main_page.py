from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR,
                                       "#login_link_invalid"), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def go_to_basket(self):
        btn_go_to_basket = self.browser.find_element(By.CSS_SELECTOR,
                                                     ".btn-group .btn-default:nth-child(1)")
        btn_go_to_basket.click()

