from collections import deque

# No se usar python :c

def bfs(listaAdyacencia, nodoInicio, nodoFinal):
    # Cola de nodos por visitar
    colaPendientes = deque([nodoInicio])
    # Set de nodos visitados
    visitados = {nodoInicio}
    # Mapa de padres
    padres = {nodoInicio: None}

    while(colaPendientes):
        # Tomamos el nodo de enfrente y lo eliminamos (esto me parece re ilegal)
        nodoActual = colaPendientes.popleft() 

        if nodoActual == nodoFinal:
            camino = []
            actual = nodoFinal

            while actual is not None:
                camino.append(actual)
                actual = padres[actual]

            camino.reverse()
            return camino

        for vecino in listaAdyacencia[nodoActual]:
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodoActual
                colaPendientes.append(vecino)

    return None