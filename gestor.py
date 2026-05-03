tareas = []

# Usamos un bucle infinito
while True:
    condicion = int(input("""
1. Añadir tarea
2. Ver tareas
3. Salir
Elige una opción: """))
    
    if condicion == 1:
        tarea_nueva = input("Ingrese la tarea a añadir: ")
        tareas.append(tarea_nueva)
    elif condicion == 2: 
        print(tareas)
    elif condicion == 3:
        print("¡Hasta luego!")
        break # Esta instrucción sale del bucle completamente
    else:
        print("Opción no válida. Intenta de nuevo.")

