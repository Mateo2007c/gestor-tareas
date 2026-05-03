tareas = []

# Usamos un bucle infinito
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
        tarea_nueva = input("Ingrese la tarea a añadir: ")
        tareas.append(tarea_nueva)
        print("¡Tarea añadida!")
        
    elif condicion == 2: 
        print("\n--- TUS TAREAS ---")
        # Imprimimos las tareas con un número al lado para poder borrarlas luego
        for i in range(len(tareas)):
            print(f"{i + 1}. {tareas[i]}")
        print("------------------")
            
    elif condicion == 3:
        print("¡Hasta luego!")
        break # Esta instrucción sale del bucle completamente
        
    elif condicion == 4:
        # Mostramos las tareas antes de pedir cuál borrar
        print(tareas)
        try:
            indice = int(input("Ingrese el NÚMERO de la tarea a eliminar: "))
            # Restamos 1 porque las listas en programación empiezan en el índice 0
            tarea_eliminada = tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
        except ValueError:
            print("Debes ingresar el número de la tarea, no texto.")
        except IndexError:
            # Capturamos el error si intenta borrar, por ejemplo, la tarea 5 y solo hay 2
            print("Ese número de tarea no existe. Intenta de nuevo.")
            
    else:
        print("Opción no válida. Intenta de nuevo.")
