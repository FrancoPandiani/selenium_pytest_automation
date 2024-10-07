from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from pages.my_account_page import MyAccountPage

class LoginPage(BasePage):
    
    email_field=(By.ID,"i0116")
    password_field=(By.NAME,"passwd")
    login_button=(By.ID, "idSIButton9")
    
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
        
        
        
    """
    def login(self, email, password):
        email_input = WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located((By.ID, "i0116"))
        )
        email_input.send_keys(email)
        self.driver.find_element(By.ID, "idSIButton9").click()

        password_input = WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located((By.NAME, "passwd")))
        password_input.send_keys(password)
        self.driver.find_element(By.ID, "idSIButton9").click()

        try:
            accept_button = WebDriverWait(self.driver, Config.TIMEOUT).until(
                EC.visibility_of_element_located((By.ID, "acceptButton")))
            accept_button.click()
        except Exception:
            print("No se encontró el botón de aceptación en el tiempo esperado.")

    def verify_login_success(self):
        WebDriverWait(self.driver, Config.TIMEOUT).until(EC.title_contains("Microsoft"))
        assert "Microsoft" in self.driver.title, "El título no contiene la palabra Microsoft."

    def click_nav_menu_button(self):
        button = WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="O365_MainLink_NavMenu"]')))
        button.click() """
