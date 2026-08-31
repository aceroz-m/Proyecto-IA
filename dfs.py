def dfs(listaAdyacencia, nodoInicio, nodoFinal):
    # Pila de nodos por visitar (LIFO, a diferencia de la cola del BFS)
    pilaPendientes = [nodoInicio]
    # Set de nodos visitados
    visitados = {nodoInicio}
    # Mapa de padres
    padres = {nodoInicio: None}

    while pilaPendientes:
        # Tomamos el último nodo agregado y lo eliminamos
        nodoActual = pilaPendientes.pop()

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
                pilaPendientes.append(vecino)

    return None