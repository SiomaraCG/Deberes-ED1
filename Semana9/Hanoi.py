# Importamos la librería de visualización gráfica matplotlib
import matplotlib.pyplot as plt

# Función recursiva para resolver las Torres de Hanoi
def hanoi(n, source, target, auxiliary, moves):
    # Caso base: si solo hay un disco, se mueve directamente al objetivo
    if n == 1:  
        # Agrega el movimiento a la lista
        moves.append((source, target))  
    else:
        # Mueve n-1 discos de source a auxiliary
        hanoi(n-1, source, auxiliary, target, moves)  
        # Mueve el disco n de source a target
        moves.append((source, target))  
        # Mueve los n-1 discos de auxiliary a target
        hanoi(n-1, auxiliary, target, source, moves)  

# Función para dibujar el estado actual de las varillas
def draw_state(ax, rods, num_disks):
    # Limpia el área de dibujo
    ax.clear()  
    # Posiciones horizontales de las varillas
    rod_positions = [0.2, 0.5, 0.8]  
    # Altura de cada disco
    disk_height = 0.02  
    # Colores para los discos
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta'] 

    # Dibuja cada varilla y sus discos
    for rod_index, rod in enumerate(rods):
        # Posición x de la varilla actual
        rod_x = rod_positions[rod_index]  
        # Dibuja la varilla
        ax.plot([rod_x, rod_x], [0, num_disks * disk_height], color='black', linewidth=2)  

        # Dibuja cada disco en la varilla
        for disk_index, disk_size in enumerate(rod):
            # Ancho del disco basado en su tamaño
            disk_width = (disk_size + 1) * 0.05  
            # Posición x del disco
            disk_x = rod_x - disk_width / 2  
            # Posición y del disco
            disk_y = disk_index * disk_height 
            # Dibuja el disco
            ax.add_patch(plt.Rectangle((disk_x, disk_y), disk_width, disk_height, color=colors[disk_size % len(colors)])) 

    # Límite x del área de dibujo
    ax.set_xlim(0, 1)  
    # Límite y del área de dibujo
    ax.set_ylim(0, num_disks * disk_height + 0.1)  
    # Oculta los ejes
    ax.axis('off')  

# Función para crear la animación
def animate_hanoi(num_disks):
    # Crea una figura y un eje para dibujar
    fig, ax = plt.subplots()  
    # Inicializa las varillas con los discos en la primera varilla
    rods = [list(range(num_disks, 0, -1)), [], []]  
    # Lista para almacenar los movimientos
    moves = []  
    # Resuelve las Torres de Hanoi y guarda los movimientos
    hanoi(num_disks, 0, 2, 1, moves)
    
    # Dibuja el estado inicial
    draw_state(ax, rods, num_disks) 
    # Pausa de 2 segundos antes de empezar la animación
    plt.pause(2)  

    # Función de actualización para la animación
    def update(frame):
        if frame < len(moves):
            # Obtiene el movimiento actual
            source, target = moves[frame]  
            # Verifica que haya discos en la varilla de origen
            if rods[source]:  
                # Toma el disco de la varilla de origen
                disk = rods[source].pop() 
                # Coloca el disco en la varilla de destino
                rods[target].append(disk)  
                # Dibuja el nuevo estado
            draw_state(ax, rods, num_disks)  
            # Pausa para dar tiempo a la animación a ser dibujada
            plt.pause(1)  

    # Ejecuta la función de actualización para cada movimiento
    for frame in range(len(moves)):  
        update(frame)

    # Muestra la animación completa
    plt.show()  

# Ejemplo de uso: animación de las Torres de Hanoi con 3 discos
animate_hanoi(3)
