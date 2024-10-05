from abc import ABC, abstractmethod
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

# Aplique el patrón 'Template Method' para mayor flexibilidad y reutilizacion.

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.url = Config.LOG_URL

    def open(self):
        self.driver.get(self.url)

    @abstractmethod
    def login(self, email, password):
        pass

    @abstractmethod
    def verify_login_success(self):
        pass
