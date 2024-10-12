from dateutil import parser
from datetime import datetime
import os
import requests
import zipfile
import pandas as pd
import numpy as np
import geopandas as gpd

def crear_archivo_texto(nombre_archivo):
    """
    Crea un archivo de texto con la fecha actual y un mensaje de descripción.
    
    Args:
        nombre_archivo (str): Nombre del archivo de texto a crear.
    """
    fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M")

    ruta_guardado = os.path.join('..', 'Data', 'processed', nombre_archivo)

    os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)

    with open(ruta_guardado, 'w') as archivo:
        archivo.write("Datos de Ensanut procesados:\n")
        archivo.write(f"Fecha de ejecución: {fecha_hoy}\n")
        archivo.write("\n")
        archivo.write("Los datos de ENSANUT en el apartado de salud ahora están concatenados.\n")
        archivo.write("Apartir de los raw data, se tomaron las columnas con la edad, sexo, entidad, fecha de entrevista, preguntas relacionadas a su salud mental,\n")
        archivo.write("las preguntas seleccionadas fueron '¿Alguna vez a propósito se ha herido, cortado,  intoxicado o hecho daño con el fin de quitarse la vida?',\n")
        archivo.write("'Durante la última semana...¿se sintió deprimido(a)?' y 'Durante la última semana...¿se sintió triste?'.\n")
        archivo.write("Posteriormente los dataframes abtenidos se concatenaron, agregaron una nueva columna con el nombre de la entidad federativa y se les hicieron\n")
        archivo.write("las pruebas de calidad de datos básicas, por ejemplo formatear el tipo de dato, unificar los resultados de los cuestionarios, sustituir\n")
        archivo.write("datos perdidos.\n")
        archivo.write("\n")
        archivo.write("También, se incluye un catálogo de estos nuevos datos, el cual está ubicado en la carpeta references.")


def cargar_datos(file_path, i, m, encoding='latin-1', low_memory=True):
    '''Función para cargar datos con el separador adecuado.
    
    Args:
        file_path (str): Direccion del archivo.
        i (int): Iterador sobre una lista.
        m (list): Lista con el separador adecuado.
        encoding (str): Tipo de codificado.
        low_memory (Bool): Caracteristica del archivo.
    '''
    if i in m:
        return pd.read_csv(file_path, encoding=encoding, low_memory=low_memory)
    return pd.read_csv(file_path, sep=';', encoding=encoding, low_memory=low_memory)

def agregar_fecha(df, fecha):
    '''Función para agregar una columna de fecha fija a un DataFrame
    
    Args:
        df (DataFrame): Nombre del dataframe.
        fecha (str): Fecha del archivo.
    '''
    try:
        df['Fecha'] = pd.to_datetime(fecha, dayfirst=True, errors='coerce')
    except Exception as e:
        print(f"Error al agregar la fecha: {e}")
    return df


def filtrar_columnas(df, columnas_interes):
    '''Función para filtrar columnas de interés que están presentes en el DataFrame
    
    Args:
        df (DataFrame): Nombre del dataframe.
        columnas_interes (list): Lista de las columnas que queremos aislar.
    '''
    columnas_existentes = [col for col in columnas_interes if col in df.columns]
    return df[columnas_existentes]

def renombrar_columnas(df, nuevos_nombres):
    '''Función para renombrar columnas en el DataFrame
    
    Args:
        df (DataFrame): Nombre del dataframe.
        nuevos_nombres (dict): Diccionario, key columnas que queremos renmbrar - values nuevo nombre de la columna.
    '''
    return df.rename(columns=nuevos_nombres)

def concatenar_y_guardar(dataframes, file_path):
    '''Función para concatenar y guardar DataFrames

    Args:
        dataframes (list): Dataframes a concatenar.
        file_path (Path): Direccion para guardar el archivo.'''
    
    # Concatenar los DataFrames
    df_concat = pd.concat(dataframes, axis=0, ignore_index=True)
    
    # Aplicar limpieza de fechas
    df_concat['Fecha'] = df_concat['Fecha'].apply(lambda x: pd.to_datetime(x, dayfirst=True, errors='coerce'))

    # Guardar el DataFrame en archivo CSV
    df_concat.to_csv(file_path, index=False)


