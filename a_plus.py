 
import heapq

def h(nodo, meta):
    # Distancia de manhathan como funcion heuristica, es la ideal debido a que no nos exponemos a problemas de punto flotante
    # Ademas representa adecuadamente el numero de movimientos 'ideales' para llegar a la meta
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])

def calcular_heuristica(nodos, meta):
    lista_h = {}
    for nodo in nodos:
        lista_h[nodo] = h(nodo, meta)
    return lista_h

def f(g, nodo, lista_h):
    # Funcion de evaluacion f(n) = g(n) + h(n)
    return g[nodo] + lista_h[nodo]



def a_plus(lista_adyacencia, inicio, meta):

    # Lista de nodos y calculo de heuristica
    nodos = list(lista_adyacencia.keys())
    lista_h = calcular_heuristica(nodos, meta)

    # Lista de padres para reconstruir el camino
    padres = {}

    # Funcion g que evalua el costo del camino desde el nodo inicial hasta el nodo actual
    g = {inicio: 0}

    pq = []

    padres[inicio] = None

    # Metodo de python para usar una cola de prioridad
    heapq.heappush(pq, (f(g, inicio, lista_h), inicio))

    # Conjunto para rastrear nodos expandidos
    visitados = set()

    while pq:
        _, u = heapq.heappop(pq)

        if u in visitados:
            continue

        visitados.add(u)

        # Camino encontrado
        if u == meta:
            break

        # Actualziacion de funcion g
        for item in lista_adyacencia[u]:
            v = item[0] if isinstance(item, (tuple, list)) and isinstance(item[0], tuple) else item
            peso = item[1] if isinstance(item, (tuple, list)) and len(item) >= 2 else 1
            nuevo_g = g[u] + peso

            # Si el nodo no ha sido visitado, o si se llega a este nodo de manera mas eficiente
            if v not in g or nuevo_g < g[v]:
                g[v] = nuevo_g
                padres[v] = u
                heapq.heappush(pq, (f(g, v, lista_h), v))

    camino = []

    # Reconstruccion del camino
    if meta in padres:
        it = meta
        while it is not None:
            camino.append(it)
            it = padres.get(it)

        camino.reverse()
    return camino, len(visitados)
