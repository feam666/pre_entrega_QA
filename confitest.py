import pytest
from selenium import webdriver
from utils.loginpage import login 


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()    
    options.add_argument("--incognito")  # Ejecuta el navegador en modo incógnito
    options.add_argument("--headless")  # Ejecuta el navegador en modo headless (Sin interfaz gráfica)


    
    
    driver = webdriver.Chrome(options = options)

    yield driver

    driver.quit()

@pytest.fixture
def login_in_page(driver):
    login(driver)   
    return driver


