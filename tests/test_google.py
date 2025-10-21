import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.google_page import GooglePage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(driver):
    google = GooglePage(driver)
    google.open()
    google.search("Selenium Python")
    assert "Selenium" in driver.title
