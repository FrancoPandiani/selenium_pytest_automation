import pytest
from selenium import webdriver
from pages.outlook_page import OutlookPage
from config.config import Config

@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def outlook_page(setup_teardown):
    driver = setup_teardown
    page = OutlookPage(driver)
    page.open()
    page.login(Config.OUTLOOK_EMAIL, Config.OUTLOOK_PASSWORD)
    yield page  # Permite a las pruebas usar la instancia autenticada

# Test funcional 
def test_login(outlook_page):
    assert Config.OUTLOOK_EMAIL is not None, "El email no está configurado."
    assert Config.OUTLOOK_PASSWORD is not None, "El password no está configurado."
    outlook_page.verify_login_success()

def test_click_nav_menu_button(outlook_page):
    outlook_page.click_nav_menu_button()

