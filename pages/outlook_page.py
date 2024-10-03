from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OutlookPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://login.live.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        # Esperar hasta que el campo de email sea visible y luego ingresa el email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "i0116")))
        email_input.send_keys(email)
        self.driver.find_element(By.ID, "idSIButton9").click() 
        
        # Esperar hasta que el campo de password sea visible y luego ingresa la contraseña
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "passwd")))
        password_input.send_keys(password)
        self.driver.find_element(By.ID, "idSIButton9").click()
        
        # Espera a que aparezca el cuadro de confirmación
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "acceptButton")))
            accept_button.click() 
        except Exception:
            print("No se encontró el botón de aceptación en el tiempo esperado.")

    def verify_login_success(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Microsoft"))
        assert "Microsoft" in self.driver.title, "Login failed, title does not contain Microsoft."
        
    def click_nav_menu_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="O365_MainLink_NavMenu"]')))
        button.click()
