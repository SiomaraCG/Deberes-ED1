# Se define una función llamada selection_sort que toma un arreglo como entrada
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

# Define una función llamada obtener_numeros que solicita al usuario ingresar números separados por espacios
def obtener_numeros():
    # Lee la entrada del usuario y la almacena en input_str
    input_str = input("Ingrese los números separados por espacios: ")
    try:
        # Intenta convertir los números ingresados en una lista de enteros
        numeros = [int(num) for num in input_str.split()]
    except ValueError:
        # Si se produce un error de ValueError, muestra un mensaje de error y devuelve una lista vacía
        print("Error: Por favor, ingrese solo números separados por espacios.")
        return []
    # Devuelve la lista de números ingresados por el usuario
    return numeros

# Obtiene la lista de números del usuario llamando a la función obtener_numeros
numeros = obtener_numeros()

# Realiza una copia de la lista original para mantenerla intacta
numeros_original = numeros.copy()

# Ordena la lista utilizando la función Selection Sort
selection_sort(numeros)

# Imprime la lista original y la lista ordenada
print("Lista original:", numeros_original)
print("Lista ordenada:", numeros)
