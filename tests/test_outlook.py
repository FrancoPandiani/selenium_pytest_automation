import pytest
from selenium import webdriver
from pages.outlook_page import OutlookPage
from config.config import OUTLOOK_EMAIL, OUTLOOK_PASSWORD

@pytest.fixture(scope="module")
def setup_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(setup_teardown):
    driver = setup_teardown
    outlook_page = OutlookPage(driver)

    outlook_page.open()
    
    assert OUTLOOK_EMAIL is not None, "OUTLOOK_EMAIL no está configurado."
    assert OUTLOOK_PASSWORD is not None, "OUTLOOK_PASSWORD no está configurado."

    outlook_page.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
    outlook_page.verify_login_success()

def test_logout(setup_teardown):
    driver = setup_teardown
    outlook_page = OutlookPage(driver)

    outlook_page.open()

    outlook_page.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
    outlook_page.logout()
