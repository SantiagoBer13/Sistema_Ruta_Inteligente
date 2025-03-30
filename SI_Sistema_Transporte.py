from kanren import Relation, facts, run, var, conde

# Definimos una relación "conectado"
conectado = Relation()

facts(conectado, 
      ("A", "B", 1), ("B", "C", 2), ("A", "D", 4),
      ("C", "D", 1), ("D", "E", 3), ("C", "E", 2), ("A", "E", 10))

def ruta(origen, destino, camino=[], costo_total=0):
    if origen == destino:
        return [(camino + [destino], costo_total)]

    posibles_rutas = []
    x, peso = var(), var()

    conexiones = run(0, (x, peso), conectado(origen, x, peso))

    for siguiente, costo in conexiones:
        if siguiente not in camino:
            nuevas_rutas = ruta(siguiente, destino, camino + [origen], costo_total + costo)
            posibles_rutas.extend(nuevas_rutas)

    return posibles_rutas

rutas = ruta("A", "E")
if rutas:
    print("Posibles rutas:", rutas)
    print("La mejor ruta es:", min(rutas, key=lambda r: r[1]))  # Ruta con menor costo
