import json
from modelos import GestorTareas

# --- BUCLE PRINCIPAL ---
# Creamos la INSTANCIA de nuestra aplicación
mi_gestor = GestorTareas()

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
        mi_gestor.agregar_tarea() # Llamamos a los métodos usando el objeto y un punto
    elif condicion == 2:
        mi_gestor.mostrar_tareas()
    elif condicion == 3:
        print("¡Hasta luego!")
        break
    # 👇 TU RETO: Añadir los elif para las opciones 4 y 5 👇
    elif condicion == 4:
        mi_gestor.eliminar_tarea()
    elif condicion == 5:
        mi_gestor.completar_tarea()
    else: 
        print("Opción no válida. Intenta de nuevo.")