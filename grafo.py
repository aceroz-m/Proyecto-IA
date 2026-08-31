import os
import ast

from a_plus import a_plus
from bfs import bfs
from dfs import dfs

class Grafo:
    def cargarLaberinto(ruta_archivo):
        with open(ruta_archivo, 'r') as f:
               matriz = [ast.literal_eval(line.strip()) for line in f if line.strip().startswith('[')]

        inicio = next((r, c) for r, row in enumerate(matriz) for c, v in enumerate(row) if v == 2)
        meta = next((r, c) for r, row in enumerate(matriz) for c, v in enumerate(row) if v == 3)
        return matriz, inicio, meta
    
    def listaAdyacencia(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        lista_adyacencia = {}
        
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Arriba, Abajo, Izquierda, Derecha
        
        for r in range(filas):
            for c in range(columnas):
                # Omitir paredes (1)
                if matriz[r][c] == 1:
                    continue
                
                nodo_actual = (r, c)
                lista_adyacencia[nodo_actual] = []
                
                for dr, dc in movimientos:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < filas and 0 <= nc < columnas:
                        if matriz[nr][nc] != 1:
                            # Estructura del grafo ponderado: (nodo_destino, peso)
                            lista_adyacencia[nodo_actual].append(((nr, nc)))
                            
        return lista_adyacencia

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    def primero_profundidad(lista_adyacencia, nodo_inicio, nodo_final):
        return dfs(lista_adyacencia, nodo_inicio, nodo_final)
        
    def primero_anchura(lista_adyacencia, nodo_inicio, nodo_final):
        return bfs(lista_adyacencia, nodo_inicio, nodo_final)

    def a_estrella(lista_adyacencia, nodo_inicio, nodo_final):
        return a_plus(lista_adyacencia, nodo_inicio, nodo_final)
    
if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_txt = os.path.join(directorio_actual, "laberinto.txt")

    
    matriz, inicio, meta = Grafo.cargarLaberinto(ruta_txt)

    print("Nodo Inicio:", inicio)
    print("Nodo Meta:", meta)
    lista_adyacencia = Grafo.listaAdyacencia(matriz)
    print("A*= ", Grafo.a_estrella(lista_adyacencia, inicio, meta))
    print("BFS= ", Grafo.primero_anchura(lista_adyacencia, inicio, meta))
    print("DFS= ", Grafo.primero_profundidad(lista_adyacencia, inicio, meta))