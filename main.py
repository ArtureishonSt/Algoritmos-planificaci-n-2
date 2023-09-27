import fifo
import prioridades
import rr
import sjf  # Importa el módulo sjf.py


# Función para agregar un nuevo proceso al archivo
def agregar_proceso():
    nombre = input("Ingresa el nombre del proceso: ")
    tiempo = int(input("Ingresa el tiempo de ejecución: "))
    prioridad = int(input("Ingresa la prioridad: "))
    posicion = input("¿Dónde deseas agregar el proceso? (Inicio o Fin): ").lower()

    if posicion == "inicio":
        with open("procesos.txt", "r") as archivo:
            lineas = archivo.readlines()
        with open("procesos.txt", "w") as archivo:
            archivo.write(f"{nombre}, {tiempo}, {prioridad}\n")
            archivo.writelines(lineas)
    elif posicion == "fin":
        with open("procesos.txt", "a") as archivo:
            archivo.write(f"{nombre}, {tiempo}, {prioridad}\n")
    else:
        print("Opción no válida. El proceso no se ha agregado.")


# Función para mostrar el menú y obtener una selección válida
def mostrar_menu():
    print("Selecciona una opción:")
    print("1. FIFO")
    print("2. Prioridades (Mayor a Menor)")
    print("3. Round Robin")
    print("4. SJF (Shortest Job First)")
    print("5. Agregar nuevo proceso")
    print("6. Salir")

    try:
        opcion = int(input("Ingresa el número de la opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Selecciona una opción válida.")
    except ValueError:
        print("Ingresa un número válido.")

    return mostrar_menu()  # Llama de nuevo a la función si la entrada no es válida


# Función principal
def main():
    archivo = "procesos.txt"  # Reemplaza con el nombre de tu archivo

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            fifo.simulacion_FIFO(archivo)
        elif opcion == 2:
            prioridades.administrar_procesos_prioridades()
        elif opcion == 3:
            nombre_archivo = "procesos.txt"
            procesos = rr.cargar_procesos(nombre_archivo)
            print("Ejecución de procesos (Round Robin):")
            rr.round_robin(procesos)
        elif opcion == 4:
            nombre_archivo = "procesos.txt"
            procesos = sjf.leer_procesos()
            print("Ejecución de procesos (SJF - Shortest Job First):")
            sjf.ejecutar_sjf(procesos)
        elif opcion == 5:
            agregar_proceso()
        elif opcion == 6:
            print("Saliendo del programa.")
            break


if __name__ == "__main__":
    main()
