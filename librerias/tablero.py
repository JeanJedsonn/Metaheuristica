import copy
from random import randint

class Tablero:
    tablero: list[int]
    
    def __init__(self, tablero_inicial=None, n=4):
        if tablero_inicial is None:
            self.n = n
            self.tablero = self.generar_tablero_aleatorio()
        else:
            self.tablero = tablero_inicial
            self.n = len(self.tablero)

    # Genera un tablero aleatorio
    def generar_tablero_aleatorio(self):
        tablero = []
        for i in range(self.n):
            tablero.append(randint(0, self.n-1))
        return tablero

    # retorna la cantidad de ataques entre reinas
    def costo(self):
        errores = 0
        N = self.n

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
        N = self.n
        reina = randint(0, N-1)
        fila = randint(0, N-1)
        self.tablero[reina] = fila

    # retorna un vecino aleatorio (OBJETO Tablero, no lista)
    def vecino_aleatorio(self):
        nuevo_tablero_lista = copy.copy(self.tablero)
        vecino = Tablero(tablero_inicial=nuevo_tablero_lista)
        vecino.mover_reina_aleatoria()
        return vecino