def arreglo_clase():
    # Creamos un arreglo vacio para que almacene los elementos
    arreglo = []
    # Se ingresa 20 elementos numéricos
    for i in range(20): # Ejecuta 20 veces
        # Se solicita al usuario que ingrese un número
        elemento = float(input(f"Ingrese el elemento {i + 1}: "))
        # Agrega el elemento ingresado a la lista arreglo
        arreglo.append(elemento)
        # Se imprime la lista después de cada número ingresado
        print("Elementos ingresados:", arreglo)

    # Creamos la parte 2 que es ingresar un numero adicional, denominado clave
    clave = float(input("Ingrese la clave a buscar: "))

    # Función para la búsqueda secuencial
    def busqueda_secuencial(arreglo, clave):
        # for para recorrer sobre todos los elementos del arreglo
        for i in range(len(arreglo)):
            # Si el elemento en la posición "i" del arreglo es igual a la clave, se retorna la posición "i"
            if arreglo[i] == clave:
                return i
        # Si la clave no se encuentra en el arreglo, se retorna -1
        return -1

    # Función para el ordenamiento burbuja
    def ordenamiento_burbuja(arreglo):
        # Obtenemos el tamaño del arreglo
        n = len(arreglo)
        # Creamo dos for para comparar y ordenar los elementos del arreglo
        for i in range(n):
            for j in range(0, n - i - 1):
                # Si el elemento actual es mayor que el siguiente, se intercambian
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

    # Función para la búsqueda binaria
    def busqueda_binaria(arreglo, clave):
        # Inicialización de variables para los índices de inicio y fin del rango de búsqueda
        inicio = 0
        fin = len(arreglo) - 1
        # Con while realizamos la búsqueda binaria
        while inicio <= fin:
            # Cálculo del índice medio del rango
            medio = (inicio + fin) // 2
            # Si el elemento en el índice medio es igual a la clave, se retorna el índice medio
            if arreglo[medio] == clave:
                return medio
            # Si la clave es mayor que el elemento en el índice medio, se actualiza el índice de inicio
            elif arreglo[medio] < clave:
                inicio = medio + 1
            # Si la clave es menor que el elemento en el índice medio, se actualiza el índice de fin
            else:
                fin = medio - 1
        # Si la clave no se encuentra en el arreglo, se retorna -1.
        return -1

    # Búsqueda secuencial del elemento en el arreglo
    posicion_secuencial = busqueda_secuencial(arreglo, clave)
    # Se imprime el resultado de la búsqueda secuencial
    if posicion_secuencial != -1:
        print(f"La clave fue encontrada en la posición {posicion_secuencial} mediante búsqueda secuencial.")
    else:
        print("Clave no encontrada mediante búsqueda secuencial.")

    # Se ordena el arreglo utilizando el método de ordenamiento burbuja
    ordenamiento_burbuja(arreglo)

    # Búsqueda binaria del elemento en el arreglo ordenado
    posicion_binaria = busqueda_binaria(arreglo, clave)
    # Se imprime el resultado de la búsqueda binaria
    if posicion_binaria != -1:
        print(f"La clave fue encontrada en la posición {posicion_binaria} mediante búsqueda binaria.")
    else:
        print("Clave no encontrada mediante búsqueda binaria.")

# Llamamos a la función "arreglo_clase" para iniciar el programa
arreglo_clase()