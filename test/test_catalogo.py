def test_inventory_navigation(login):

    inventory = InventoryPage(login)

    expected_title = "Products" # Título esperado de la página de inventario
    actual_title = inventory.get_title() # Obtener el título actual de la página de inventario
    assert actual_title == expected_title
    print(f"\nTítulo validado: {actual_title}")



    assert inventory.products_visible() # Validar que los productos estén visibles en la página de inventario
    print("Productos visibles correctamente")



    assert inventory.menu_visible() # # Validar que el menú esté visible en la página de inventario
    print("Menú visible")
    assert inventory.filter_visible()
    print("Filtro visible")



    product_name, product_price = inventory.get_first_product_info() # Obtener nombre y precio del primer producto

    print(f"\nPrimer producto: {product_name}")
    print(f"Precio: {product_price}")