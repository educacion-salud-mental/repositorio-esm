import os
import pandas as pd
import re

os.chdir("../Data/raw/DATOS EDUCACION")


# Censos de Población y Vivienda
CENSOS_DE_POBLACION_Y_VIVIENDA_PATH="./CENSOS DE POBLACION Y VIVIENDA"# Ruta en donde se encuentran los datos de Censos
work_directory=CENSOS_DE_POBLACION_Y_VIVIENDA_PATH

"""
Se cargan los datos a un dataframe por archivo, y se guardan en una lista.

"""
dataframes=[]
diccionarios_de_datos=[]
for item in os.listdir(work_directory):
    item_path=f"{work_directory}/{item}"
    # En caso de tratarse de un archivo resultado de una extracción zip:
    if os.path.isdir(item_path):
        file_name=os.listdir(f"{item_path}/conjunto_de_datos")[0]
        file_path=f"{item_path}/conjunto_de_datos/{file_name}"
        df=pd.read_csv(file_path)
    # Se busca un archivo diccionario de datos y se guarda el dataframe de este en la lista de diccionarios
        pattern = r"^diccionario.*datos$"
        for subitem in os.listdir(item_path):
            match = re.search(pattern,subitem)
            if match:
                dictionary_name=match.group()

        data_dictionary_path=f"{item_path}/{dictionary_name}/{os.listdir(f"{item_path}/{dictionary_name}")[0]}"
        dictionary_df=pd.read_csv(data_dictionary_path,encoding='ISO-8859-1')
        diccionarios_de_datos.append(dictionary_df)
    # En este caso particular, el resto de los archivos son de tipo excel
    else:
        file_path=item_path
        df=pd.read_excel(file_path,sheet_name=1,skiprows=4)
    
    dataframes.append(df)
    print(f"Datos del archivo {item} se cargaron a la lista 'dataframes' ")

## Filtro columnas

def filtro_columnas(df,dictionary_dataframe,columns):
    """
    df: Dataframe de los datos que se quieren utilizar
    diciontary_dataframe: Dataframe de diccionario de datos asociado con el dataframe en uso
    columns:Lista de columnas que se mantendran en el dataframe

    Esta función primero traduce los mnemónicos del dataframe en uso a sus nombres completos utilizando
    el dataframe del diccionario de datos. Luego, se filtran las clolumnas que se quieren usar en el d-
    ataframe original.

    """
    rename_dictionary={}
    for index,row in dictionary_dataframe.iterrows():
        old_column_name=row['mnemonico']
        new_column_name=row['indicador']
        rename_dictionary[old_column_name] = new_column_name

    df=df.rename(columns=rename_dictionary)
    df=df[columns]
    return df

## Revision de nulos:

def revision_nulos(df):
    """
    df:Dataframe que se quiere analizar

    Esta función recibe el dataframe que se quiere analizar para imprimir el porcentaje de registros nulos
    por cada columna del dataframe.
    """
    total_rows=len(df)
    for column in df.columns:
        nans=0
        nans=df[column].isna().sum()
        if nans!=0:
            print(f"{round(100*nans/total_rows,4)}% de los registros en {column} son nulos")
    
## Calidad de datos 

def formato_columnas(df,format_columns):
    """
    df:Dataframe que se quiere analizar
    format_columns: Diccionario en donde las llaves siguen la estructura '<tipo_dato>_columns' y los valores
    son listas de los nombres de las columnas que se quieren guardar bajo el tipo de dato de la llave.


    Esta función primero genera un diccionario donde las llaves son el nombre de la columna dentro
    del dataframe, y los valores son el tipo de dato en la que se quieren guardar. Luego, intenta 
    actualizar el tipo de dato que sigue cada columna. Si se encuentra con un error ValueError, 
    guarda la columna y el valor que causó el error en una lista llamada error_columns. Esta lista 
    es lo que entrega al final
    """
    formats={}
    for string_column in format_columns['string_columns']:
        formats[string_column]='str'

    for float_column in format_columns['float_columns']:
        formats[float_column]='float'

    for integer_column in format_columns['integer_columns']:
       formats[integer_column]='int'

    error_columns=[]
    for column,format_type in formats.items():
        try:
            df[column] = df[column].astype(format_type)
            #print(f"Columna {column} formateada a {format_type}")
        except ValueError as e:
            pattern = r"'(.*?)'"
            match = re.search( pattern, str(e) )
            error_value=match.group(1)
            error_columns.append([column,error_value])  # Store the column name
            #print(f"Error al formatear la columna '{column}' a '{format_type}': {e}")

    #if len(error_columns)!=0:
    #    for error_column in error_columns:
    #            percentage=100*round(len(df[df[error_column[0]]==error_column[1]])/len(df),2)
    #            print(f"{percentage}% de los registros en {error_column[0]} son {error_column[1]} ")
                #df=df[~(df[error_column[0]]==error_column[1])]
                #print(f"Se omitieron los registros erroneos en {error_column[0]} exitosamente!")
    return error_columns
        


os.chdir("..")
os.chdir("..")
os.chdir("..")
os.chdir("./notebooks")
