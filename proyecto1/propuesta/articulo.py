import random

class Articulo:
    def __init__(self, peso, valor):
        self.peso = peso   # wi: Cantidad de dólares requerida
        self.valor = valor # vi: Beneficio esperado
        self.valorPorPeso = valor/peso  #100$/1kg = 100$, 1$/100kg = 0.01$
        
    def getValorPorPeso(self):
        return self.valorPorPeso

    def getPeso(self):
        return self.peso

    def getValor(self):
        return self.valor

    def getValorPorPeso(self):
        return self.valorPorPeso