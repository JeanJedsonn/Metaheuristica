import random
import math

def generar_vecino(actual, n):
    vecino = list(actual)
    indice_cambio = random.randint(0, n - 1)
    # Cambio de estado del artículo (0 o 1)
    vecino[indice_cambio] = 1 - vecino[indice_cambio] 
    
    return vecino

def calcular_varianza(solucion, items, W):
    diferencias = []
    peso_total = 0

    # 1. Identificar artículos seleccionados y calcular diferencias
    for i in range(len(solucion)):
        if solucion[i] == 1:
            peso_total += items[i].peso
            # Arreglo de la diferencia entre el peso y valor
            diferencias.append(items[i].peso - items[i].valor)

    # 2. Restricción: No superar la capacidad máxima W
    if peso_total > W or not diferencias:
        return -1.0  # Penalización por solución inválida

    # 3. Cálculo de la varianza manual
    n_sel = len(diferencias)
    
    # Calcular la media (promedio)
    suma = sum(diferencias)
    media = suma / n_sel
    
    # Calcular la suma de los cuadrados de las distancias a la media
    varianza_sum = 0
    for d in diferencias:
        varianza_sum += (d - media) ** 2
        
    # Retornar el promedio de los cuadrados
    return varianza_sum / n_sel

def definir_Temp_sup(tam_datos_items, items, capacidad_W):
    muestras = 500                      # ejecutar n veces
    deltas_muestreo = []                # lista de deltas
    sol_temp = [0] * tam_datos_items    # solucion temporal

    # bucle para muestrear
    for _ in range(muestras):
        vecino_temporal = generar_vecino(sol_temp, tam_datos_items)
        varianza_original = calcular_varianza(sol_temp, items, capacidad_W)
        varianza_vecino  = calcular_varianza(vecino_temporal, items, capacidad_W)
        
        if varianza_vecino != -1.0:
            deltas_muestreo.append(abs(varianza_vecino - varianza_original))
            sol_temp = vecino_temporal

    if deltas_muestreo:
        delta_promedio = sum(deltas_muestreo) / len(deltas_muestreo)
        T_sup_temp = -delta_promedio / math.log(0.8) # Probabilidad de 0.8 inicial
    else:
        T_sup_temp = 1000.0 # Valor de respaldo
    
    return T_sup_temp