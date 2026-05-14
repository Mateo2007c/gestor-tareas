import json

# 1. Clase que representa una sola Tarea
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion # Atributo de dato
        self.completada = completada   # Atributo de dato
        
    def marcar_completada(self):
        self.completada = True         # Comportamiento (Método)

# 2. Clase que representa nuestra Aplicación completa
class GestorTareas:
    def __init__(self):
        # Al crearse el gestor, automáticamente carga las tareas del JSON
        self.tareas = self.cargar_tareas()
        
    def cargar_tareas(self):
        try:
            with open('tareas.json', 'r') as archivo:
                datos = json.load(archivo)
                # Magia de Python: Convertimos los diccionarios del JSON a objetos Tarea
                return [Tarea(t['descripcion'], t['completada']) for t in datos]
        except FileNotFoundError:
            return []
            
    def guardar_tareas(self):
        # Magia de Python: Convertimos los objetos Tarea a diccionarios para el JSON
        datos = [{'descripcion': t.descripcion, 'completada': t.completada} for t in self.tareas]
        with open('tareas.json', 'w') as archivo:
            json.dump(datos, archivo)

    def agregar_tarea(self):
        nueva_descripcion = input("Ingrese la tarea a añadir: ")
        # Creamos un nuevo "Objeto" Tarea
        nueva_tarea = Tarea(nueva_descripcion)
        self.tareas.append(nueva_tarea)
        self.guardar_tareas() # Guardamos tras modificar
        print("¡Tarea añadida!")

    def mostrar_tareas(self):
        print("\n--- TUS TAREAS ---")
        if not self.tareas:
            print("No hay tareas.")
            return
        for i in range(len(self.tareas)):
            # Como ahora es un objeto, accedemos a sus atributos con un PUNTO
            tarea_actual = self.tareas[i]
            estado = "[X]" if tarea_actual.completada else "[ ]"
            print(f"{i + 1}. {estado} {tarea_actual.descripcion}")
        print("------------------")

    # 👇 TU RETO: Define aquí los métodos eliminar_tarea(self) y completar_tarea(self) 👇
    # Pista para completar: en vez de tareas[indice]["completada"] = True, 
    def eliminar_tarea(self):
        try:
            numero = int(input("Ingrese el numero de la tarea a eliminar: "))
            # Calculamos el índice restando 1
            indice = numero - 1 
            tarea_eliminada = self.tareas.pop(indice)
            self.guardar_tareas()
            # Usamos el PUNTO para acceder a la descripción del objeto
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada con éxito")
        except ValueError:
            print("Debes ingresar un número válido.")
        except IndexError: 
            print("El número propuesto no existe.")
    
    def completar_tarea(self):
        self.mostrar_tareas()
        if not self.tareas:
            return
        
        try:
            numero = int(input("Ingrese el numero de la tarea a completar: "))
            # Calculamos el índice exacto para evitar el error Off-by-one
            indice = numero - 1 
            
            self.tareas[indice].marcar_completada()
            self.guardar_tareas()
            # Usamos el PUNTO para acceder al atributo
            print(f"¡Genial! Marcaste '{self.tareas[indice].descripcion}' como terminada.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
        except IndexError:
            print("Error: Ese número de tarea no existe en la lista.")
        


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
    else: 
        print("Opción no válida. Intenta de nuevo.")