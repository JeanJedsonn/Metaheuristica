from typing import List
from config import datos_items, MAX_ITERACIONES, TEMPERATURA_INICIAL, CAPACIDAD_MOCHILA
from mochila import Mochila
from articulo import Articulo
from copy import copy

import math
from random import randint

def main():
    #inicializar el estado inicial
    iteraciones:int     = 0
    vecino:Mochila      = None
    items:List[Articulo] = inicializar_items()
    mochila:Mochila     = Mochila(CAPACIDAD_MOCHILA)
    mochila.llenar_mochila(items)

    print("Estado inicial: ", mochila.costo(), "Peso: ", mochila.get_peso(), "Capacidad: ", mochila.get_capacidad())

    #inicializar la temperatura
    temperatura:int     = TEMPERATURA_INICIAL
    probabilidad:float  = 0
    random:float        = 0

    #bucle principal
    while (temperatura > 1):
        #bucle interno
        iteraciones = 0
        while (iteraciones < MAX_ITERACIONES):
            #generar vecino
            vecino = copy(mochila)
            vecino.vecino_aleatorio_2(items)
            delta_costo = mochila.costo() - vecino.costo()       # si negativo es mejor, si positivo es peor

            #print("Valor actual: ", mochila.costo(), "Peso: ", mochila.get_peso(), "Capacidad: ", mochila.get_capacidad())
            #print("Valor vecino: ", vecino.costo(), "Peso: ", vecino.get_peso(), "Capacidad: ", vecino.get_capacidad())

            #FIX: no se esta cumpliendo la condicion de que el vecino sea factible y tiene a empeorar (sobrepeso)
            if ( vecino.capacidad_suficiente() and delta_costo < 0):
                print("Mejorando: ")
                print(" * Costo Actual: ", mochila.costo(), " -> Costo Vecino: ", vecino.costo())
                print(" * Peso Actual: ", mochila.get_peso(), " -> Peso Vecino: ", vecino.get_peso())
                mochila = copy(vecino)

            #si el vecino es peor o no es factible
            else:
                random = randint(0, 100)/100                # Numero aleatorio
                probabilidad = math.exp(delta_costo / temperatura)  # Probabilidad de aceptar el vecino
                if probabilidad > 1:
                    print("Delta: ", delta_costo)
                    print("Temperatura: ", temperatura)

                print("Probabilidad: ", probabilidad)
                print("Random: ", random)
                if (random < probabilidad):
                    print("Empeorando: ")
                    print(" * Costo Actual: ", mochila.costo(), " -> Costo Vecino: ", vecino.costo())
                    print(" * Valor Actual: ", mochila.get_valor(), " -> Valor Vecino: ", vecino.get_valor())
                    print(" * Peso Actual: ", mochila.get_peso(), " -> Peso Vecino: ", vecino.get_peso())
                    mochila = copy(vecino)

            iteraciones += 1
            
        #enfriamiento
        temperatura *= 0.99

    print("Mejor solucion: ", mochila.get_valor(), "Peso: ", mochila.get_peso(), "Capacidad: ", mochila.get_capacidad())
    return mochila

def inicializar_items(): 
    items:List[Articulo] = []
    for item in datos_items:
        items.append(Articulo(item[0], item[1]))
    return items

if __name__ == "__main__":
    main()