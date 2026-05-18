# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")

    with open(filename, 'r') as archivo:
        total = 0.0
        contador = 0
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia:  # Ignora líneas vacías
                continue
            try:
                total += float(linea_limpia)
                contador += 1
            except ValueError:
                continue  # Ignora líneas que no sean números

        if contador == 0:
            raise ValueError("El archivo no contiene números válidos.")

        return total / contador

