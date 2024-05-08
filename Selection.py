def selection_sort(arreglo):
    # Iteramos a través de todos los elementos del arreglo
    for i in range(len(arreglo)):
        # Encontramos el índice del elemento mínimo restante
        min_index = i
        for j in range(i + 1, len(arreglo)):
            if arreglo[j] < arreglo[min_index]:
                min_index = j
        # Intercambiamos el elemento mínimo con el primer elemento restante
        arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]

# Solicitar al usuario que ingrese los números separados por espacios
def obtener_numeros():
    input_str = input("Ingrese los números separados por espacios: ")
    try:
        numeros = [int(num) for num in input_str.split()]
    except ValueError:
        print("Error: Por favor, ingrese solo números separados por espacios.")
        return []
    return numeros

# Obtener la lista de números del usuario
numeros = obtener_numeros()

# Hacer una copia de la lista original para mantenerla intacta
numeros_original = numeros.copy()

# Ordenar la lista utilizando Selection Sort
selection_sort(numeros)

# Imprimir la lista original y la lista ordenada
print("Lista original:", numeros_original)
print("Lista ordenada:", numeros)
