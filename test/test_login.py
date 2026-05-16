import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()

try:
    # ingreso a la pagina
    driver.get("https://www.saucedemo.com/")
    
    # ingresar usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    # ingresar contraseña
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")


    # presionar el boton de login
    password = driver.find_element(By.ID, "password")
    password.send_keys(Keys.ENTER)

    # verificar que se haya ingresado correctamente
    if "/inventory.html" in driver.current_url:
        print("Login exitoso")  
    else:
        print("Login fallido")

finally:
    driver.quit() 

