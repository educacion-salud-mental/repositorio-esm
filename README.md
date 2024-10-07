# Proyecto de ingeniería de características 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Este proyecto se creó para completar asignaciones dentro de la maestría en ciencia de datos. Se analizará una posible relación entre el campo de salud mental y el de la educación en la población méxicana juvenil. 

**Objetivo**

Nuestro objetivo con este proyecto es lograr encontrar relaciones y/o hallazgos que nos ayuden responder de manera satisfactoria las preguntas: 

*¿ Habrá alguna correlación entre el desempeño acádemico y la salud mental de los estudiantes jovenes?*

*¿ En que parte de la republica es más probable de abandonar la escuela, y/o tener problemas de salud mental?¿Estarán relacionados/vínculados?*

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

---

## 1. Instalar Anaconda

### Paso 1: Descargar el Instalador
1. Visita la página oficial de Anaconda: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution).
2. Selecciona la versión correspondiente a tu sistema operativo (Windows, macOS o Linux) y descárgala.

### Paso 2: Instalar Anaconda
- En **Windows/macOS**: Ejecuta el instalador descargado y sigue las instrucciones en pantalla.
- En **Linux**: Abre una terminal y ejecuta el siguiente comando para iniciar la instalación:

    ```bash
    bash ~/Downloads/Anaconda3-2024.XX-Linux-x86_64.sh
    ```

### Paso 3: Verificar la Instalación
Una vez completada la instalación, abre una terminal o el `Anaconda Prompt` y ejecuta:

```bash
conda --version
