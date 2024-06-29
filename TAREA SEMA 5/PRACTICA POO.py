# Programa para gestionar el inventario de productos.

def agregar_producto(inventario, nombre, cantidad, precio):
    """
    Función que agrega un producto al inventario.

    Args:
    inventario (dict): El inventario de productos.
    nombre (str): El nombre del producto.
    cantidad (int): La cantidad del producto.
    precio (float): El precio del producto.

    Returns:
    dict: El inventario actualizado.
    """
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    return inventario


# Ejemplo de uso del programa
if __name__ == "__main__":
    inventario = {}
    inventario = agregar_producto(inventario, "Manzanas", 100, 0.50)
    inventario = agregar_producto(inventario, "Naranjas", 150, 0.50)
    print(f"Inventario: {inventario}")
