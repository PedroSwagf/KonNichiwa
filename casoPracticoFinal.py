#importamos los modulos de sistema
import os
import time

#ponemos los comando para limpiar la consola y cambiarle el color de la misma

os.system("cls")                                                        #limpiamos la consola antes de arrancar el programa
os.system("color B")                                                    #cambiamos le color de la consola al iniciarel programa


#definimos las clases para las tareas
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion                                  #guardamos la descripcion de la tarea
        self.completada = completada                                    #guardamos el estado de la tarea para saber si esta completada o no, por defecto es false osea esta en pendiente

class GestorTareas:
    def __init__(self):
        self.tareas = []  

    def agregar_tareas(self, descripcion):
        try:
            tarea = Tarea(descripcion)                                  #creamos una nueva tarea
            self.tareas.append(tarea)                                   #añadimos la tarea a la lista de tareas
            os.system("Color 2")                                        #cambiamos el color a verde si la tarea es agregada correctamente
            print("Tarea agregada correctamente.")                      #imprimimos el mensaje
            time.sleep(2)                                               #hacemos una pause de 2 segundos
            os.system("Color B")                                        #ponemos el color de la consola como en el inicio del programa
        except IndexError:
            os.system("Color D")                                        #cambiamos el color a rojo si hubo un problema simulando que fuera un mensaje de advertencia
            print("No se pudo agregar la tarea.")                       #lanzamos esta excepcion en casa de que pase algo y no se pueda agregar correctamente la tarea.
            time.sleep(2)                                               #hacemos una pause de 2 segundos
            os.system("Color B")                                        #ponemos el color de la consola como en el inicio del programa
            
    def marcar_completadas(self, posicion):
        try:
            tarea = self.tareas[posicion]                           #obtenemos la tarea segun la posicion en la que este por defecto siempre se empezara desde la posicion 0
            tarea.completada = True                                 #marcamos como lista
            os.system("Color A")                                    #cambiamos el color del texto a verde claro para indicar que fue agragada correctamente
            print("La Tarea se marco como completada correctamente.")
            time.sleep(2)                                           
            os.system("Color B")                                     
        except IndexError:
            os.system("Color D")
            print("La posicion especificada no existe.")            #lanzamos esta excepcion en caso de que usuario señale una posicion que no existe a la hora de marcar la tarea como completada
            time.sleep(2)                                           
            os.system("Color B")   
            
    def reabrir_tarea(self, posicion):
        try:
            tarea = self.tareas[posicion]                           #obtenemos la tarea por su posición
            tarea.completada = False                                #la marcamos como no completada
            os.system("Color A") 
            print("La tarea se reabrio correctamente.")
            time.sleep(2)  
            os.system("Color B") 
        except IndexError:                                          #si la posicion no existe
            os.system("Color D")  
            print("La posición especificada no existe.")  
            time.sleep(2)  
            os.system("Color B")  
                                    
    def mostrar_tareas(self):
        if not self.tareas:                                         #si no hay tareas, cambiamos el color y lanzamos un mensaje.
            os.system("Color E")                                    #cambiamos el color del texto a amarillo
            print("No hay tareas pendientes.")
            time.sleep(2)                                            
            os.system("Color B")                                     
        else:
            for i, tarea in enumerate(self.tareas):                  #recorremos todas las tareas con un bucle for
                estado = "Completada" if tarea.completada else "Pendiente"   #comprobamos el estado de la tarea
                print(f"{i}. {tarea.descripcion} - {estado}")        #imprimimos el estado de la misma

    def eliminar_tareas(self, posicion):
        try:
            del self.tareas[posicion]                                #eliminamos la tarea por su posicion
            os.system("Color A")
            print("Tarea eliminada correctamente.")
            time.sleep(2)
            os.system("Color B")
        except IndexError:                                           #si la posición no existe
            os.system("Color C")
            print("La posicion especificada no existe.")
            time.sleep(2)
            os.system("Color B")
            
# Funcion principal para interactuar con el usuario
def main():
      
    gestor = GestorTareas()                                         #hacemos una instancia del gestor de tareas

    while True:                                                     #declaramos un bucle while para que el programa finalize cuando el usuario decida salir
        print("Kon'nichiwa")                                        #mensaje de bienvenida
        print("")
        print("")
        print("")
        print("                                       ╔════════════════════════════════╗")
        print("                                       ║ Opciones a realizar:           ║")
        print("                                       ║════════════════════════════════║")
        print("                                       ║ 1. Agregar nueva tarea         ║")
        print("                                       ║ 2. Marcar tarea como completada║")
        print("                                       ║ 3. Mostrar todas las tareas    ║")
        print("                                       ║ 4. Eliminar tarea              ║")
        print("                                       ║ 5. Reabrir tarea               ║")
        print("                                       ║ 6. Salir                       ║")
        print("                                       ╚════════════════════════════════╝")

        print("")
        print("")
        print("")
        
        opcion = input("Seleccione una opcion: ")               #pedimos al usuario que elija una opcion
                                                                #declaramos las opciones a elegir en el gestor de tareas
        if opcion == "1":
            descripcion = input("Ingresa la descripcion de la tarea: ") #le pedimos al usuario que agrege una descripcion en la tarea
            gestor.agregar_tareas(descripcion)                  #añadimos la nueva tarea al gestor    
        elif opcion == "2":
            posicion = int(input("Ingresa la posicion de la tarea a marcar como completada: ")) #pedimos al usuario que seleccione la posicion de la tarea que quiere marcar como lista
            gestor.marcar_completadas(posicion)                 #marcamos la tarea como completada     
        elif opcion == "3":                                     #mostramos todas las tareas
            gestor.mostrar_tareas()         
        elif opcion == "4":
            posicion = int(input("Ingresa la posicion de la tarea a eliminar: ")) #pedimos que el usuario seleccione la posicion para eliminar la tarea
            gestor.eliminar_tareas(posicion)                    #eliminamos la tarea  
        elif opcion == "5":
            posicion = int(input("Ingresa la posicion de la tarea a reabrir:"))    #pedimos la posicion de la tarea a reabrir, esta opcion la agrege de mi parte porque me parece util en caso de que se marque una tarea completada por error y la misma aun sigue en proceso
            gestor.reabrir_tarea(posicion)
        elif opcion == "6":
            print("¡Sayonara!")                                #despedida
            time.sleep(2)
            os.system("cls")                                   #limpipamos la consola 
            os.system("Color F")                               #la devolvemos a color blanco 
            break
        else:
            os.system("Color D")
            print("Opcion no valida intentelo de nuevo.") #si el usuario elige una opcion que no esta en la seleccion le lanzamos este mensaje
            time.sleep(2)
            os.system("Color B")
            
            #comprobamos si el script se está ejecutando directamente y llamamos a la función principal
if __name__ == "__main__":
    main() #ejecutamos la funcion principal
