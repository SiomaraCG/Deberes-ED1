# Creamos una clase llamada Cola
class Cola:
    def __init__(self):
        # Inicializa una nueva cola usando una lista vacía
        self.items = []  

    def encolar(self, item):
        # Añade un elemento al final de la lista (cola)
        self.items.append(item)  

    def desencolar(self):
        if not self.esta_vacia():
            # Elimina y retorna el primer elemento de la lista (cola)
            return self.items.pop(0)  
        else:
            # Retorna None si la lista (cola) está vacía
            return None  

    def esta_vacia(self):
        # Retorna True si la lista (cola) está vacía, de lo contrario False
        return len(self.items) == 0  

class SistemaDeGestionDeTareas:
    def __init__(self):
        # Inicializa una nueva instancia de la clase Cola
        self.cola_de_tareas = Cola()  

    def agregar_tarea(self, tarea):
        # Añade una tarea a la cola de tareas
        self.cola_de_tareas.encolar(tarea)  
        # Imprime un mensaje indicando que la tarea se agregó a la cola
        print(f"Tarea '{tarea}' agregada a la cola.")  

    def procesar_tarea(self):
        # Intenta eliminar y obtener la primera tarea de la cola
        tarea = self.cola_de_tareas.desencolar()  
        if tarea:
            # Si hay una tarea, imprime un mensaje indicando que se está procesando
            print(f"Procesando tarea: {tarea}")  
        else:
            # Si no hay tareas, imprime un mensaje indicando que la cola está vacía
            print("No hay tareas en la cola.") 

if __name__ == "__main__":
    # Crea una instancia del sistema de gestión de tareas
    sistema = SistemaDeGestionDeTareas() 
    # Agrega "Tarea 1" a la cola de tareas 
    sistema.agregar_tarea("Tarea 1") 
    # Agrega "Tarea 2" a la cola de tareas 
    sistema.agregar_tarea("Tarea 2") 
    # Procesa (elimina y muestra) la primera tarea en la cola ("Tarea 1") 
    sistema.procesar_tarea()
    # Procesa (elimina y muestra) la siguiente tarea en la cola ("Tarea 2")  
    sistema.procesar_tarea() 
    # Intenta procesar otra tarea, pero la cola está vacía, así que muestra un mensaje indicando eso 
    sistema.procesar_tarea()  
