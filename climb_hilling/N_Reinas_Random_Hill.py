# N(S) = Una reina aleatoria variara de su fila
# F = Soluciones factibles, incluye reinas que se atacan
# costo = numero de ataques entre reinas

# Importar
from random import randint
import copy

# Configuraciones iniciales
N = 4
MAX_ITERACIONES = 100   # Reinicios maximos
MAX_INTENTOS = 50     # Intentos maximos

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


def tiempo_aleatorio():
    return randint(1, MAX_INTENTOS)

def random_restart_hill_climbing():
    t:int  = 0                                      # Iteraciones de tiempo
    solucion: Tablero = Tablero()                   # Solucion actual
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
        solucion = Tablero()
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



