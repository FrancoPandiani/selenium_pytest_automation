from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class OutlookPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Config.LOG_URL

    def open(self):
        self.driver.get(self.url)

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
        assert "Microsoft" in self.driver.title, "El titulo no contiene la palabra Microsoft."

    def click_nav_menu_button(self):
        button = WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="O365_MainLink_NavMenu"]')) )
        button.click()
