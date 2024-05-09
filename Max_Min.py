# Se define una función llamada max_min que toma un arreglo como entrada
def max_min(arreglo):
    if len(arreglo) == 0:
        # Si el arreglo está vacío, retorna None para el máximo y el mínimo
        return None, None  
    elif len(arreglo) == 1:
        # Si el arreglo tiene un solo elemento, lo retorna como máximo y mínimo
        return arreglo[0], arreglo[0] 
    else:
        # Empieza asumiendo que el primer elemento es el máximo
        maximo = arreglo[0]
        # Empieza asumiendo que el primer elemento es el mínimo  
        minimo = arreglo[0]
        # Por cada elemento en el arreglo  
        for elemento in arreglo:  
            # Si el elemento actual es mayor que el máximo
            if elemento > maximo:  
                # Actualiza el valor máximo
                maximo = elemento 
                # Si el elemento actual es menor que el mínimo 
            elif elemento < minimo:  
                # Actualiza el valor mínimo
                minimo = elemento  
                # Retorna los valores máximo y mínimo
        return maximo, minimo  

# Solicita al usuario que ingrese el arreglo
# Se pide al usuario que ingrese números separados por espacios
entrada = input("Ingrese los números del arreglo separados por espacios: ")  
# Convierte la entrada en una lista de enteros
arreglo = list(map(int, entrada.split()))  

# Llama a la función para encontrar el máximo y mínimo
# Usa la función para obtener los valores máximo y mínimo del arreglo
maximo, minimo = max_min(arreglo)  
# Imprime los valores máximo y mínimo encontrados
print("Max =", maximo, ", Min =", minimo)  


