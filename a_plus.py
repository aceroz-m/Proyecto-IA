 
import heapq

def h(nodo, meta):
    # Distancia de manhathan como funcion heuristica, es la ideal debido a que no nos exponemos a problemas de punto flotante
    # Ademas representa adecuadamente el numero de movimientos 'ideales' para llegar a la meta
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])

def calcular_heuristica(nodos, meta):
    # Funcion de conveniencia para inicializar una lista con la funcion h
    lista_h = {}
    for n in nodos:
        lista_h[n] = h(n, meta)
    return lista_h

def f(g, nodo, lista_h):
    # Funcion de evaluacion f(n) = g(n) + h(n)
    return g[nodo] + lista_h[nodo]



def a_plus(lista_adyacencia, inicio, meta):

    # Lista de nodos y calculo de heuristica
    nodos = [n for n, _ in lista_adyacencia.items()]
    lista_h = calcular_heuristica(nodos, meta)

    # Lista de padres para reconstruir el camino
    padres = {}

    # Funcion g que evalua el costo del camino desde el nodo inicial hasta el nodo actual
    g = {inicio: 0}

    pq = []

    padres[inicio] = None

    # Metodo de python para usar una cola de prioridad
    heapq.heappush(pq, (f(g, inicio, lista_h), inicio))

    while pq:
        _, u = heapq.heappop(pq)

        # Camino encontrado
        if u == meta:
            break

        # Actualziacion de funcion g
        nuevo_g = g[u] + 1
        for v in lista_adyacencia[u]:

            # Si el nodo no ha sido visitado, o si se llega a este nodo de manera mas eficiente
            if v not in g or nuevo_g < g[v]:
                g[v] = nuevo_g
                padres[v] = u
                heapq.heappush(pq, (f(g, v, lista_h),v))

    camino = []

    # Reconstruccion del camino
    it = meta
    while it is not None:
        camino.append(it)
        it = padres.get(it)

    camino.reverse()
    return camino