import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def login(driver):
    driver.get("https://www.saucedemo.com/") # URL de la página de login de Sauce Demo

    usuario = driver.find_element(By.ID, "user-name") # ingreso de usuario
    usuario.send_keys("standard_user")

    password = driver.find_element(By.ID, "password") # ingreso de contraseña
    password.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click() # click en el botón de login

    print("Login exitoso") # Imprimir mensaje de éxito en la consola

try:
    login(driver)

finally:
    driver.quit()