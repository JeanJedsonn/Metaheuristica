# N(S) = Una reina aleatoria variara de su fila
# F = Soluciones factibles, incluye reinas que se atacan
# costo = numero de ataques entre reinas

# Importar
from random import randint
import copy
import math
import chess

# Add parent directory to path to allow importing from librerias
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from librerias.tablero import Tablero

board = chess.Board()

# Configuraciones iniciales
N = 8
MAX_ITERACIONES = 10000   # Reinicios maximos
TEMPERATURA_INICIAL = 100


def simulated_annealing():
    # Inicializar el estado actual
    estado_actual:Tablero   = Tablero(n=N)                 # Tablero inicial
    costo_actual:int        = estado_actual.costo()     # Costo del tablero inicial
    vecino:Tablero          = Tablero(n=N)                 # Vecino aleatorio
    costo_vecino:int        = vecino.costo()            # Costo del vecino
    iteraciones:int         = 0                         # Iteraciones
    
    # Inicializar la temperatura
    # No se usa una funcion para decrementar la temperatura, basta con restarle 1
    temperatura:int     = TEMPERATURA_INICIAL       # Temperatura inicial
    random:int          = 0                         # Numero aleatorio
    probabilidad:float  = 0                         # Probabilidad
    
    # Bucle principal
    while (temperatura > 1 and costo_actual > 0):
        iteraciones     = 0
        # en este caso el bucle es redundante, las iteraciones las hace la temperatura inicial
        while (iteraciones < MAX_ITERACIONES and costo_actual > 0):
            
            costo_actual    = estado_actual.costo()             # Costo del tablero
            vecino          = copy.copy(estado_actual.vecino_aleatorio())  # Vecino aleatorio
            costo_vecino    = vecino.costo()                    # Costo del vecino
            delta_costo     = costo_vecino - costo_actual       # Diferencia de costos



            # Si el vecino es mejor que la solucion actual
            if (delta_costo < 0):
                estado_actual = copy.copy(vecino)                      # Actualizar la solucion actual
                costo_actual = costo_vecino

            else:
                random = randint(0, 100)/100                # Numero aleatorio
                probabilidad = math.exp(-delta_costo / temperatura)  # Probabilidad de aceptar el vecino

                # Si el numero aleatorio es menor que la probabilidad
                if (random < probabilidad):                   
                    estado_actual = copy.copy(vecino)                    # Actualizar la solucion actual
                    costo_actual = costo_vecino
            
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