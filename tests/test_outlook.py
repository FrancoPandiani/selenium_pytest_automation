import pytest
from selenium import webdriver
from pages.outlook_page import OutlookPage
from config.config import OUTLOOK_EMAIL, OUTLOOK_PASSWORD

@pytest.fixture(scope="module",autouse=True)
def setup_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
@pytest.mark.parametrize("email, password", [(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)])
def test_login(setup_teardown, email, password):
    driver = setup_teardown
    outlook_page = OutlookPage(driver)
    outlook_page.open()

    assert email is not None, "El email no está configurado."
    assert password is not None, "El password no está configurado."

    outlook_page.login(email, password)
    outlook_page.verify_login_success()

"""
def test_button(setup_teardown):
     driver = setup_teardown
     outlook_page = OutlookPage(driver)
     outlook_page.click_button()"""
