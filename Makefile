# Nombre del entorno conda
CONDA_ENV = virtualEnvIngCarac

# Archivo de entorno para Anaconda (puede ser environment.yml)
ENV_FILE = environment.yml

# Nombre del script que descarga los datoså
DOWNLOAD_SCRIPT = sm-inter-proc-data.py

# URL de la API o fuente de datos para la descarga masiva
DATA_URL = https://api.example.com/data

# Crear el entorno conda a partir de un archivo environment.yml
.PHONY: conda_env
conda_env:
	conda env create -f $(ENV_FILE) --name $(CONDA_ENV)

# Activar el entorno conda e instalar dependencias desde requirements.txt si no usas environment.yml
.PHONY: install
install: conda_env
	conda activate $(CONDA_ENV) 

# Ejecutar el script de descarga de datos con el entorno conda activado
.PHONY: download
download: install
	conda run -n $(CONDA_ENV) python $(DOWNLOAD_SCRIPT) $(DATA_URL)
