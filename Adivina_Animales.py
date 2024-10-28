#Adivina quién con aprendizaje sin base de datos

animales = {
    "León": {"tipo_piel": "pelaje", "numero_patas": 4, "tamaño": "grande", "es_domestico": False, "vuela": False},
    "Elefante": {"tipo_piel": "piel dura", "numero_patas": 4, "tamaño": "grande", "es_domestico": False, "vuela": False},
    "Águila": {"tipo_piel": "plumas", "numero_patas": 2, "tamaño": "mediano", "es_domestico": False, "vuela": True},
    "Gato": {"tipo_piel": "pelaje", "numero_patas": 4, "tamaño": "pequeño", "es_domestico": True, "vuela": False},
    "Perro": {"tipo_piel": "pelaje", "numero_patas": 4, "tamaño": "pequeño", "es_domestico": True, "vuela": False},
}

def aplicar_regla(pregunta, valor, base_conocimiento):
    """Filtra los animales de la base de conocimiento según una característica específica."""
    return {animal: caracteristicas for animal, caracteristicas in base_conocimiento.items() if caracteristicas.get(pregunta) == valor}

def obtener_valores_disponibles(pregunta, base_conocimiento):
    """Obtiene todos los valores únicos para una característica específica entre los animales restantes."""
    return set(caracteristicas[pregunta] for caracteristicas in base_conocimiento.values())

def iniciar_juego():
    """Inicia el juego de adivinanza."""
    base_conocimiento = animales.copy()
    print("Bienvenido al juego de Adivina quién - Animales")
    print("Responde con 'si' o 'no' a las siguientes preguntas:")

    preguntas = list(base_conocimiento[list(base_conocimiento.keys())[0]].keys())
    
    while len(base_conocimiento) > 1 and preguntas:
        pregunta = preguntas.pop(0)
        valores_disponibles = obtener_valores_disponibles(pregunta, base_conocimiento)
        
        for valor in valores_disponibles:
            respuesta = input(f"¿El animal tiene {pregunta.replace('_', ' ')} '{valor}'? ").strip().lower()
            
            if respuesta == 'si':
                base_conocimiento = aplicar_regla(pregunta, valor, base_conocimiento)
                break
            elif respuesta == 'no':
                base_conocimiento = {animal: caracteristicas for animal, caracteristicas in base_conocimiento.items() if caracteristicas.get(pregunta) != valor}
                break
            else:
                print("Respuesta no válida. Responde con 'si' o 'no'.")
                continue
        
        if len(base_conocimiento) == 1:
            print(f"¡He adivinado! El animal es: {list(base_conocimiento.keys())[0]}")
            return

    if len(base_conocimiento) > 1:
        print("No pude adivinar exactamente. Hay varios animales posibles.")
    elif len(base_conocimiento) == 0:
        print("No pude adivinar el animal.")
    else:
        print(f"¡He adivinado! El animal es: {list(base_conocimiento.keys())[0]}")

def agregar_animal():
    """Permite al usuario agregar un nuevo animal a la base de conocimiento."""
    nombre = input("Introduce el nombre del nuevo animal: ").strip()
    if nombre in animales:
        print("Ese animal ya existe en la base de conocimiento.")
        return
    
    caracteristicas = {}
    for pregunta in animales[list(animales.keys())[0]].keys():
        respuesta = input(f"¿El animal tiene {pregunta.replace('_', ' ')}? (si/no): ").strip().lower()
        caracteristicas[pregunta] = True if respuesta == 'si' else False
    
    animales[nombre] = caracteristicas
    print(f"El animal '{nombre}' ha sido agregado exitosamente.")

def agregar_pregunta():
    """Permite al usuario agregar una nueva pregunta para los animales existentes."""
    nueva_pregunta = input("Introduce la nueva pregunta (ejemplo: 'es_acuatico', 'tiene_escamas'): ").strip()
    if nueva_pregunta in animales[list(animales.keys())[0]]:
        print("Esa pregunta ya existe.")
        return

    # Añadir la nueva pregunta a todos los animales
    for animal in animales:
        respuesta = input(f"¿El animal '{animal}' tiene {nueva_pregunta.replace('_', ' ')}? (si/no): ").strip().lower()
        animales[animal][nueva_pregunta] = True if respuesta == 'si' else False

    print(f"La nueva pregunta '{nueva_pregunta}' ha sido agregada exitosamente a todos los animales.")

def menu_principal():
    """Muestra el menú principal del juego."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar juego")
        #print("2. Agregar nuevo animal")
        print("2. Agregar nueva pregunta")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == '1':
            iniciar_juego()
        elif opcion == '2':
            agregar_pregunta()
        elif opcion == '3':
        #    agregar_pregunta()
        #elif opcion == '4':
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú principal
menu_principal()