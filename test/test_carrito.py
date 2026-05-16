import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cart(login_in_driver):
    driver = login_in_driver

    # Agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    
    # Verificar contador carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"

    # Obtener nombre del primer producto
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar el producto agregado en el carrito
    assert cart_item == product_name, "El producto agregado no coincide"

    #------------------------------------------

    from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_add_product_to_cart(login_in_driver):

    driver = login_in_driver

    # ------------------------------------------------
    # 1 - Obtener nombre del primer producto
    # ------------------------------------------------

    first_product_name = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )[0].text

    print(f"\nProducto seleccionado: {first_product_name}")


    # ------------------------------------------------
    # 2 - Agregar producto al carrito
    # ------------------------------------------------

    add_to_cart_button = driver.find_elements(
        By.CLASS_NAME,
        "btn_inventory"
    )[0]

    add_to_cart_button.click()

    print("Producto agregado al carrito")


    # ------------------------------------------------
    # 3 - Verificar contador del carrito
    # ------------------------------------------------

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert cart_badge.text == "1", \
        "El contador del carrito no se actualizó correctamente"

    print(f"Contador del carrito: {cart_badge.text}")


    # ------------------------------------------------
    # 4 - Navegar al carrito
    # ------------------------------------------------

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    print("Ingreso al carrito correctamente")


    # ------------------------------------------------
    # 5 - Verificar producto en el carrito
    # ------------------------------------------------

    cart_product_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    ).text

    assert cart_product_name == first_product_name, \
        "El producto agregado no coincide con el del carrito"

    print(f"Producto en carrito: {cart_product_name}")

    print("\nTest de carrito ejecutado correctamente")