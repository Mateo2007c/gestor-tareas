tareas = []

def agregar_tarea():
    new_task = input("Ingrese la tarea a añadir: ")
    tareas.append(new_task)
    print("¡Tarea añadida!")
    
def eliminar_tarea():
    print(tareas)
    
    try:
        indice = input("Ingrese el numero de tarea a eliminar: ")
        tarea_eliminada = tareas.pop(indice - 1 )
        print(f"Tarea {tarea_eliminada} eliminda con exito")
    except ValueError:
        print("Debes ingresar un numero de la tarea")
    except IndexError: 
        print("El indice propuesto no existe.")
        


def mostrar_tareas():
    print("\n--- TUS TAREAS ---")
    for i in range(len(tareas)):
        print(f"{i - 1}. {tareas[i - 1]}")
    print("------------------")
    

while True:
    try: 
        condicion = int(input("""
1. Añadir tarea
2. Ver tareas
3. Salir
4. Eliminar tarea
Elige una opción: """))
    except ValueError:
        # Manejo del error si el usuario no introduce un número
        print("Por favor, introduce un número válido.")
        continue 
    
    if condicion == 1:
        agregar_tarea()
        
    elif condicion == 2:
        mostrar_tareas()
        
    elif condicion == 3:
        print("Hasta luego")
        break
        
    elif condicion == 4:
        eliminar_tarea()
    
    else: 
        print("Ingrese otra opcion")