from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "form.js-register-form.is-active input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form.js-register-form.is-active input[name='password']")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "form.js-register-form.is-active input[name='password_confirm']")
    CHECKBOX = (By.CSS_SELECTOR, "div.c-checkbox-field__checkmark")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'js-submit-registry')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='l-popup__message-header']")
    CLOSE_POPUP = (By.XPATH, "//div[@class='l-popup__message-close js-close-popup']")

    def enter_email(self, email):
        """Enter email"""
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enter password"""
        self.send_keys(self.PASSWORD_INPUT, password)

    def repeat_password(self, password):
        """Repeat password"""
        self.send_keys(self.PASSWORD_REPEAT, password)

    def check_terms(self):
        """Accept"""
        self.click(self.CHECKBOX)

    def submit_registration(self):
        """Click on registration"""
        self.click(self.SUBMIT_BUTTON)

    def is_registration_successful(self):
        """Check if success popup is visible"""
        return self.is_visible(self.SUCCESS_MESSAGE)

    def close_success_popup(self):
        """Close popup """
        self.click(self.CLOSE_POPUP)