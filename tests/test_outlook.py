import pytest
from selenium import webdriver
from pages.outlook_page import OutlookPage
from config.config import OUTLOOK_EMAIL, OUTLOOK_PASSWORD

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
    page.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
    yield page  # Permite a las pruebas usar la instancia autenticada
    # No es necesario cerrar el driver, ya que lo manejamos en setup_teardown

def test_login(outlook_page):
    assert OUTLOOK_EMAIL is not None, "El email no está configurado."
    assert OUTLOOK_PASSWORD is not None, "El password no está configurado."
    outlook_page.verify_login_success()

def test_click_nav_menu_button(outlook_page):
    outlook_page.click_nav_menu_button()

"""
def test_button(setup_teardown):
     driver = setup_teardown
     outlook_page = OutlookPage(driver)
     outlook_page.click_button()"""
