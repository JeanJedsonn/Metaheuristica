import random
import math
from articulo import Articulo
from config import DATOS_ITEMS, TEMP_INF, ALFA, CAPACIDAD_MAXIMA_MOCHILA
from funciones import generar_vecino, calcular_varianza, definir_Temp_sup


def main():
    # Definición de los artículos (peso, valor)

    tam_datos_items = len(DATOS_ITEMS)
    
    # Cálculo de la capacidad máxima W (30% del total de pesos)
    suma_items = sum(p for p, v in DATOS_ITEMS) # Suma total de pesos de los artículos
    capacidad_W = math.ceil(CAPACIDAD_MAXIMA_MOCHILA * 0.3)   # Capital total W
    
    items = [Articulo(p, v) for p, v in DATOS_ITEMS]
    

    # Parámetros del Simulated Annealing
    TEMP_SUP = definir_Temp_sup(tam_datos_items, items, capacidad_W)         # Temperatura inicial basada en el muestreo
    T_inf = TEMP_INF                    # Temperatura final
    alfa = ALFA                         # Factor de enfriamiento
    ITERAR = tam_datos_items * 10       # Iteraciones por temperatura

    # Inicialización de la solución
    mochila_actual = [0] * tam_datos_items                                 # Mochila inicialmente vacía
    mejor_solucion = list(mochila_actual)                                  # Mejor solución encontrada
    mejor_varianza = calcular_varianza(mochila_actual, items, capacidad_W) # Varianza de la solución inicial
    
    a, b = 0, 0 # Contadores de ciclos y pasos, no son importantes

    # Ciclo principal del Simulated Annealing
    while TEMP_SUP > T_inf:
        a += 1
        for _ in range(ITERAR):
            b += 1
            
            vecino = generar_vecino(mochila_actual, tam_datos_items)
            v_actual = calcular_varianza(mochila_actual, items, capacidad_W)
            v_vecino = calcular_varianza(vecino, items, capacidad_W)

            # Si el vecino cumple con la restricción de peso
            if v_vecino != -1.0:
                delta = v_vecino - v_actual

                # Criterio de Aceptación de Metropolis
                probabilidad = math.exp(delta / TEMP_SUP) if TEMP_SUP > 0 else 0
                if (delta > 0 or random.random() < probabilidad):
                    mochila_actual = vecino
                    
                    # Guardar la mejor configuración encontrada
                    if v_vecino > mejor_varianza:
                        mejor_solucion = list(vecino)
                        mejor_varianza = v_vecino

        TEMP_SUP *= alfa # Enfriamiento geométrico

    # Resultados finales
    print("--- Resultado del Proyecto: Mochila 0-1 (FACYT UC) ---")
    print(f"Suma total de pesos (s): ${suma_items}")
    print(f"Capacidad máxima (W - 30% de la suma total de items): ${capacidad_W}")
    print(f"Mejor varianza encontrada (T_sup): {mejor_varianza}")
    print(f"Vector de solución x_i: {mejor_solucion}")

    pesos_sel = [items[i].peso for i in range(tam_datos_items) if mejor_solucion[i] == 1]
    valores_sel = [items[i].valor for i in range(tam_datos_items) if mejor_solucion[i] == 1]

    print(f"\nInversiones seleccionadas (Pesos/Beneficio): {pesos_sel}")
    print(f"Inversiones seleccionadas (Valores/Dolares): {valores_sel}")
    print(f"Total capital invertido: ${sum(pesos_sel)} / ${capacidad_W}")
    print(f"\nNiveles de enfriamiento (a): {a}")
    print(f"Total de iteraciones (b): {b}")

if __name__ == "__main__":
    main()