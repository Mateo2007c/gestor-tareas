tareas = []

def agregar_tarea():
    new_task = input("Ingrese la tarea a añadir: ")
    # Usamos la clave "descripcion"
    new_task_dict = {"descripcion": new_task, "completada": False}
    tareas.append(new_task_dict)
    print("¡Tarea añadida!")

def mostrar_tareas():
    print("\n--- TUS TAREAS ---")
    if not tareas:
        print("No hay tareas.")
        return

    for i in range(len(tareas)):
        # Imprimimos el estado visual accediendo al diccionario
        estado = "[X]" if tareas[i]["completada"] else "[ ]"
        # Accedemos con la clave "descripcion"
        print(f"{i + 1}. {estado} {tareas[i]['descripcion']}")
    print("------------------")
    
def eliminar_tarea():
    # Reutilizamos la función mostrar_tareas() (Principio DRY)
    mostrar_tareas()
    if not tareas:
        return
        
    try:
        indice = int(input("Ingrese el número de tarea a eliminar: "))
        tarea_eliminada = tareas.pop(indice - 1)
        # Accedemos a la descripción de la tarea eliminada
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito")
    except ValueError:
        print("Debes ingresar un número válido.")
    except IndexError: 
        print("El número propuesto no existe.")

def completar_tarea():
    # Reutilizamos la función mostrar_tareas()
    mostrar_tareas()
    if not tareas:
        return

    try:
        numero = int(input("\nIngresa el número de la tarea completada: "))
        indice = numero - 1
        
        # Cambiar el estado en el diccionario a True
        tareas[indice]["completada"] = True
        print(f"¡Genial! Marcaste '{tareas[indice]['descripcion']}' como terminada.")
    except ValueError:
        print("Error: Por favor, ingresa un número válido.")
    except IndexError:
        print("Error: Ese número de tarea no existe en la lista.")

# Bucle principal
while True:
    try: 
        condicion = int(input("""
1. Añadir tarea
2. Ver tareas
3. Salir
4. Eliminar tarea
5. Completar tarea
Elige una opción: """))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue 
    
    if condicion == 1:
        agregar_tarea()
    elif condicion == 2:
        mostrar_tareas()
    elif condicion == 3:
        print("¡Hasta luego!")
        break
    elif condicion == 4:
        eliminar_tarea()
    elif condicion == 5:
        completar_tarea() # ¡Agregamos la llamada a la opción 5!
    else: 
        print("Opción no válida. Intenta de nuevo.")