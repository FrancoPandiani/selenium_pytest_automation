from pages.login_page import LoginPage
from tests.base_test import BaseTest
from config.config import Config

class TestLogin(BaseTest):
    
    def test_valid_credentials(self):
     loging_page = LoginPage(self.driver)
     loging_page.set_email_address(Config.OUTLOOK_EMAIL)
     loging_page.click_login_button()
     loging_page.set_password(Config.OUTLOOK_PASSWORD)
     loging_page.click_login_button()
     actual_title = loging_page.get_title()
     assert actual_title == " Cuenta Microsoft" or "Microsoft account"
     
"""
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
    """
