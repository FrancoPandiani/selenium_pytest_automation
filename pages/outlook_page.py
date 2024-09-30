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
        # Esperar hasta que el campo de email sea visible y luego ingresar el email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "i0116"))
        )
        email_input.send_keys(email)
        
        # Hacer clic en el botón "Siguiente"
        self.driver.find_element(By.ID, "idSIButton9").click() 
        
        # Esperar hasta que el campo de contraseña sea visible y luego ingresar la contraseña
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "passwd"))
        )
        password_input.send_keys(password)
        
        # Hacer clic en el botón "Iniciar sesión"
        self.driver.find_element(By.ID, "idSIButton9").click()  # iniciar sesión

    def verify_login_success(self):
        # Esperar a que el título contenga "Outlook"
        WebDriverWait(self.driver, 10).until(EC.title_contains("Outlook"))
        assert "Outlook" in self.driver.title, "Login failed, title does not contain 'Outlook'."


    def logout(self):
        profile_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='profile-button']")))
        profile_icon.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "id_signout"))).click()
