class Nodo {
    String nombre;
    Nodo siguiente;

    Nodo(String nombre) {
        this.nombre = nombre;
        this.siguiente = null;
    }
}

class Cola {
    Nodo frente;
    Nodo finalCola;

    Cola() {
        this.frente = null;
        this.finalCola = null;
    }

    void agregar(String nombre) {
        Nodo nuevoNodo = new Nodo(nombre);
        if (finalCola == null) {
            frente = finalCola = nuevoNodo;
        } else {
            finalCola.siguiente = nuevoNodo;
            finalCola = nuevoNodo;
        }
    }

    String quitar() {
        if (frente == null) {
            return null;
        }
        String nombre = frente.nombre;
        frente = frente.siguiente;
        if (frente == null) {
            finalCola = null;
        }
        return nombre;
    }

    boolean estaVacia() {
        return frente == null;
    }
}

class Cliente {
    String nombre;
    int tiempoLlegada;

    Cliente(String nombre, int tiempoLlegada) {
        this.nombre = nombre;
        this.tiempoLlegada = tiempoLlegada;
    }
}

class SistemaDeCola {
    Cola cola;
    int tiempoActual;

    SistemaDeCola() {
        this.cola = new Cola();
        this.tiempoActual = 0;
    }

    void agregarCliente(String nombre) {
        Cliente cliente = new Cliente(nombre, tiempoActual);
        cola.agregar(cliente.nombre);
        tiempoActual++;
    }

    void atenderCliente() {
        String clienteAtendido = cola.quitar();
        if (clienteAtendido != null) {
            System.out.println("Atendiendo a: " + clienteAtendido + " en el tiempo: " + tiempoActual);
        } else {
            System.out.println("No hay clientes en la cola.");
        }
        tiempoActual++;
    }

    void mostrarEstado() {
        Nodo actual = cola.frente;
        System.out.println("Clientes en la cola:");
        while (actual != null) {
            System.out.println(actual.nombre);
            actual = actual.siguiente;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        SistemaDeCola sistema = new SistemaDeCola();

        // Simulación con una llegada rápida de clientes
        sistema.agregarCliente("Alex Carrión");
        sistema.agregarCliente("Jorge Herrera");
        sistema.agregarCliente("Daniela Maza");

        sistema.atenderCliente();
        sistema.atenderCliente();
        sistema.atenderCliente();
        sistema.atenderCliente();

        // Simulación con una llegada lenta de clientes
        sistema.agregarCliente("Maria González");
        sistema.atenderCliente();
        sistema.agregarCliente("Luis Martinez");
        sistema.atenderCliente();
        sistema.atenderCliente();

        // Mostrar estado final de la cola
        sistema.mostrarEstado();
    }
}

