from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    KONTO_BUTTON=(By.ID, "header-account")

    def click_konto(self):
        self.click(self.KONTO_BUTTON)

    REGISTER_BUTTON = (By.XPATH, "//div[normalize-space(text())='Zarejestruj się']")

    def click_register(self):
        self.click(self.REGISTER_BUTTON)