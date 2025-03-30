from kanren import Relation, facts, run, var

# Definimos una relación "conectado"
conectado = Relation()

# Agregamos hechos (conexiones entre estaciones)
facts(conectado, 
      ("A", "B"), ("B", "C"), ("A", "D"),
      ("C", "D"), ("D", "E"), ("C", "E"),("A","E"))

# Función recursiva para encontrar una ruta entre dos puntos
def ruta(origen, destino, camino=[]):
    if origen == destino:
        return [camino + [destino]]

    posibles_rutas = []
    x = var()  # Variable lógica

    # Buscamos nodos conectados con el origen
    conexiones = run(0, x, conectado(origen, x))  # Se usa correctamente `conectado(origen, x)`

    for siguiente in conexiones:
        if siguiente not in camino:  # Evitamos ciclos
            nuevas_rutas = ruta(siguiente, destino, camino + [origen])
            posibles_rutas.extend(nuevas_rutas)

    return posibles_rutas

# Ejecutamos la búsqueda de la mejor ruta de A a E
rutas = ruta("A", "E")
if rutas:
    print("Posibles rutas:", rutas)
    print("La mejor ruta es:", min(rutas, key=len))  # Escogemos la más corta
else:
    print("No hay ruta disponible de A a E.")
