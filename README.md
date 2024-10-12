![MCD](https://mcd.unison.mx/wp-content/themes/awaken/img/logo_mcd.png)
# Educación y Salud Mental en México 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


**Objetivo**

Este proyecto se creó para completar asignaciones dentro de la maestría en ciencia de datos. Se analizará una posible relación entre el campo de salud mental y el de la educación en la población méxicana juvenil. Nuestro objetivo con este proyecto es lograr encontrar relaciones y/o hallazgos que nos ayuden responder de manera satisfactoria las preguntas: 

*¿Habrá alguna relación entre el desempeño acádemico y la salud mental de los estudiantes jovenes?*

*¿En que parte de la república es más probable de abandonar la escuela, y/o tener problemas de salud mental?¿Estarán relacionados/vínculados?*

*¿Existe alguna relación entre la pertenencia en la escuela y la salud mental en la población juvenil mexicana?*

Esperamos poder hallar resolución a estas incognitas y lograr comunicar nuestros hallazgos tanto al público general como directivos del área de educación.

**Acerca de las fuentes de datos**

Para la información relacionada con la educación en México, optamos por utilizar los resultados de encuestas del INEGI y un reporte del [SEP de indicadores educativos del 2023](https://www.planeacion.sep.gob.mx/indicadorespronosticos.aspx):
Nos apoyaremos del [Censo General de Población y Vivienda](https://www.inegi.org.mx/programas/ccpv/2020/) de varios años para obtener información georeferencial y temporal sobre la población méxicana que estudia. La [Encuesta Nacional sobre Acceso y Permanencia en la Educación (ENAPE) 2021](https://www.inegi.org.mx/programas/enape/2021/#tabulados) nos permitrá generar información estadística sobre el acceso y permanencia de la población de 0 a 29 años en el Sistema Educativo Nacional.

Mientras que para los datos relacionados con la salud mental se tomó como fuente principal la Encuesta Nacional de Salud y Nutrición, [ENSANUT](https://ensanut.insp.mx/), la cual se inició en año 2000. Se planeaba hacerla cada 6 años, sin embargo se realizó también en el 2016 y se lleva haciendo cada año desde el 2020. Dicha entrevista tiene dos apartados, salud y nutrición, y cada uno de estos se divide en adolesentes y mayores de 20 años en este proyecto se recauda cada catálogo de datos y los resultados de cada cuestionario de datos realizado, estos últimos se analizarán para saber si existe información sobre la salud mental de nuestros dos grupos de edades.

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
├── evaluation         <- Model evaluations, metrics, and reports
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
├── scripts         <- Useful scripts used for downloading,processing or visualizing data.
│
```

--------


## Ejecutando proyecto

1. Primero se tiene que creear el entorno ejecutando:

    ```bash
    make venv
    ```

2. Luego, se instalan las dependencias especificadas dentro del archivo 'requirements.txt':
    ```bash
    make install requirements
    ```

3. Se descargan los dos conjuntos de datos:
    ```bash
    make download educacion
    make download salud
    ```

4. Se procesan los dos conjuntos de datos:
    ```bash
    make process educacion
    make process salud
    ```


# Licencia
Este proyecto se rige bajo la licencia de MIT.
