from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.my_account_page import MyAccountPage

class LoginPage(BasePage):
    
    email_field=(By.ID,"i0116")
    password_field=(By.NAME,"passwd")
    login_button=(By.ID,"idSIButton9")
    warning_message =(By.ID,"i0116Error")
    
    
    def __init__(self,driver):
        super().__init__(driver)
        
    def set_email_address(self, email_address):
        self.set(self.email_field,email_address)
        
    def set_password(self, password):
        self.set(self.password_field,password)
    
    def click_login_button(self):
        self.click(self.login_button)
        return MyAccountPage(self.driver)
    
    def log_into_app(self,email,password,login_button):
        self.set_email_address(email)
        self.click_login_button(login_button)
        self.set_password(password)
        self.click_login_button(login_button)
        
    def get_warning_message(self):
        return self.get_text(self.warning_message)