def procesar_y_guardar(rutas_archivos, fechas, columnas_interes, renombrar_columnas_map, archivo_salida, l , m):
    '''Función para procesar y concatenar archivos
    Args:
        rutas_archivos (list): Lista de los paths.
        fechas (list): Lista de las fechas que se cambian.
        columnas_interes (list): Lista de las columnas de interes.
        renombrar_columnas_map (dict): Diccionario, key columnas que queremos renmbrar - values nuevo nombre de la columna.
        archivo_salida (Path): Donde guardar el producto.
        l (list): Lista para el low_memory
        m (list): Lista para sep ;
    '''
    dataframes = []
    
    for i, ruta in enumerate(rutas_archivos):
        file_path = os.path.join(*ruta)
        low_memory = i not in l  # Ajustar low_memory según sea necesario
        df = cargar_datos(file_path, i, m, low_memory=low_memory)
        
        if fechas[i]:  # Si hay una fecha definida, agregarla
            df = agregar_fecha(df, fechas[i])
        df = filtrar_columnas(df, columnas_interes[i])
        df = renombrar_columnas(df, renombrar_columnas_map[i])
        dataframes.append(df)
    
    concatenar_y_guardar(dataframes, archivo_salida)



def cargar_y_concatenar_datos(file_path_adol, file_path_adul, output_file):
    '''Función para cargar los datos de Adolescentes y Adultos y concatenarlos
    
     Args:
        file_path_adol (Path: Path del archivo Adol.
        file_path_adul (Path): Path del archivo Adul.
        output_file (Path): Path del archivo que se guarda concatenado.
    '''
    # Cargar los archivos CSV
    df_adol = pd.read_csv(file_path_adol, low_memory=False)
    df_adul = pd.read_csv(file_path_adul, low_memory=False)

    # Concatenar los DataFrames hacia abajo
    df_concatenado = pd.concat([df_adol, df_adul], axis=0, ignore_index=True)

    # Guardar el DataFrame concatenado
    df_concatenado.to_csv(output_file, index=False)
    return output_file




def limpiar_y_transformar(df_combinado):
    '''Función para limpiar y transformar el DataFrame combinado
    
    Args:
        df_combinado (DataFrame): Dataframe que se va a limpiar.
    '''
    # Reemplazar valores vacíos o nulos
    df_combinado = df_combinado.replace(['', ' ', '9'], np.nan)
    df_combinado = df_combinado.fillna(0)
    
    # Convertir tipos de datos
    df_combinado['Edad'] = df_combinado['Edad'].astype(int)
    df_combinado['Sexo'] = df_combinado['Sexo'].astype('category')
    df_combinado['Entidad'] = df_combinado['Entidad'].astype('category')
    
    # Unificar formato de fecha utilizando una detección automática con parser
    def parse_fecha(fecha):
        try:
            return parser.parse(fecha, dayfirst=True)
        except (ValueError, TypeError):
            return np.nan

    df_combinado['Fecha'] = df_combinado['Fecha'].apply(parse_fecha)
    
    # Convertir otros tipos de datos
    df_combinado['Atentar_contras_si'] = df_combinado['Atentar_contras_si'].astype('category')
    df_combinado['Depresion'] = df_combinado['Depresion'].astype('category')
    df_combinado['Tristeza'] = df_combinado['Tristeza'].astype('category')
    df_combinado['C_Entidad'] = df_combinado['C_Entidad'].astype('category')

    return df_combinado



def procesar_datos_ensanut():
    '''Función principal que ejecuta el flujo completo del proceso'''
    # Rutas de archivos
    file_path_adol = os.path.join('..', 'Data', 'interim', 'Adolescentes.csv')
    file_path_adul = os.path.join('..', 'Data', 'interim', 'Adultos.csv')
    output_file_concatenado = os.path.join('..', 'Data', 'interim', 'Datos-Adol-Adul.csv')

    # Cargar, concatenar y guardar datos de adolescentes y adultos
    concatenado_path = cargar_y_concatenar_datos(file_path_adol, file_path_adul, output_file_concatenado)

    # Ruta del archivo shapefile
    mapa_a = os.path.join('..', 'Data', 'raw', 'MAPA', '2023_1_00_ENT.shp')

    # Fusionar datos ENSA con el mapa
    df_combinado = fusionar_con_mapa(concatenado_path, mapa_a)

    # Limpiar y transformar los datos
    df_combinado = limpiar_y_transformar(df_combinado)

    # Guardar el DataFrame procesado
    output_file = os.path.join('..', 'Data', 'processed', 'Ensanut-data-p.csv')
    df_combinado.to_csv(output_file, index=False, encoding='utf-8-sig')

    # Crear archivo de información
    crear_archivo_texto('datos_ENSANUT_info.txt')



