import os

class Grafo:
    def cargar_laberinto(ruta_archivo):
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

    
    matriz, inicio, meta = Grafo.cargar_laberinto(ruta_txt)

    print("Nodo Inicio (2):", inicio)
    print("Nodo Meta (3):", meta)