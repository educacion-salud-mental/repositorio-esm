import os
import pandas as pd
import re
os.chdir("../Data/raw/DATOS EDUCACION")

COLUMNS=[
       'Entidad Federativa',
       'Clave del Municipio',
       'Municipio',
       'Clave de Localidad',
       'Localidad', 'Longitud', 'Latitud', 'Altitud', 
       'Población total','Población masculina', 'Población femenina',
       # Columnas relacionadas con la educacion
       'Población de 8 a 14 años que no sabe leer y escribir',
       'Población masculina de 8 a 14 años que no sabe leer y escribir',
       'Población femenina de 8 a 14 años que no sabe leer y escribir',
       'Población de 15 años y más analfabeta',
       'Población masculina de 15 años y más analfabeta',
       'Población femenina de 15 años y más analfabeta',
       'Población de 5 años que no asiste a la escuela',
       'Población masculina de 5 años que no asiste a la escuela',
       'Población femenina de 5 años que no asiste a la escuela',
       'Población de 6 a 11 años que no asiste a la escuela',
       'Población de 6 a 14 años que no asiste a la escuela',
       'Población masculina de 6 a 14 años que no asiste a la escuela',
       'Población femenina de 6 a 14 años que no asiste a la escuela',
       'Población de 12 a 14 años que no asiste a la escuela',
       'Población de 15 a 24 años que asiste a la escuela',
       'Población masculina de 15 a 24 años que asiste a la escuela',
       'Población femenina de 15 a 24 años que asiste a la escuela',
       'Población de 15 años y más sin escolaridad',
       'Población masculina de 15 años y más sin escolaridad',
       'Población femenina de 15 años y más sin escolaridad',
       'Población de 15 años y más con educación básica incompleta',
       'Población masculina de 15 años y más con educación básica incompleta',
       'Población femenina de 15 años y más con educación básica incompleta',
       'Población de 15 años y más con educación básica completa',
       'Población masculina de 15 años y más con educación básica completa',
       'Población femenina de 15 años y más con educación básica completa',
       'Población de 15 años y más con educación posbásica',
       'Población masculina de 15 años y más con educación posbásica',
       'Población femenina de 15 años y más con educación posbásica',
       'Grado promedio de escolaridad',
       'Grado promedio de escolaridad de la población masculina',
       'Grado promedio de escolaridad de la población femenina',
         ]

## Formatos de las columnas
STRING_COLUMNS=[
       'Entidad Federativa',
       'Clave del Municipio',
       'Municipio',
       'Clave de Localidad',
       'Localidad',
]
FLOAT_COLUMNS=[
    'Longitud', 'Latitud', 'Altitud',
    'Grado promedio de escolaridad',
    'Grado promedio de escolaridad de la población masculina',
    'Grado promedio de escolaridad de la población femenina',

]
INTEGER_COLUMNS=[
       'Población total','Población masculina', 'Población femenina',
       'Población de 8 a 14 años que no sabe leer y escribir',
       'Población masculina de 8 a 14 años que no sabe leer y escribir',
       'Población femenina de 8 a 14 años que no sabe leer y escribir',
       'Población de 15 años y más analfabeta',
       'Población masculina de 15 años y más analfabeta',
       'Población femenina de 15 años y más analfabeta',
       'Población de 5 años que no asiste a la escuela',
       'Población masculina de 5 años que no asiste a la escuela',
       'Población femenina de 5 años que no asiste a la escuela',
       'Población de 6 a 11 años que no asiste a la escuela',
       'Población de 6 a 14 años que no asiste a la escuela',
       'Población masculina de 6 a 14 años que no asiste a la escuela',
       'Población femenina de 6 a 14 años que no asiste a la escuela',
       'Población de 12 a 14 años que no asiste a la escuela',
       'Población de 15 a 24 años que asiste a la escuela',
       'Población masculina de 15 a 24 años que asiste a la escuela',
       'Población femenina de 15 a 24 años que asiste a la escuela',
       'Población de 15 años y más sin escolaridad',
       'Población masculina de 15 años y más sin escolaridad',
       'Población femenina de 15 años y más sin escolaridad',
       'Población de 15 años y más con educación básica incompleta',
       'Población masculina de 15 años y más con educación básica incompleta',
       'Población femenina de 15 años y más con educación básica incompleta',
       'Población de 15 años y más con educación básica completa',
       'Población masculina de 15 años y más con educación básica completa',
       'Población femenina de 15 años y más con educación básica completa',
       'Población de 15 años y más con educación posbásica',
       'Población masculina de 15 años y más con educación posbásica',
       'Población femenina de 15 años y más con educación posbásica',
    
]
FORMAT_COLUMNS={
    'string_columns':STRING_COLUMNS,
    'float_columns':FLOAT_COLUMNS,
    'integer_columns':INTEGER_COLUMNS

}

# Censos de Población y Vivienda
CENSOS_DE_POBLACION_Y_VIVIENDA_PATH="./CENSOS DE POBLACION Y VIVIENDA"
work_directory=CENSOS_DE_POBLACION_Y_VIVIENDA_PATH


dataframes=[]
diccionarios_de_datos=[]
for item in os.listdir(work_directory):
    item_path=f"{work_directory}/{item}"
    if os.path.isdir(item_path):
        file_name=os.listdir(f"{item_path}/conjunto_de_datos")[0]
        file_path=f"{item_path}/conjunto_de_datos/{file_name}"
        df=pd.read_csv(file_path)
        
        pattern = r"^diccionario.*datos$"
        for subitem in os.listdir(item_path):
            match = re.search(pattern,subitem)
            if match:
                dictionary_name=match.group()

        data_dictionary_path=f"{item_path}/{dictionary_name}/{os.listdir(f"{item_path}/{dictionary_name}")[0]}"
        dictionary_df=pd.read_csv(data_dictionary_path,encoding='ISO-8859-1')
        diccionarios_de_datos.append(dictionary_df)

    else:
        file_path=item_path
        df=pd.read_excel(file_path,sheet_name=1,skiprows=4)
    
    dataframes.append(df)
    print(f"Datos del archivo {item} se cargaron a la lista 'dataframes' ")

## Filtro columnas

def filtro_columnas(df,dictionary_dataframe,columns=COLUMNS):
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
    total_rows=len(df)
    for column in df.columns:
        nans=0
        nans=df[column].isna().sum()
        if nans!=0:
            print(f"{round(100*nans/total_rows,4)}% de los registros en {column} son nulos")
    
## Calidad de datos 

# Primero hacemos un diccionario que contiene el formato en la que conviene guardar cada columna

def formato_columnas(df,format_columns=FORMAT_COLUMNS):
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

    if len(error_columns)!=0:
        for error_column in error_columns:
                percentage=100*round(len(df[df[error_column[0]]==error_column[1]])/len(df),2)
                print(f"{percentage}% de los registros en {error_column[0]} son {error_column[1]} ")
                #df=df[~(df[error_column[0]]==error_column[1])]
                #print(f"Se omitieron los registros erroneos en {error_column[0]} exitosamente!")
    return error_columns
        


os.chdir("..")
os.chdir("..")
os.chdir("..")
os.chdir("./notebooks")