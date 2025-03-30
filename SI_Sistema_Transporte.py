import networkx as nx
import matplotlib.pyplot as plt
from kanren import Relation, facts, run, var

# 🔹 Definimos una relación de conexiones con tráfico (peso)
conectado = Relation()
facts(conectado, 
      ("A", "B", 1), ("B", "C", 2), ("A", "D", 4),
      ("C", "D", 1), ("D", "E", 3), ("C", "E", 2), ("A", "E", 10))

# 🔹 Función para encontrar rutas considerando tráfico
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

# 🔹 Buscamos la mejor ruta de A a E
rutas = ruta("A", "E")
mejor_ruta, mejor_costo = min(rutas, key=lambda r: r[1])

print("Posibles rutas:", rutas)
print(f"Mejor ruta: {mejor_ruta} con costo {mejor_costo}")

# 🔹 Creamos el grafo
G = nx.DiGraph()

# Agregamos las conexiones al grafo
conexiones = [
    ("A", "B", 1), ("B", "C", 2), ("A", "D", 4),
    ("C", "D", 1), ("D", "E", 3), ("C", "E", 2), ("A", "E", 10)
]
for origen, destino, peso in conexiones:
    G.add_edge(origen, destino, weight=peso)

# 🔹 Dibujamos el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
plt.figure(figsize=(8,6))

# Dibujamos los nodos y conexiones
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", edge_color="gray", font_size=12, font_weight="bold")

# Dibujamos los pesos de las conexiones
edge_labels = {(origen, destino): peso for origen, destino, peso in conexiones}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# 🔹 Resaltamos la mejor ruta
ruta_edges = [(mejor_ruta[i], mejor_ruta[i+1]) for i in range(len(mejor_ruta)-1)]
nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color="red", width=2.5)

plt.title(f"Mejor ruta de A a E (costo: {mejor_costo})", fontsize=14)
plt.show()
