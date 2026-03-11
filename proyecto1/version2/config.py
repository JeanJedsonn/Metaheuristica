import os

TEMP_INF = 0.001
ALFA = 0.95
CAPACIDAD_MAXIMA_MOCHILA = 1471

def cargar_datos_desde_archivo(ruta_archivo="datos.txt"):
    """
    Lee un archivo de texto con dos listas de la forma (a1, a2, ..., an) y (b1, b2, ..., bn)
    y retorna una lista de tuplas (a_i, b_i).
    """
    
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError("No se encontró el archivo datos.txt")

    try:
        with open(ruta_archivo, 'r') as f:
            contenido = f.read()
            
        # Separamos por el delimitador ';'
        partes = contenido.split(';')
        
        if len(partes) >= 2:
            # Limpiamos los caracteres de lista o tupla y posibles saltos de linea
            str_pesos = partes[0].replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('\n', ' ')
            str_valores = partes[1].replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('\n', ' ')
            
            # Separamos por comas (o espacios si no hay comas)
            separador_pesos = ',' if ',' in str_pesos else None
            separador_valores = ',' if ',' in str_valores else None
            
            # Covertimos a sublistas evaluando cada elemento
            pesos = [int(float(x.strip())) for x in str_pesos.split(separador_pesos) if x.strip()]
            valores = [int(float(x.strip())) for x in str_valores.split(separador_valores) if x.strip()]
            
            if len(pesos) != len(valores):
                raise ValueError("Las dos listas en datos.txt no tienen el mismo tamaño")
                
            # Formamos las tuplas (peso, valor)
            return list(zip(pesos, valores))
            
    except Exception as e:
        raise ValueError(f"Error al leer datos.txt: {e}")

DATOS_ITEMS = cargar_datos_desde_archivo("datos.txt")