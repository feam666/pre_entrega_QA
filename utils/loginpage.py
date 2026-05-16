import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def login(driver):
    driver.get("https://www.saucedemo.com/")

    # ingresar usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    # ingresar contraseña
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    # click login
    driver.find_element(By.ID, "login-button").click()

try:
    login(driver)

finally:
    driver.quit()