def dfs(listaAdyacencia, nodoInicio, nodoFinal):
    # Pila de nodos por visitar (LIFO, a diferencia de la cola del BFS)
    pilaPendientes = [nodoInicio]
    # Set de nodos visitados
    visitados = set()
    # Mapa de padres
    padres = {nodoInicio: None}

    while pilaPendientes:
        # Tomamos el último nodo agregado y lo eliminamos
        nodoActual = pilaPendientes.pop()
        visitados.add(nodoActual)

        if nodoActual == nodoFinal:
            camino = []
            actual = nodoFinal

            while actual is not None:
                camino.append(actual)
                actual = padres[actual]

            camino.reverse()
            return camino, len(visitados)

        for item in listaAdyacencia[nodoActual]:
            vecino = item[0] if isinstance(item, (tuple, list)) and isinstance(item[0], tuple) else item
            if vecino not in visitados:
                padres[vecino] = nodoActual
                pilaPendientes.append(vecino)

    return None, len(visitados)