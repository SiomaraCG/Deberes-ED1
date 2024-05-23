class Cola:
    def __init__(self):
        self.items = []  # Inicializa una nueva cola usando una lista

    def encolar(self, item):
        self.items.append(item)  # Añade un elemento al final de la cola

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)  # Elimina y retorna el primer elemento de la cola
        else:
            return None  # Retorna None si la cola está vacía

    def esta_vacia(self):
        return len(self.items) == 0  # Verifica si la cola está vacía
    
class SistemaDeGestionDeTareas:
    def __init__(self):
        self.cola_de_tareas = Cola()

    def agregar_tarea(self, tarea):
        self.cola_de_tareas.encolar(tarea)
        print(f"Tarea '{tarea}' agregada a la cola.")

    def procesar_tarea(self):
        tarea = self.cola_de_tareas.desencolar()
        if tarea:
            print(f"Procesando tarea: {tarea}")
        else:
            print("No hay tareas en la cola.")

if __name__ == "__main__":
    sistema = SistemaDeGestionDeTareas()
    sistema.agregar_tarea("Tarea 1")
    sistema.agregar_tarea("Tarea 2")
    sistema.procesar_tarea()
    sistema.procesar_tarea()
    sistema.procesar_tarea()
