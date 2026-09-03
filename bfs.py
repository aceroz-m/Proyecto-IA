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

        # Si hemos encontrado el final del camino
        if nodoActual == nodoFinal:
            # Creamos un camino
            camino = []
            # Definimos un nodo actual que es el nodo final
            actual = nodoFinal

            # Mientras el nodo actual no sea None, agregamos el nodo actual al camino y actualizamos el nodo actual al padre del nodo actual
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]

            # Volteamos el camino
            camino.reverse()
            # Devolvemos el camino
            return camino, len(visitados) # Devolvemos el camino y la cantidad de nodos visitados

        # Si no es el final del camino, tomamos los vecinos del nodo actual
        for item in listaAdyacencia[nodoActual]:
            vecino = item[0] if isinstance(item, (tuple, list)) and isinstance(item[0], tuple) else item
            # Si el vecino no ha sido visitado lo agregamos a la cola
            if vecino not in visitados:
                visitados.add(vecino)
                # Agregamos el nodo actual como padre del vecino
                padres[vecino] = nodoActual
                # Ponemos en la cola de pendientes por visitar al vecino
                colaPendientes.append(vecino)

    return None, len(visitados) # Si no encontramos un camino, devolvemos None y la cantidad de nodos visitados