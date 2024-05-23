# Primero importamos las librerias que vamos a utilizar en este caso es random, time
import random
import time

# Se crea una funcion para generar una lista de números aleatorios
def generar_lista(tamano):
    # Aqui se genera y retorna una lista de elementos con valores aleatorios entre 1 y 100
    return [random.randint(1, 100) for _ in range(tamano)]

# Se crea una función que encuentra el elemento máximo y se suma todos los elementos 
def maximo_y_suma(lista):
    # Inicializa 'maximo' con el primer elemento de la lista
    maximo = lista[0]
    # Inicializa 'suma' en 0
    suma = 0
    # Recorre cada elemento de la lista
    for num in lista:
        if num > maximo:
            maximo = num
        # Suma el elemento actual a 'suma'
        suma += num
    # Retorna el valor máximo y la suma de los elementos
    return maximo, suma

# Bloque principal del programa
if __name__ == "__main__":
    # Se define el tamaño de la lista
    tamano_lista = 1000
    # En 'tamano_lista' se genera una lista de números aleatorios de tamaño
    lista = generar_lista(tamano_lista)
    # Se registra el tiempo de inicio
    start_time = time.time()
    # Se encuentra el máximo y la suma de los elementos de la lista
    maximo, suma = maximo_y_suma(lista)
    # Se registra el tiempo de finalización
    end_time = time.time()
    # Calcula el tiempo de ejecución total
    optimized_time = end_time - start_time

    # Imprime la lista generada
    print(f"Lista: {lista}")
    # Imprime el valor máximo encontrado en la lista
    print(f"Máximo: {maximo}")
    # Imprime la suma de los elementos de la lista
    print(f"Suma: {suma}")
    # Imprime el tiempo de ejecución del código
    print(f"Tiempo de ejecución (optimizado): {optimized_time:.6f} segundos")
