def max_min(arreglo):
    if len(arreglo) == 0:
        return None, None  # Si el arreglo está vacío, retorna None para el máximo y el mínimo
    elif len(arreglo) == 1:
        return arreglo[0], arreglo[0]  # Si el arreglo tiene un solo elemento, lo retorna como máximo y mínimo
    else:
        maximo = arreglo[0]  # Empieza asumiendo que el primer elemento es el máximo
        minimo = arreglo[0]  # Empieza asumiendo que el primer elemento es el mínimo
        for elemento in arreglo:  # Por cada elemento en el arreglo
            if elemento > maximo:  # Si el elemento actual es mayor que el máximo
                maximo = elemento  # Actualiza el valor máximo
            elif elemento < minimo:  # Si el elemento actual es menor que el mínimo
                minimo = elemento  # Actualiza el valor mínimo
        return maximo, minimo  # Retorna los valores máximo y mínimo

# Solicita al usuario que ingrese el arreglo
entrada = input("Ingrese los números del arreglo separados por espacios: ")  # Pide al usuario que ingrese números separados por espacios
arreglo = list(map(int, entrada.split()))  # Convierte la entrada en una lista de enteros

# Llama a la función para encontrar el máximo y mínimo
maximo, minimo = max_min(arreglo)  # Usa la función para obtener los valores máximo y mínimo del arreglo
print("Max =", maximo, ", Min =", minimo)  # Imprime los valores máximo y mínimo encontrados


