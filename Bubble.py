# Se define una función llamada bubble_sort que toma un arreglo como entrada
def bubble_sort(arreglo):
    # Se obtiene la longitud del arreglo
    n = len(arreglo)
    # Se inicia un bucle while que se ejecutará hasta que n sea 0
    while n > 0:
        # Inicia un bucle for que recorre sobre el rango de índices de 1 a n
        for i in range(1, n):
            # Se comprueba si el elemento actual es mayor que el anterior
            if arreglo[i - 1] > arreglo[i]:
                # Intercambia los elementos si el anterior es mayor
                arreglo[i - 1], arreglo[i] = arreglo[i], arreglo[i - 1]
        # Disminuye n después de cada pasada del bucle
        n -= 1
    # Devuelve el arreglo ordenado
    return arreglo

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

# Ordena la lista utilizando la función bubble_sort
numeros_ordenados = bubble_sort(numeros)

# Imprime la lista original y la lista ordenada
print("Lista original:", numeros_original)
print("Lista ordenada:", numeros_ordenados)