def main():
    rutas_archivos_1 = [
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2006.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2012.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2018.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2020.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2021.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2022.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2023.csv')
    ]
    rutas_archivos_2 = [
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2006.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2012.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2018.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2020.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2021.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2022.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2023.csv')
    ]


    fechas_1 = ['31-07-2006', '31-07-2012', '31-07-2018', None, None, None, None]
    fechas_2 = ['31-07-2006', '31-07-2012', '31-07-2018', None, None, None, None]




    columnas_interes_1 = [
        ['edad', 'sexo', 'ent', 'Fecha', 'd510'],
        ['edad', 'sexo', 'entidad', 'Fecha', 'd701'],
        ['EDAD', 'SEXO', 'ENT', 'Fecha', 'P7_17', 'P5_1_3', 'P5_1_7'],
        ['H0303', 'H0302', 'ENTIDAD', 'FECHA_INI', 'AD0217'],
        ['edad', 'sexo', 'entidad', 'fecha_ini', 'd0819', 'd0601c', 'd0601g'],
        ['edad', 'sexo', 'entidad', 'fecha_ini', 'd0819', 'd0601c', 'd0601g'],
        ['edad', 'sexo', 'entidad', 'fecha_ini', 'd0819', 'd0601c', 'd0601g']
    ]

    renombrar_columnas_map_1 = [
        {'edad': 'Edad', 'sexo': 'Sexo', 'ent': 'Entidad', 'd510': 'Atentar_contras_si'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'd701': 'Atentar_contras_si'},
        {'EDAD': 'Edad', 'SEXO': 'Sexo', 'ENT': 'Entidad', 'P7_17': 'Atentar_contras_si', 'P5_1_3': 'Depresion', 'P5_1_7': 'Tristeza'},
        {'H0303': 'Edad', 'H0302': 'Sexo', 'ENTIDAD': 'Entidad', 'FECHA_INI': 'Fecha', 'AD0217': 'Atentar_contras_si'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'}
    ]
    columnas_interes_2 = [
        ['edad', 'sexo', 'ent','Fecha', 'a301a'],
        ['edad', 'sexo', 'entidad', 'Fecha', 'd701'],
        ['EDAD','SEXO', 'ENT','Fecha','P12_8','P2_1_3','P2_1_7'],
        ['H0303','H0302', 'ENTIDAD','FECHA_INI','ADUL209'],
        ['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217'],
        ['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217'],
        ['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217']
    ]

    renombrar_columnas_map_2 = [
        {'edad': 'Edad', 'sexo': 'Sexo', 'ent':'Entidad', 'a301a':'Tristeza'},
        {'entidad': 'Entidad', 'sexo': 'Sexo', 'edad': 'Edad', 'a201_c': 'Depresion', 'a201_g': 'Tristeza'},
        {'EDAD': 'Edad', 'SEXO': 'Sexo', 'ENT': 'Entidad', 'P12_8': 'Atentar_contras_si', 'P2_1_3': 'Depresion', 'P2_1_7': 'Tristeza'},
        {'ENTIDAD': 'Entidad', 'FECHA_INI': 'Fecha', 'ADUL209': 'Atentar_contras_si', 'H0302':'Sexo', 'H0303':'Edad'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'}
    ]
    l_1 = [0,4]
    l_2 = [0,2,3,4,5]
    l_3 = [0,1]
    
    # Procesar y guardar datos de adolescentes
    procesar_y_guardar(rutas_archivos_1, fechas_1, columnas_interes_1, renombrar_columnas_map_1, 
                       os.path.join('..', 'Data', 'interim', 'Adolescentes.csv'),l_1, l_3)
    
    # Procesar y guardar datos de adultos
    procesar_y_guardar(rutas_archivos_2, fechas_2, columnas_interes_2, renombrar_columnas_map_2, 
                       os.path.join('..', 'Data', 'interim', 'Adultos.csv'),l_2, l_3)
    
    # Ejecutar el procesamiento de datos
    procesar_datos_ensanut()
    print('Datos procesados')

def main_():
    rutas_archivos_1 = [
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2006.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2012.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2018.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2020.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2021.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2022.csv'),
        ('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2023.csv')
    ]
    rutas_archivos_2 = [
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2006.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2012.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2018.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2020.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2021.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2022.csv'),
        ('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2023.csv')
    ]


    fechas_1 = ['31-07-2006', '31-07-2012', '31-07-2018', None, None, None, None]
    fechas_2 = ['31-07-2006', '31-07-2012', '31-07-2018', None, None, None, None]




    columnas_interes_1 = [
        ['edad', 'sexo', 'ent', 'Fecha', 'd510'],
        ['edad', 'sexo', 'entidad', 'Fecha', 'd701'],
        ['EDAD', 'SEXO', 'ENT', 'Fecha', 'P7_17', 'P5_1_3', 'P5_1_7'],
        ['H0303', 'H0302', 'ENTIDAD', 'FECHA_INI', 'AD0217'],
        ['edad', 'sexo', 'entidad', 'fecha_ini', 'd0819', 'd0601c', 'd0601g'],
        ['edad', 'sexo', 'entidad', 'fecha_ini', 'd0819', 'd0601c', 'd0601g'],
        ['edad', 'sexo', 'entidad', 'fecha_ini', 'd0819', 'd0601c', 'd0601g']
    ]

    renombrar_columnas_map_1 = [
        {'edad': 'Edad', 'sexo': 'Sexo', 'ent': 'Entidad', 'd510': 'Atentar_contras_si'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'd701': 'Atentar_contras_si'},
        {'EDAD': 'Edad', 'SEXO': 'Sexo', 'ENT': 'Entidad', 'P7_17': 'Atentar_contras_si', 'P5_1_3': 'Depresion', 'P5_1_7': 'Tristeza'},
        {'H0303': 'Edad', 'H0302': 'Sexo', 'ENTIDAD': 'Entidad', 'FECHA_INI': 'Fecha', 'AD0217': 'Atentar_contras_si'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'}
    ]
    columnas_interes_2 = [
        ['edad', 'sexo', 'ent','Fecha', 'a301a'],
        ['edad', 'sexo', 'entidad', 'Fecha', 'd701'],
        ['EDAD','SEXO', 'ENT','Fecha','P12_8','P2_1_3','P2_1_7'],
        ['H0303','H0302', 'ENTIDAD','FECHA_INI','ADUL209'],
        ['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217'],
        ['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217'],
        ['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217']
    ]

    renombrar_columnas_map_2 = [
        {'edad': 'Edad', 'sexo': 'Sexo', 'ent':'Entidad', 'a301a':'Tristeza'},
        {'entidad': 'Entidad', 'sexo': 'Sexo', 'edad': 'Edad', 'a201_c': 'Depresion', 'a201_g': 'Tristeza'},
        {'EDAD': 'Edad', 'SEXO': 'Sexo', 'ENT': 'Entidad', 'P12_8': 'Atentar_contras_si', 'P2_1_3': 'Depresion', 'P2_1_7': 'Tristeza'},
        {'ENTIDAD': 'Entidad', 'FECHA_INI': 'Fecha', 'ADUL209': 'Atentar_contras_si', 'H0302':'Sexo', 'H0303':'Edad'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'},
        {'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'}
    ]
    l_1 = [0,4]
    l_2 = [0,2,3,4,5]
    l_3 = [0,1]
    
    # Procesar y guardar datos de adolescentes
    procesar_y_guardar(rutas_archivos_1, fechas_1, columnas_interes_1, renombrar_columnas_map_1, 
                       os.path.join('..', 'Data', 'interim', 'Adolescentes.csv'),l_1, l_3)
    
    # Procesar y guardar datos de adultos
    procesar_y_guardar(rutas_archivos_2, fechas_2, columnas_interes_2, renombrar_columnas_map_2, 
                       os.path.join('..', 'Data', 'interim', 'Adultos.csv'),l_2, l_3)
    
    # Ejecutar el procesamiento de datos
    procesar_datos_ensanut()
    print('Datos procesados')

if __name__ == "__main__":
    main()
