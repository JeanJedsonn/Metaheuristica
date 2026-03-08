from typing import List
import random
from articulo import Articulo

class Mochila:
    def __init__(self, capacidad):
        self.peso:      float = 0           # Peso total de los items en la mochila
        self.valor:     float = 0              # Valor total de los items en la mochila
        self.capacidad: float = capacidad              # Capacidad maxima de la mochila
        self.items:     List[Articulo] = []    # Lista de items en la mochila
        self.totalItems:int = 0                # Total de items en la mochila

        self.mediaPeso:     float = 0          # Media del peso de los items
        self.mediaValor:    float = 0          # Media del valor de los items
        self.varianzaPeso:  float = 0          # Varianza del peso de los items
        self.varianzaValor: float = 0          # Varianza del valor de los items

    # ---------- # ---------- # ---------- #
    #          METODOS ELEMENTALES         #
    # ---------- # ---------- # ---------- #

    # agrega un item a la mochila
    def agregar_item(self, item:Articulo):
        self.items.append(item)         # agrega el item a la lista de items
        self.peso += item.peso          # suma el peso del item al peso total
        self.valor += item.valor        # suma el valor del item al valor total
        self.totalItems += 1            # incrementa el total de items

        self.mediaPeso = self.peso / self.totalItems    # media del peso de los items
        self.mediaValor = self.valor / self.totalItems  # media del valor de los items
        self.varianzaPeso = self.varianzaPeso + (item.peso - self.mediaPeso) ** 2  # varianza del peso de los items
        self.varianzaValor = self.varianzaValor + (item.valor - self.mediaValor) ** 2  # varianza del valor de los items

    # elimina un item de la mochila
    def eliminar_item(self, item:Articulo):
        self.peso -= item.peso          # resta el peso del item de la mochila
        self.valor -= item.valor        # resta el valor del item de la mochila
        self.totalItems -= 1            # decrementa el total de items
        self.items.remove(item)         # elimina el item de la lista de items

        if self.totalItems > 0:
            self.mediaPeso = self.peso / self.totalItems                                    # media del peso de los items
            self.mediaValor = self.valor / self.totalItems                                  # media del valor de los items
            self.varianzaPeso = self.varianzaPeso + (item.peso - self.mediaPeso) ** 2       # varianza del peso de los items
            self.varianzaValor = self.varianzaValor + (item.valor - self.mediaValor) ** 2   # varianza del valor de los items
        else:
            self.mediaPeso = 0
            self.mediaValor = 0
            self.varianzaPeso = 0
            self.varianzaValor = 0

    # retorna la lista de los items
    def get_items(self):
        return self.items

    # retorna el peso total de la mochila
    def get_peso(self):
        return self.peso

    # retorna la capacidad maxima de la mochila
    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    # retorna el valor total de la mochila
    def get_valor(self):
        return self.valor

    # retorna el peso medio de los items
    def get_peso_medio(self):
        return self.peso / self.totalItems

    def get_valor_medio(self):
        return self.valor / self.totalItems

    def get_item_aleatorio(self):
        return random.choice(self.items)
    

    # verifica si la mochila tiene capacidad suficiente
    def capacidad_suficiente(self):
        return self.peso <= self.capacidad

    # retorna el costo de la mochila por unidad de peso
    def costo(self):
        return self.valor/self.peso

    # ---------- # ---------- # ---------- #
    #          METODOS COMPLEJOS           #
    # ---------- # ---------- # ---------- #

    def llenar_mochila(self, items:List[Articulo]):
        for item in items:
            if self.capacidad_suficiente():
                self.agregar_item(item)

    # convierte la mochila en un vecino aleatorio
    def vecino_aleatorio(self, items:List[Articulo]):        
        # elige un item aleatorio para agregar o intercambiar
        item = random.choice(items)           # elige un item aleatorio de la mochila

        # caso 1, remover el item de la mochila
        if item in self.items:                   # si el item esta en la mochila
            self.eliminar_item(item)               # elimina el item de la mochila
        
        else:                                      # si el item no esta en la mochila
            # caso 2, hay espacio para agregarlo
            if self.get_peso() + item.peso <= self.capacidad:
                self.agregar_item(item)            # agrega el item a la mochila
            # caso 3, no hay espacio para agregarlo
            else:
                # elige un item aleatorio para remover
                item_a_remover = random.choice(self.items)
                self.eliminar_item(item_a_remover) # elimina el item de la mochila
                self.agregar_item(item)            # agrega el item a la mochila, puede sobrepasar la capacidad

    def vecino_aleatorio_2(self, items:List[Articulo]):        
        item_lista = random.choice(items)           # elige un item aleatorio de la mochila
        item_mochila = random.choice(self.items)    # elige un item aleatorio de la mochila
        
        # caso 1, remover el item de la mochila
        if item_lista in self.items:
            self.eliminar_item(item_lista)
            return
        
        # caso 2, la mochila tiene capacidad suficiente para intentar mejorarla
        if self.get_peso()+item_lista.peso <= self.capacidad:
            self.agregar_item(item_lista)
        
        # caso 3, la mochila no tiene capacidad suficiente, se intentara intercambiar o eliminar
        else:
            if item_mochila.peso > item_lista.peso:
                self.eliminar_item(item_mochila)
                self.agregar_item(item_lista)
            else:
                self.eliminar_item(item_mochila)

