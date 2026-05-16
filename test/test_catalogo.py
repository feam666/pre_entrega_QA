import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

@pytest.fixture
def driver_logged(login_in_page):

    driver = login_in_page

    return driver


# Validar título de la página
def test_inventory_title(driver_logged):

    titulo = driver_logged.title

    assert titulo == "Swag Labs", \
        "El título de la página no es correcto"


# Validar presencia de productos
def test_productos_visibles(driver_logged):

    productos = driver_logged.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0, \
        "No hay productos visibles en la página"


# Validar elementos importantes de la interfaz
def test_ui_elements(driver_logged):

    menu = driver_logged.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    filtro = driver_logged.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    carrito = driver_logged.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    assert menu.is_displayed(), \
        "El menú no está visible"

    assert filtro.is_displayed(), \
        "El filtro no está visible"

    assert carrito.is_displayed(), \
        "El carrito no está visible"


# Mostrar nombre y precio del primer producto
def test_primer_producto(driver_logged):

    primer_producto = driver_logged.find_element(
        By.CLASS_NAME,
        "inventory_item"
    )

    nombre = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")

    assert nombre != "", \
        "El producto no tiene nombre"

    assert precio != "", \
        "El producto no tiene precio"