import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver_logged(login_in_page):

    driver = login_in_page

    return driver


def test_cart(driver_logged):

    driver = driver_logged

    # Obtener el primer producto
    primer_producto = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )[0]

    # Guardar nombre del producto
    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    # Guardar precio del producto
    precio_producto = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"Producto agregado: {nombre_producto}")
    print(f"Precio: {precio_producto}")

    # Agregar primer producto al carrito
    boton_agregar = primer_producto.find_element(
        By.CLASS_NAME,
        "btn_inventory"
    )

    boton_agregar.click()

    # Verificar contador del carrito
    contador_carrito = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert contador_carrito.text == "1", \
        "El contador del carrito no se incrementó correctamente"

    # Navegar al carrito
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Verificar ítem en carrito
    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    precio_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    # Comprobar producto correcto
    assert producto_carrito == nombre_producto, \
        "El producto agregado no coincide"

    assert precio_carrito == precio_producto, \
        "El precio del producto no coincide"

    print("Producto validado correctamente en el carrito")