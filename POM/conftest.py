import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options=Options()
    options.add_argument("--window-size=1920,1080")
    driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()
