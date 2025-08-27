import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

@pytest.mark.regression
def test_registration(driver):
    # Initialize page objects
    home_page = HomePage(driver)
    registration_page = RegistrationPage(driver)

    # Open the website
    driver.get("https://demo.sellingo.pl")

    # Go to account section
    home_page.click_konto()
    home_page.click_register()

    # Fill in the registration form
    registration_page.enter_email("wihakas517@litepax.com")
    registration_page.enter_password("123QWe!@#")
    registration_page.repeat_password("123QWe!@#")
    registration_page.check_terms()
    registration_page.submit_registration()

    # Verify registration success
    assert registration_page.is_registration_successful(), "Registration popup did not appear"
    registration_page.close_success_popup()

    # Logout from account
    home_page.click_konto()

    # Verify logout
    assert home_page.is_visible(home_page.KONTO_BUTTON), "Logout failed"