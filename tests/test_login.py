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
     assert actual_title == "Cuenta Microsoft" or "Microsoft account"
     
    def test_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.set_email_address("email invalido")
        login_page.click_login_button()
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Escriba una dirección de correo electrónico, un número de teléfono o un nombre Skype válidos.")

     