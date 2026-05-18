# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if not lines or len(lines) <= 1:
            return []

        headers = []
        for header in lines[0].split(','):
            headers.append(header.strip())

        result = []

        for line in lines[1:]:
            if not line.strip():
                continue

            values = []
            for val in line.split(','):
                values.append(val.strip())

            row_dict = {}
            for i in range(len(headers)):
                key = headers[i]
                val = values[i]

                if key == 'age':
                    row_dict[key] = int(val)
                else:
                    row_dict[key] = val

            result.append(row_dict)

        return result
    except FileNotFoundError:
        raise FileNotFoundError("No existe el archivo")



