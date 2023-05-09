from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")
