import pytest
from selenium import webdriver
from config.config import Config

@pytest.fixture(params=["chrome","firefox","edge"])
def initialize_driver(request):
    
    if request.param == "chrome":
        driver= webdriver.Chrome()
    elif request.param == "firefox":
        driver= webdriver.Firefox()
    elif request.param == "edge":
        driver= webdriver.Edge()
    request.cls.driver = driver
    print ("Browser", request.param)
    driver.get(Config.LOG_URL)
    driver.maximize_window()
    yield 
    print("Close Driver")
    driver.close()

    
