# Creamos la clase Nodo
class Nodo:
    def __init__(self, valor):
        # Se inicia el nodo con un valor y un puntero siguiente que inicialmente es None
        self.valor = valor
        self.siguiente = None

# Creamos la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        # Se inicia la lista enlazada con la cabeza apuntando a None
        self.cabeza = None
        
    def añadir(self, valor):
        # Creamos un nuevo nodo con el valor proporcionado
        nuevo_nodo = Nodo(valor)
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza de la lista
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            # Si la lista no está vacía, recorre la lista hasta encontrar el último nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            # Se añade el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        # Aqui verificamos si la lista está vacía
        if not self.cabeza:
            print("La lista está vacía.")
            return
        
        # Si el nodo a eliminar es la cabeza, se actualiza la cabeza al siguiente nodo
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return

        # Recorre la lista buscando el nodo anterior al que debe ser eliminado
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente


        # Dado caso que no se encuentre el valor, se imprimira un mensaje
        if not actual.siguiente:
            print(f"La canción {valor} no se encuentra en la playlist.")
        else:
            # Si encuentra el valor, actualiza el puntero siguiente para eliminar el nodo
            actual.siguiente = actual.siguiente.siguiente 
    
    def mostrar(self):
        # Recorre la lista e imprime el valor de cada nodo
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

class Playlist:
    def __init__(self):
        # Se inicia la playlist con una lista enlazada vacía
        self.playlist = ListaEnlazada()

    def añadir_cancion(self, cancion):
        # Se añade una canción a la lista enlazada
        self.playlist.añadir(cancion)
        # Se imprime un mensaje confirmando que la canción fue añadida
        print(f'Canción "{cancion}" añadida a la playlist.')

    def eliminar_cancion(self, cancion):
        # Se elimina una canción de la lista enlazada
        self.playlist.eliminar(cancion)
        # Se imprime un mensaje confirmando que la canción fue eliminada
        print(f'Canción "{cancion}" eliminada de la playlist.')

    def mostrar_playlist(self):
        # Se imprime un encabezado para la playlist
        print("Playlist:")
        # Se mostraran todas las canciones en la lista enlazada
        self.playlist.mostrar()

# Acontinuación tenemos un ejemplo de ejecución
# Crea una instancia de la playlist
mi_playlist = Playlist()
mi_playlist.añadir_cancion("Sebastián Yatra - Cómo Mirarte")
mi_playlist.añadir_cancion("Yo Te Esperaré -Cali Y El Dandee")
mi_playlist.añadir_cancion("Camila — Mientes")
# Se muestra la playlist actual
mi_playlist.mostrar_playlist()
# Eliminamos una canción de la playlist
mi_playlist.eliminar_cancion("Yo Te Esperaré -Cali Y El Dandee")
# Se muestra la playlist después de la eliminación
mi_playlist.mostrar_playlist()


