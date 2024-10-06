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
        



def main():
  file_path = os.path.join('..', 'Data', 'raw', 'DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2006.csv')
  # Cargar el archivo CSV en un DataFrame
  df = pd.read_csv(file_path, low_memory=False, encoding = 'latin-1')
  df['Fecha'] = pd.to_datetime('2006-07-01')
  # Seleccionar las columnas que te interesan
  filtered_df_2006 = df[['edad', 'sexo', 'ent','Fecha', 'd510']]
  # Renombrar columnas específicas
  filtered_df_2006 = filtered_df_2006.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'ent':'Entidad', 'd510':'Atentar_contras_si'})
  
  file_path = os.path.join('..', 'Data', 'raw','DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2012.csv')
  df = pd.read_csv(file_path, encoding = 'latin-1')
  df['Fecha'] = pd.to_datetime('2012-01-07')
  # Seleccionar las columnas que te interesan
  filtered_df_2012 = df[['edad','sexo','entidad','Fecha', 'd701']]
  filtered_df_2012=filtered_df_2012.rename(columns={'entidad': 'Entidad', 'sexo': 'Sexo', 'edad': 'Edad', 'd701': 'Atentar_contras_si'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2018.csv')
  df = pd.read_csv(file_path, sep=';', encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2018 = df[['EDAD','SEXO', 'ENT', 'FECHA_ENTREVISTA','P7_17','P5_1_3','P5_1_7']]
  filtered_df_2018 = filtered_df_2018.rename(columns={'EDAD': 'Edad', 'SEXO': 'Sexo', 'ENT': 'Entidad', 'P7_17': 'Atentar_contras_si', 'P5_1_3': 'Depresion', 'P5_1_7': 'Tristeza', 'FECHA_ENTREVISTA': 'Fecha'})
  filtered_df_2018['Fecha'] = pd.to_datetime('2018-07-01')

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2020.csv')
  df = pd.read_csv(file_path, sep=';', encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2020 = df[['H0303','H0302', 'ENTIDAD','FECHA_INI','AD0217']]
  filtered_df_2020 = filtered_df_2020.rename(columns={'ENTIDAD': 'Entidad', 'FECHA_INI': 'Fecha', 'AD0217': 'Atentar_contras_si', 'H0302':'Sexo', 'H0303':'Edad'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2021.csv')
  df = pd.read_csv(file_path, sep=';', low_memory=False, encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2021 = df[['edad', 'sexo', 'entidad','fecha_ini','d0819', 'd0601c','d0601g']]
  filtered_df_2021 = filtered_df_2021.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2022.csv')
  df = pd.read_csv(file_path, sep=';', encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2022 = df[['edad','sexo','entidad', 'fecha_ini', 'd0819', 'd0601c','d0601g']]
  filtered_df_2022= filtered_df_2022.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADOLESCENTES', 'ENSANUT-Adolescentes-Datos-2023.csv')
  df = pd.read_csv(file_path, sep=';', encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2023 = df[['edad','sexo','entidad', 'fecha_ini', 'd0819','d0601c','d0601g']]
  filtered_df_2023 = filtered_df_2023.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'd0819': 'Atentar_contras_si', 'd0601c': 'Depresion', 'd0601g': 'Tristeza'})

  # Lista de DataFrames
  dataframes = [filtered_df_2006, filtered_df_2012, filtered_df_2018, filtered_df_2020, filtered_df_2021, filtered_df_2022,filtered_df_2023] 

  # Concatenar los DataFrames hacia abajo
  df_concatenado = pd.concat(dataframes, axis=0, ignore_index=True) 
  df_concatenado['Fecha'] = pd.to_datetime(df_concatenado['Fecha'], errors='coerce')

  # ruta donde guardar el CSV
  file_path = os.path.join('..', 'Data', 'interim', 'Adolescentes.csv')

  # Guarda el DataFrame en formato CSV
  df_concatenado.to_csv(file_path, index=False)  # index=False evita que se guarde el índice del DataFrame





  file_path = os.path.join('..', 'Data', 'raw', 'DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2006.csv')
  df = pd.read_csv(file_path, low_memory=False, encoding = 'latin-1')
  df['Fecha'] = pd.to_datetime('2006-07-01')
  # Seleccionar las columnas que te interesan
  filtered_df_2006 = df[['edad', 'sexo', 'ent','Fecha', 'a301a']]
  # Renombrar columnas específicas
  filtered_df_2006 = filtered_df_2006.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'ent':'Entidad', 'a301a':'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2012.csv')
  df = pd.read_csv(file_path, encoding = 'latin-1')
  df['Fecha'] = pd.to_datetime('2012-01-07')
  # Seleccionar las columnas que te interesan
  filtered_df_2012 = df[['edad','sexo','entidad','Fecha', 'a201_c', 'a201_g']]
  filtered_df_2012=filtered_df_2012.rename(columns={'entidad': 'Entidad', 'sexo': 'Sexo', 'edad': 'Edad', 'a201_c': 'Depresion', 'a201_g': 'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2018.csv')
  df = pd.read_csv(file_path, sep=';', low_memory=False, encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  df['Fecha'] = pd.to_datetime('2018-07-01')
  filtered_df_2018 = df[['EDAD','SEXO', 'ENT','Fecha','P12_8','P2_1_3','P2_1_7']]
  filtered_df_2018 = filtered_df_2018.rename(columns={'EDAD': 'Edad', 'SEXO': 'Sexo', 'ENT': 'Entidad', 'P12_8': 'Atentar_contras_si', 'P2_1_3': 'Depresion', 'P2_1_7': 'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2020.csv')
  df = pd.read_csv(file_path, sep=';', low_memory=False, encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2020 = df[['H0303','H0302', 'ENTIDAD','FECHA_INI','ADUL209']]
  filtered_df_2020 = filtered_df_2020.rename(columns={'ENTIDAD': 'Entidad', 'FECHA_INI': 'Fecha', 'ADUL209': 'Atentar_contras_si', 'H0302':'Sexo', 'H0303':'Edad'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2021.csv')
  df = pd.read_csv(file_path, sep=';', low_memory=False, encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2021 = df[['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217']]
  filtered_df_2021 = filtered_df_2021.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2022.csv')
  df = pd.read_csv(file_path, sep=';', low_memory=False, encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2022 = df[['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217']]
  filtered_df_2022 = filtered_df_2021.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'})

  file_path = os.path.join('..', 'Data', 'raw','DATOS ADULTOS', 'ENSANUT-Adultos-Datos-2023.csv')
  df = pd.read_csv(file_path, sep=';', encoding = 'latin-1')
  # Seleccionar las columnas que te interesan
  filtered_df_2023 = df[['edad', 'sexo', 'entidad','fecha_ini','a1213', 'a0213','a0217']]
  filtered_df_2023 = filtered_df_2021.rename(columns={'edad': 'Edad', 'sexo': 'Sexo', 'entidad': 'Entidad', 'fecha_ini': 'Fecha', 'a1213': 'Atentar_contras_si', 'a0213': 'Depresion', 'a0217': 'Tristeza'})

  # Lista de DataFrames
  dataframes = [filtered_df_2006, filtered_df_2012, filtered_df_2018, filtered_df_2020, filtered_df_2021, filtered_df_2022,filtered_df_2023]  # Reemplaza con los nombres de tus DataFrames

  # Concatenar los DataFrames hacia abajo
  df_concatenado = pd.concat(dataframes, axis=0, ignore_index=True)
  df_concatenado['Fecha'] = pd.to_datetime(df_concatenado['Fecha'], errors='coerce')
  # ruta donde guardar el CSV
  file_path = os.path.join('..', 'Data', 'interim', 'Adultos.csv')

  # Guarda el DataFrame en formato CSV
  df_concatenado.to_csv(file_path, index=False)  # index=False evita que se guarde el índice del DataFrame




  file_path_adol = os.path.join('..', 'Data', 'interim', 'Adolescentes.csv')
  file_path_adul = os.path.join('..', 'Data', 'interim', 'Adultos.csv')
  df_adol = pd.read_csv(file_path_adol, low_memory=False)
  df_adul = pd.read_csv(file_path_adul, low_memory=False)

  dataframes = [df_adol,df_adul] 

  # Concatenar los DataFrames hacia abajo
  df_concatenado = pd.concat(dataframes, axis=0, ignore_index=True)

  # ruta donde guardar el CSV
  file_path = os.path.join('..', 'Data', 'interim', 'Datos-Adol-Adul.csv')

  # Guarda el DataFrame en formato CSV
  df_concatenado.to_csv(file_path, index=False)

  # Abrir el el archivo .shp
  mapa_a = os.path.join('..', 'Data', 'raw', 'MAPA', '2023_1_00_ENT.shp')
  datos_mapa = gpd.read_file(mapa_a, encoding = 'latin-1')

  datos_ensa = gpd.read_file(file_path, encoding = 'latin-1')

  datos_ensa['Entidad'] = datos_ensa['Entidad'].astype(int)
  datos_mapa['CVE_ENT'] = datos_mapa['CVE_ENT'].astype(int)

  # Fusionar los DataFrames en la columna 'Entidad' (CSV) y 'CVE_ENT' (SHP)
  df_combinado = pd.merge(datos_ensa, datos_mapa, left_on='Entidad', right_on='CVE_ENT', how='left')

  df_combinado = gpd.GeoDataFrame(df_combinado, geometry='geometry')

  df_combinado = df_combinado.drop(columns=['CVE_ENT','CVEGEO', 'geometry'])
  df_combinado  = df_combinado.rename(columns={'NOMGEO': 'Entidad', 'Entidad':'C_Entidad'})

  df_combinado = df_combinado[['Edad',	'Sexo',	'C_Entidad', 'Entidad',	'Fecha',	'Atentar_contras_si',	'Depresion',	'Tristeza']]

  # Reemplazar los valores vacíos o nulos con NaN en df_combinado
  df_combinado = df_combinado.replace(['', ' ', '9'], np.nan)  # Convertir celdas vacías y espacios en NaN
  df_combinado = df_combinado.fillna(0)  # Reemplazar NaN con 0


  # Convertir la columna 'Edad' a tipo entero
  df_combinado['Edad'] = df_combinado['Edad'].astype(int)

  # Convertir la columna 'Sexo' a tipo categórico
  df_combinado['Sexo'] = df_combinado['Sexo'].astype('category')

  # Convertir la columna 'Entidad' a tipo categórico
  df_combinado['Entidad'] = df_combinado['Entidad'].astype('category')

  # Convertir la columna 'Fecha' a tipo datetime
  df_combinado['Fecha'] = pd.to_datetime(df_combinado['Fecha'], errors='coerce')

  # Convertir las columnas 'Atentar_contras_si', 'Depresion' y 'Tristeza' a tipo categórico
  df_combinado['Atentar_contras_si'] = df_combinado['Atentar_contras_si'].astype('category')
  df_combinado['Depresion'] = df_combinado['Depresion'].astype('category')
  df_combinado['Tristeza'] = df_combinado['Tristeza'].astype('category')
  df_combinado['C_Entidad'] = df_combinado['C_Entidad'].astype('category')

  file_path = os.path.join('..', 'Data', 'processed', 'Ensanut-data-p.csv')
  df_combinado.to_csv(file_path, index=False, encoding='utf-8-sig')
  crear_archivo_texto('datos_ENSANUT_info.txt')

if __name__ == "__main__":
    main()
