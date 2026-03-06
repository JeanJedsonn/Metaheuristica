# N(S) = Una reina aleatoria variara de su fila
# F = Soluciones factibles, incluye reinas que se atacan
# costo = numero de ataques entre reinas

# Importar
import sys
import os
from random import randint
import copy
import
# Add parent directory to path to allow importing from librerias
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from librerias.tablero import Tablero

# Configuraciones iniciales
N = 8
MAX_ITERACIONES = 100   # Reinicios maximos
MAX_INTENTOS = 50     # Intentos maximos

def GRASP():
    costoActual: int = 1000
    while (costoActual > 0):
        solucionInicial = construirSolInicial()
        solucionLocal = busquedaLocal(solucionInicial)
        if (solucionLocal.costo() < costoActual):
            costoActual = solucionLocal.costo()
    
def main():
    GRASP()

if __name__ == "__main__":
    main()
