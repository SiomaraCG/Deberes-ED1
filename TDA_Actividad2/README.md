# Sistema de Gestión de Tareas con Cola

Este proyecto implementa una cola y un sistema de gestión de tareas simple en Python.

## Descripción

La cola es una estructura de datos FIFO (First In, First Out) ideal para manejar tareas en el orden en que llegan. Este sistema permite agregar tareas a una cola y procesar la tarea más antigua.

## Instrucciones para Compilar y Ejecutar

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/sistema-gestion-tareas.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd sistema-gestion-tareas
    ```
3. Ejecuta el script principal:
    ```bash
    python gestion_de_tareas.py
    ```

## Ejemplos de Uso

```python
sistema = SistemaDeGestionDeTareas()
sistema.agregar_tarea("Tarea 1")
sistema.agregar_tarea("Tarea 2")
sistema.procesar_tarea()
sistema.procesar_tarea()
sistema.procesar_tarea()
