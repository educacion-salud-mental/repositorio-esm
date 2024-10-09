![MCD](https://mcd.unison.mx/wp-content/themes/awaken/img/logo_mcd.png)
# Educación y Salud Mental en México 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Este proyecto se creó para completar asignaciones dentro de la maestría en ciencia de datos. Se analizará una posible relación entre el campo de salud mental y el de la educación en la población méxicana juvenil. 

**Objetivo**

Nuestro objetivo con este proyecto es lograr encontrar relaciones y/o hallazgos que nos ayuden responder de manera satisfactoria las preguntas: 

*¿ Habrá alguna correlación entre el desempeño acádemico y la salud mental de los estudiantes jovenes?*

*¿ En que parte de la república es más probable de abandonar la escuela, y/o tener problemas de salud mental?¿Estarán relacionados/vínculados?*

Esperamos poder hallar resolución a estas incognitas y lograr comunicar nuestros hallazgos tanto al público general como directivos del área de educación.

**Acerca de las fuentes de datos**

Para la información relacionada con la educación en México, optamos por utilizar los resultados de encuestas del INEGI y un reporte del SEP de indicadores educativos:
Nos apoyaremos del Censo General de Población y Vivienda de varios años para obtener información georeferencial y temporal sobre la población méxicana que estudia. La Encuesta Nacional sobre Acceso y Permanencia en la Educación (ENAPE) 2021 nos permitrá generar información estadística sobre el acceso y permanencia de la población de 0 a 29 años en el Sistema Educativo Nacional.

Mientras que para los datos relacionados con la salud mental se tomó como fuente principal la Encuesta Nacional de Salud y Nutrición, ENSANUT, la cual se inició en año 2000. Se planeaba hacerla cada 6 años, sin embargo se realizó también en el 2016 y se lleva haciendo cada año desde el 2020. Dicha entrevista tiene dos apartados, salud y nutrición, y cada uno de estos se divide en adolesentes y mayores de 20 años en este proyecto se recauda cada catálogo de datos y los resultados de cada cuestionario de datos realizado, estos últimos se analizarán para saber si existe información sobre la salud mental de nuestros dos grupos de edades.

Posteriormente se buscará la manera de unir la información de educación y salud mental de una manera sensata y poder hacer una estadistica sobre estos datos.
## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
├── helpers            <- Esta carpeta se utiliza para colocar funciones de utilidad
│                         o archivos auxiliares que pueden ser reutilizados en todo el
│                         proyecto.
│        
├── models             <- Trained and serialized models, model predictions, or model summaries
├── pipelines          <- Data processing pipelines or trained and serialized models
├── evaluetion         <- Model evaluations, metrics, and reports
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
```

--------


# Guía de Instalación y Uso de Anaconda

## Requisitos Previos
Para seguir esta guía, necesitarás acceso a Internet y permisos de instalación en tu sistema.

----------------

# Guía de Configuración del Entorno

Este documento proporciona los pasos necesarios para instalar Anaconda, Python, crear y activar un ambiente virtual con Anaconda, y ejecutar un archivo `environment.yml` usando Conda.

## 1. Verificación e Instalación de Anaconda

### Verificar si Anaconda está instalado:
1. Abre una terminal y ejecuta el siguiente comando:

    ```bash
    conda --version
    ```

2. Si el comando anterior muestra una versión de Conda, significa que Anaconda está instalada. Si no aparece, sigue los pasos de instalación a continuación.

### Instalación de Anaconda:
1. Descarga el instalador de Anaconda desde [aquí](https://www.anaconda.com/products/individual#download-section).
2. Ejecuta el instalador y sigue las instrucciones en pantalla.
3. Reinicia tu terminal y verifica la instalación con el siguiente comando:

    ```bash
    conda --version
    ```

## 2. Instalación de Python

1. Python viene incluido con Anaconda. Para verificar la versión de Python instalada, ejecuta:

    ```bash
    python --version
    ```

2. Si deseas instalar una versión específica de Python, puedes hacerlo creando un ambiente con esa versión (ver el siguiente paso).

## 3. Crear un Ambiente Virtual con Anaconda

Para crear un ambiente virtual con Anaconda, ejecuta el siguiente comando, reemplazando `nombreEntornoVirtual` con el nombre que deseas para tu ambiente y `3.x` con la versión de Python que desees (si es necesario):

```bash
conda create --name nombreEntornoVirtual -> crea el entorno virtual
conda activate nombreEntornoVirtual -> activa el entorno virtual
conda deactivate -> en caso de quere salir del entorno virtual es posible desactivarlo para volver al entorno base
conda env update --file environment.yml -> actualiza el archivo environment.yml en caso de instalar más paquetes o librerías
