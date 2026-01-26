# N(S) = Una reina aleatoria variara de su fila
# F = Soluciones factibles, incluye reinas que se atacan
# costo = numero de ataques entre reinas

# Importar
import sys
import os
from random import randint
import copy

# Add parent directory to path to allow importing from librerias
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from librerias.tablero import Tablero

# Configuraciones iniciales
N = 8
MAX_ITERACIONES = 100   # Reinicios maximos
MAX_INTENTOS = 50     # Intentos maximos




def tiempo_aleatorio():
    return randint(1, MAX_INTENTOS)

def random_restart_hill_climbing():
    t:int  = 0                                      # Iteraciones de tiempo
    solucion: Tablero = Tablero(n=N)                   # Solucion actual
    mejorSolucion: Tablero = copy.copy(solucion)    # Mejor solucion

    #do while, mientras no se cumplan las condiciones de parada
    while True:
        tiempo = tiempo_aleatorio()     # Intentos para encontrar una solucion

        #do while, mientras no se cumplan las condiciones de tiempo aleatorio o solucion
        while True:
            vecino = solucion.vecino_aleatorio()

            # Si el vecino es mejor que la solucion actual
            if (vecino.costo() < solucion.costo()):
                solucion = vecino

                # Si la solucion actual es mejor que la mejor solucion conocida
                if (solucion.costo() < mejorSolucion.costo()):
                    mejorSolucion = copy.copy(solucion)
            
            tiempo -= 1
            
            #do
            if (solucion.costo() == 0 or tiempo == 0):
                break
        
        t += 1
        solucion = Tablero(n=N)
        #do
        if (mejorSolucion.costo() == 0 or t == MAX_ITERACIONES):
            break
    return mejorSolucion

def main():
    mejor = random_restart_hill_climbing()
    print("Mejor solucion encontrada:", mejor.tablero)
    print("Costo:", mejor.costo())

if __name__ == "__main__":
    main()



