from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

# Aplique el patrón 'Template Method' para mayor flexibilidad y reutilizacion.

class BasePage(ABC):
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.url)
            
    def find(self, *locator):
        WebDriverWait(self.driver,Config.TIME_OUT).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click(self,locator):
        self.find(*locator).click()
        
    def set(self,locator,value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)
        
    def get_text(self,locator):
        return self.find(*locator).text
    
    def get_title(self):
        return self.driver.title
