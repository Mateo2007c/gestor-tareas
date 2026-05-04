import json # 1. Importamos la librería estándar para manejar archivos JSON

# 2. Función para cargar las tareas al iniciar el programa
def cargar_tareas():
    try:
        # 'r' significa read (modo lectura)
        with open('tareas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe (la primera vez que abres el programa), devolvemos lista vacía
        return []

# 3. Función para guardar las tareas en el disco duro
def guardar_tareas():
    # 'w' significa write (modo escritura)
    with open('tareas.json', 'w') as archivo:
        json.dump(tareas, archivo)

# Inicializamos nuestra lista usando la función de carga
tareas = cargar_tareas()

def agregar_tarea():
    new_task = input("Ingrese la tarea a añadir: ")
    new_task_dict = {"descripcion": new_task, "completada": False}
    tareas.append(new_task_dict)
    guardar_tareas() # <--- GUARDAMOS TRAS AÑADIR
    print("¡Tarea añadida!")

def mostrar_tareas():
    print("\n--- TUS TAREAS ---")
    if not tareas:
        print("No hay tareas.")
        return

    for i in range(len(tareas)):
        estado = "[X]" if tareas[i]["completada"] else "[ ]"
        print(f"{i + 1}. {estado} {tareas[i]['descripcion']}")
    print("------------------")
    
def eliminar_tarea():
    mostrar_tareas()
    if not tareas:
        return
        
    try:
        indice = int(input("Ingrese el número de tarea a eliminar: "))
        tarea_eliminada = tareas.pop(indice - 1)
        guardar_tareas() # <--- GUARDAMOS TRAS BORRAR
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito")
    except ValueError:
        print("Debes ingresar un número válido.")
    except IndexError: 
        print("El número propuesto no existe.")

def completar_tarea():
    mostrar_tareas()
    if not tareas:
        return

    try:
        numero = int(input("\nIngresa el número de la tarea completada: "))
        indice = numero - 1
        tareas[indice]["completada"] = True
        guardar_tareas() # <--- GUARDAMOS TRAS MARCAR COMPLETADA
        print(f"¡Genial! Marcaste '{tareas[indice]['descripcion']}' como terminada.")
    except ValueError:
        print("Error: Por favor, ingresa un número válido.")
    except IndexError:
        print("Error: Ese número de tarea no existe en la lista.")

# --- BUCLE PRINCIPAL ---
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
        completar_tarea()
    else: 
        print("Opción no válida. Intenta de nuevo.")