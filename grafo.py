import os

class Grafo:
    def cargarLaberinto(ruta_archivo):
        matriz = []
        inicio = None
        meta = None
        
        with open(ruta_archivo, 'r') as f:
            for i, linea in enumerate(f):
                # Limpiar caracteres
                linea_limpia = (
                    linea.strip()
                    .replace('[', '')
                    .replace(']', '')
                    .replace('(', '')
                    .replace(')', '')
                    .replace(',', ' ')
                    .replace("'", '')
                    .replace('"', '')
                )
                
                if not linea_limpia:
                    continue
                    
                # Convertir a enteros solo los elementos que contengan dígitos válidos
                fila = [int(val) for val in linea_limpia.split() if val.isdigit()]
                
                if not fila:
                    continue
                    
                matriz.append(fila)
                
                for j, val in enumerate(fila):
                    if val == 2:
                        inicio = (i, j)
                    elif val == 3:
                        meta = (i, j)
                    
        return matriz, inicio, meta
    
    def matrizAdyacencia(matriz):
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
                            lista_adyacencia[nodo_actual].append(((nr, nc), 1))
                            
        return lista_adyacencia

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    # funcion heuristica
    def h(self, n):
        #inserte su codigo aqui
        return H[n] # puede retornar una lista con el calculo de la heuristica para cada estado

    def primero_profundidad(self, nodo_inicio, nodo_final):
    #inserte si codigo aqui
        return None
        
    def primero_anchura(self, nodo_inicio, nodo_final):
    #inserte si codigo aqui
        return None
    
    def a_estrella(self, nodo_inicio, nodo_final):
    #inserte si codigo aqui
        return None
    
if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_txt = os.path.join(directorio_actual, "laberinto.txt")

    
    matriz, inicio, meta = Grafo.cargarLaberinto(ruta_txt)

    print("Nodo Inicio:", inicio)
    print("Nodo Meta:", meta)
    lista_adyacencia = Grafo.matrizAdyacencia(matriz)
