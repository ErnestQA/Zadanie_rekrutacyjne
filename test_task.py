from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://demo.sellingo.pl")

KONTO_BUTTON=wait.until(EC.element_to_be_clickable((By.ID, "header-account")))
KONTO_BUTTON.click()
TEXT_MOJE_KONTO = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Moje konto']")))

ZAREJESTRUJ_SIE=wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space(text())='Zarejestruj się']")))
ZAREJESTRUJ_SIE.click()

FIELD_MOJE_KONTO=wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='l-modal-aside__body \
l-modal-aside__body--padding l-modal-aside__body--scrollable']")))
FIELD_MOJE_KONTO.click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form.js-register-form.is-active")))

EMAIL_INPUT = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form.js-register-form.is-active input[name='email']")))
#EMAIL_INPUT = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
EMAIL_INPUT.send_keys("yifedod537@litepax.com")

PASSWORD_INPUT = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form.js-register-form.is-active input[name='password']")))
PASSWORD_INPUT.send_keys("123QWe!@#")

PASSWORD_REPEAT = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form.js-register-form.is-active input[name='password_confirm']")))
PASSWORD_REPEAT.send_keys("123QWe!@#")

CHECKBOX = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.c-checkbox-field__checkmark")))
CHECKBOX.click()

ZAREJESTRUJ_BUTTON=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and \
contains(@class, 'c-button c-button--full-width m-entry-form-1__button js-submit-registry at-aside-register-submit')]")))
ZAREJESTRUJ_BUTTON.click()

MODIMO_MESSEGE=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='l-popup__message-header']")))
assert MODIMO_MESSEGE.is_displayed(),"Jestesz zalogowany"

CLOSE_POPUP = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='l-popup__message-close at-message-close js-close-popup']")))
CLOSE_POPUP.click()

KONTO_BUTTON=wait.until(EC.element_to_be_clickable((By.ID, "header-account")))
KONTO_BUTTON.click()

WYLOGUJ_BUTTON = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Wyloguj się']")))
WYLOGUJ_BUTTON.click()

MODIMO_TEXT=wait.until(EC.presence_of_element_located((By.XPATH, "//img[@class='m-header-3__logo-image js-shop-logo']")))
assert MODIMO_TEXT.is_displayed(), "Nie wylogowaw się"
print("Jestesz wylogowany")
driver.quit()


