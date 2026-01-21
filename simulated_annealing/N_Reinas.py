# N(S) = Una reina aleatoria variara de su fila
# F = Soluciones factibles, incluye reinas que se atacan
# costo = numero de ataques entre reinas

# Importar
from random import randint
import copy
import math
import chess

board = chess.Board()

# Configuraciones iniciales
N = 8                         # Reinas
MAX_ITERACIONES = 10000       # Busquedas maximas para la temperatura t
TEMPERATURA_INICIAL = 100     # Temperatura inicial

class Tablero:
    tablero: list[int]
    
    def __init__(self, tablero_inicial=None):
        if tablero_inicial is None:
            self.tablero = self.generar_tablero_aleatorio()
        else:
            self.tablero = tablero_inicial

    # Genera un tablero aleatorio
    def generar_tablero_aleatorio(self):
        tablero = []
        for i in range(N):
            tablero.append(randint(0, N-1))
        return tablero

    # retorna la cantidad de ataques entre reinas
    def costo(self):
        errores = 0

        #Ataques en diagonales
        for i in range(N):
            # es un vector, se debe evaluar con respecto a los otros elementos
            for j in range(N):
                if i == j:
                    continue
                if abs(self.tablero[i] - self.tablero[j]) == abs(i - j):
                    errores += 1

        #Ataques en filas
        # columna de 0 a N-1
        for i in range(N):
            # fila de i+1 a N-1
            for j in range(i+1, N):
                if self.tablero[i] == self.tablero[j]:
                    errores += 1
        return errores

    # Mueve una reina aleatoria a una fila aleatoria
    def mover_reina_aleatoria(self):
        reina = randint(0, N-1)
        fila = randint(0, N-1)
        self.tablero[reina] = fila

    # retorna un vecino aleatorio (OBJETO Tablero, no lista)
    def vecino_aleatorio(self):
        nuevo_tablero_lista = copy.copy(self.tablero)
        vecino = Tablero(nuevo_tablero_lista)
        vecino.mover_reina_aleatoria()
        return vecino

def simulated_annealing():
    # Inicializar el estado actual
    estado_actual:Tablero   = Tablero()                 # Tablero inicial
    costo_actual:int        = estado_actual.costo()     # Costo del tablero inicial
    vecino:Tablero          = Tablero()                 # Vecino aleatorio
    costo_vecino:int        = vecino.costo()            # Costo del vecino
    iteraciones:int         = 0                         # Iteraciones
    
    # Inicializar la temperatura
    # No se usa una funcion para decrementar la temperatura, basta con restarle 1
    temperatura:int     = TEMPERATURA_INICIAL       # Temperatura inicial
    random:int          = 0                         # Numero aleatorio
    probabilidad:float  = 0                         # Probabilidad
    
    # Bucle principal, control de temperatura
    while (temperatura > 1 and costo_actual > 0):
        iteraciones     = 0
        # bucle interno, busqueda de vecinos
        while (iteraciones < MAX_ITERACIONES and costo_actual > 0):
            
            costo_actual    = estado_actual.costo()                            # Costo del tablero
            vecino          = copy.copy(estado_actual.vecino_aleatorio())      # Vecino aleatorio
            costo_vecino    = vecino.costo()                                   # Costo del vecino
            delta_costo     = costo_vecino - costo_actual                      # Diferencia de costos



            # Si el vecino es mejor que la solucion actual
            if (delta_costo < 0):
                estado_actual = copy.copy(vecino)                        # Actualizar la solucion actual
                costo_actual = costo_vecino                              # Actualizar el costo actual

            else:
                random = randint(0, 100)/100                             # Numero aleatorio
                probabilidad = math.exp(-delta_costo / temperatura)      # Probabilidad de aceptar el vecino

                # Si el numero aleatorio es menor que la probabilidad
                if (random < probabilidad):                   
                    estado_actual = copy.copy(vecino)                    # Actualizar la solucion actual
                    costo_actual = costo_vecino                          # Actualizar el costo actual
            
            iteraciones += 1

        # Decrementar la temperatura
        temperatura *= 0.99
        print("Temperatura:", temperatura)
    
    return estado_actual

def main():
    solucion = simulated_annealing()
    board = chess.Board()
    board.clear_board()
    for i in range(N):
        board.set_piece_at(chess.square(i, solucion.tablero[i]), chess.Piece(chess.QUEEN, chess.WHITE))
    print(board)
    print("Mejor solucion encontrada:", solucion.tablero)
    print("Costo:", solucion.costo())

if __name__ == "__main__":
    main()
