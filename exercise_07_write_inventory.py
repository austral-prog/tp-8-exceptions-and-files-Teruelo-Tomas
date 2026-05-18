# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, una línea por item, ordenadas
    alfabéticamente por nombre de item, con el formato:

        item:cantidad

    Reglas:
    - Cada línea debe terminar con "\\n".
    - Si el diccionario está vacío, el archivo se crea vacío.
    - Si el archivo ya existía, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        filename: str - nombre del archivo a escribir.
        inventory: dict[str, int] - item -> cantidad.

    Returns:
        None

    Ejemplo:
        write_inventory("stock.txt", {"wood": 10, "coal": 3, "iron": 7})
        # El archivo stock.txt queda con:
        # coal:3
        # iron:7
        # wood:10
    """
    try:
        with open(filename, 'w') as archivo:

            if len(inventory) == 0:
                return

            items_ordenados = list(inventory.keys())

            items_ordenados.sort()

            for item in items_ordenados:
                cantidad = inventory[item]

                linea = item + ":" + str(cantidad) + "\n"

                archivo.write(linea)

    except PermissionError:
        print("Error: No se tienen los permisos necesarios para escribir en el archivo.")
    except Exception as error_inesperado:
        print("Ocurrió un error inesperado al intentar escribir el archivo:", error_inesperado)
