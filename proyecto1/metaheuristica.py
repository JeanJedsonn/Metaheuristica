import random
import math

class Articulo:
    def __init__(self, peso, valor):
        self.peso = peso   # wi: Cantidad de dólares requerida
        self.valor = valor # vi: Beneficio esperado
        
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


def main():
    # Definición de los artículos (peso, valor)
    datos_items = [
        (12, 150), (30, 200), (45, 180), (10, 90), (25, 170),
        (50, 400), (18, 120), (8, 70), (60, 450), (22, 190),
        (35, 210), (15, 130), (40, 300), (12, 85), (28, 220),
        (5, 40), (55, 500), (20, 160), (32, 240), (48, 380),
        (14, 110), (26, 195), (38, 280), (9, 75), (42, 310),
        (17, 140), (29, 230), (3, 25), (52, 420), (21, 155)
    ]
    tam_datos_items = len(datos_items)
    
    # Cálculo de la capacidad máxima W (30% del total de pesos)
    suma_items = sum(p for p, v in datos_items) # Suma total de pesos de los artículos
    capacidad_W = math.ceil(suma_items * 0.3) # Capital total W
    
    items = [Articulo(p, v) for p, v in datos_items]
    
    # Fase de muestreo para determinar T_sup
    muestras = 500
    deltas_muestreo = []
    sol_temp = [0] * tam_datos_items

    for _ in range(muestras):
        vecino_temp = generar_vecino(sol_temp, tam_datos_items)
        v_orig = calcular_varianza(sol_temp, items, capacidad_W)
        v_vec  = calcular_varianza(vecino_temp, items, capacidad_W)
        
        if v_vec != -1.0:
            deltas_muestreo.append(abs(v_vec - v_orig))
            sol_temp = vecino_temp

    if deltas_muestreo:
        delta_promedio = sum(deltas_muestreo) / len(deltas_muestreo)
        T_sup_temp = -delta_promedio / math.log(0.8) # Probabilidad de 0.8 inicial
    else:
        T_sup_temp = 1000.0 # Valor de respaldo
    

    # Parámetros del Simulated Annealing
    T_sup = T_sup_temp         # Temperatura inicial basada en el muestreo
    T_inf = 0.001              # Temperatura final
    alfa = 0.95                # Factor de enfriamiento
    L = tam_datos_items * 10   # Iteraciones por temperatura

    # Inicialización de la solución
    actual = [0] * tam_datos_items                                 # Mochila inicialmente vacía
    mejor_solucion = list(actual)                                  # Mejor solución encontrada
    mejor_varianza = calcular_varianza(actual, items, capacidad_W) # Varianza de la solución inicial
    
    T = T_sup   # Temperatura actual
    a, b = 0, 0 # Contadores de ciclos y pasos

    # Ciclo principal del Simulated Annealing
    while T > T_inf:
        a += 1
        for _ in range(L):
            b += 1
            
            vecino = generar_vecino(actual, tam_datos_items)
            
            v_actual = calcular_varianza(actual, items, capacidad_W)
            v_vecino = calcular_varianza(vecino, items, capacidad_W)

            # Si el vecino cumple con la restricción de peso
            if v_vecino != -1.0:
                delta = v_vecino - v_actual

                # Criterio de Aceptación de Metropolis
                probabilidad = math.exp(delta / T) if T > 0 else 0
                if (delta > 0 or random.random() < probabilidad):
                    actual = vecino
                    
                    # Guardar la mejor configuración encontrada
                    if v_vecino > mejor_varianza:
                        mejor_solucion = list(vecino)
                        mejor_varianza = v_vecino

        T *= alfa # Enfriamiento geométrico

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