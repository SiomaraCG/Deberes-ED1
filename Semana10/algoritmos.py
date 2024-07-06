# Función de ordenación por burbuja
def bubble_sort(arr):
    n = len(arr)  # Obtiene la longitud del array
    for i in range(n):  # Recorre sobre cada elemento del array
        for j in range(0, n-i-1):  # Recorre sobre los elementos restantes no ordenados
            if arr[j] > arr[j+1]:  # Compara el elemento actual con el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos si están en el orden incorrecto
# Ejemplo de uso:
arr = [68, 32, 27, 15, 24, 13, 90]
bubble_sort(arr)
print("Ordenación por burbuja:", arr)

# Función de ordenación por selección
def selection_sort(arr):
    n = len(arr)  # Obtiene la longitud del array
    for i in range(n):  # Recorre sobre cada elemento del array
        min_idx = i  # Supone que el elemento actual es el menor
        for j in range(i+1, n):  # Recorre sobre los elementos restantes
            if arr[j] < arr[min_idx]:  # Encuentra el índice del menor elemento
                min_idx = j  # Actualiza el índice del menor elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambia el menor elemento encontrado con el elemento actual
# Ejemplo de uso:
arr = [68, 27, 13, 25, 10]
selection_sort(arr)
print("Ordenación por selección:", arr)

# Función de ordenación por inserción
def insertion_sort(arr):
    n = len(arr)  # Obtiene la longitud del array
    for i in range(1, n):  # Recorre desde el segundo elemento hasta el final
        key = arr[i]  # Almacena el elemento actual
        j = i - 1  # Inicializa j para comparar con los elementos anteriores
        while j >= 0 and key < arr[j]:  # Desplaza los elementos mayores a la derecha
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Inserta el elemento en su posición correcta
# Ejemplo de uso:
arr = [15, 12, 10, 4, 7]
insertion_sort(arr)
print("Ordenación por inserción:", arr)

# Función de ordenación por mezcla (merge sort)
def merge_sort(arr):
    if len(arr) > 1:  # Comprueba si el array tiene más de un elemento
        mid = len(arr) // 2  # Encuentra el punto medio del array
        L = arr[:mid]  # Divide el array en la mitad izquierda
        R = arr[mid:]  # Divide el array en la mitad derecha

        merge_sort(L)  # Ordena recursivamente la mitad izquierda
        merge_sort(R)  # Ordena recursivamente la mitad derecha

        i = j = k = 0  # Inicializa los índices para recorrer L, R y arr

        while i < len(L) and j < len(R):  # Mezcla los arrays L y R en arr
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):  # Copia los elementos restantes de L en arr
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):  # Copia los elementos restantes de R en arr
            arr[k] = R[j]
            j += 1
            k += 1
# Ejemplo de uso:
arr = [11, 15, 13, 9, 6, 7]
merge_sort(arr)
print("Ordenación por mezcla:", arr)

# Función de ordenación rápida (quick sort)
def quick_sort(arr, low, high):
    if low < high:  # Comprueba si hay más de un elemento en el array
        pi = partition(arr, low, high)  # Particiona el array y obtiene el índice del pivote

        quick_sort(arr, low, pi - 1)  # Ordena recursivamente la sublista izquierda
        quick_sort(arr, pi + 1, high)  # Ordena recursivamente la sublista derecha

# Función para particionar el array
def partition(arr, low, high):
    pivot = arr[high]  # Selecciona el último elemento como pivote
    i = low - 1  # Inicializa el índice del elemento más pequeño

    for j in range(low, high):  # Recorre los elementos desde low hasta high-1
        if arr[j] < pivot:  # Si el elemento actual es menor que el pivote
            i += 1  # Incrementa el índice del elemento más pequeño
            arr[i], arr[j] = arr[j], arr[i]  # Intercambia los elementos

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Intercambia el pivote con el elemento siguiente al más pequeño
    return i + 1  # Devuelve el índice del pivote
# Ejemplo de uso:
arr = [10, 7, 8, 9, 2, 6]
quick_sort(arr, 0, len(arr) - 1)
print("Ordenación rápida:", arr)


