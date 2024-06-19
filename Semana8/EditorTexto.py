# Creamos la clase Nodo
class Nodo:
    def __init__(self, dato):
        # Dato almacenado en el nodo
        self.dato = dato
        # Hace referencia al nodo anterior
        self.anterior = None
        # Hace referencia al nodo siguiente
        self.siguiente = None

# Creamos la clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        # Hace referencia al primer nodo de la lista
        self.cabeza = None
        # Hace referencia al nodo actual (usado como cursor)
        self.cursor = None

    def insertar(self, dato, posicion):
        # Se crea un nuevo nodo con el dato proporcionado
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            # Caso 1: Lista vacía, insertamos en la cabeza
            self.cabeza = nuevo_nodo
            self.cursor = self.cabeza
        elif posicion <= 0:
            # Caso 2: Insertar al principio de la lista
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            self.cursor = self.cabeza
        else:
            # Caso 3: Insertar en una posición específica o al final de la lista
            actual = self.cabeza
            index = 0
            while actual.siguiente:
                if index == posicion:
                    # Insertar el nuevo nodo en la posición especificada
                    nuevo_nodo.siguiente = actual.siguiente
                    nuevo_nodo.anterior = actual
                    actual.siguiente.anterior = nuevo_nodo
                    actual.siguiente = nuevo_nodo
                    self.cursor = nuevo_nodo
                    return
                actual = actual.siguiente
                index += 1
            
            # Si no se encontró la posición, se inserta al final de la lista
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            self.cursor = nuevo_nodo

    def eliminar(self, posicion):
        if self.cabeza is None:
            # No hacer nada si la lista está vacía
            return
        
        actual = self.cabeza
        index = 0
        while actual:
            if index == posicion:
                # Ajustar las referencias de los nodos anterior y siguiente
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                
                # Actualizar la cabeza si es necesario
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                # Actualizar el cursor si es necesario
                if actual == self.cursor:
                    self.cursor = actual.anterior
                return
            actual = actual.siguiente
            index += 1

    def mover_cursor(self, posicion):
        if self.cabeza is None:
            # No hacer nada si la lista está vacía
            return
        
        actual = self.cabeza
        index = 0
        while actual:
            if index == posicion:
                # Mover el cursor a la posición indicada
                self.cursor = actual
                return
            actual = actual.siguiente
            index += 1

    def obtener_texto(self):
        actual = self.cabeza
        texto = ""
        while actual:
            texto += actual.dato
            actual = actual.siguiente
        return texto

# Creamos la clase que representa un EditorDeTexto usando una lista doblemente enlazada
class EditorDeTexto:
    def __init__(self):
        # Se inicia una nueva lista doblemente enlazada
        self.lista = ListaDoblementeEnlazada()

    def insertar_texto(self, texto, posicion):
        for char in texto:
            # Insertar cada carácter en la posición indicada
            self.lista.insertar(char, posicion)
            posicion += 1

    def eliminar_texto(self, posicion, longitud):
        for _ in range(longitud):
            # Eliminar caracteres a partir de la posición indicada
            self.lista.eliminar(posicion)

    def mover_cursor(self, posicion):
        # Mover el cursor a la posición indicada
        self.lista.mover_cursor(posicion)

    def obtener_texto(self):
        # Obtener el texto completo almacenado en la lista
        return self.lista.obtener_texto()

# Acontinuación tenemos un ejemplo de ejecución
editor = EditorDeTexto()

# Insertar texto inicial en la posición 0
editor.insertar_texto("Hola soy Siomara", 0)
print("Texto inicial:", editor.obtener_texto())

# Insertar más texto en una posición específica (posición 15)
editor.insertar_texto(" y me gusta programar", 15)
print("Texto después de la inserción:", editor.obtener_texto())

# Eliminar una parte del texto desde la posición 5, eliminando 4 caracteres
editor.eliminar_texto(5, 4)
print("Texto después de eliminar:", editor.obtener_texto())

# Mover el cursor a la posición 12 y luego insertar texto en esa posición
editor.mover_cursor(12)
editor.insertar_texto("una estudiante de informática", 12)
print("Texto después de mover el cursor y insertar:", editor.obtener_texto())

