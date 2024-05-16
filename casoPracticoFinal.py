import os
import time
os.system("color B")
#Definimos las clases para las tareas
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tareas(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def marcar_completadas(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
            print("La Tarea se marco como completada correctamente.")
        except IndexError:
            os.system("color 5")
            print("La posicion especificada no existe.")
            time.sleep(10)
            os.system("color 7")
    def mostrar_tareas(self):
        if not self.tareas:
            os.system("color 4")
            print("No hay tareas pendientes.")
            os.system("color B")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"{i}. {tarea.descripcion} - {estado}")

    def eliminar_tareas(self, posicion):
        try:
            del self.tareas[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            print("La posicion especificada no existe.")

# Funcion principal para interactuar con el usuario
def main():
    
    
    
    gestor = GestorTareas()

    while True:
        print("╔════════════════════════════════╗")
        print("║ Opciones a realizar:           ║")
        print("║════════════════════════════════║")
        print("║ 1. Agregar nueva tarea         ║")
        print("║ 2. Marcar tarea como completada║")
        print("║ 3. Mostrar todas las tareas    ║")
        print("║ 4. Eliminar tarea              ║")
        print("║ 5. Salir                       ║")
        print("╚════════════════════════════════╝")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripcion de la tarea: ")
            gestor.agregar_tareas(descripcion)
        elif opcion == "2":
            posicion = int(input("Ingrese la posicion de la tarea a marcar como completada: "))
            gestor.marcar_completadas(posicion)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            posicion = int(input("Ingrese la posicion de la tarea a eliminar: "))
            gestor.eliminar_tareas(posicion)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no valida Intentelo de nuevo.")

if __name__ == "__main__":
    main()
