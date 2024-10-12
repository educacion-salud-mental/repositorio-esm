# Variables definidas
VENV_DIR=venv
PYTHON=python3
REQUIREMENTS=requirements.txt
DOWNLOAD_SCRIPT_ED=ed-download-data.py  
DOWNLOAD_SCRIPT_SM=sm-download-data.py
PROCESS_SCRIPT_ED=ed-proc-data.py
PROCESS_SCRIPT_SM=sm-inter-proc-data.py

# Detectar sistema operativo
ifeq ($(OS),Windows_NT)
    # Comandos para Windows
    VENV_ACTIVATE=$(VENV_DIR)\Scripts\activate.bat
    PYTHON_EXEC=$(VENV_DIR)\Scripts\python
    PIP_EXEC=$(VENV_DIR)\Scripts\pip
else
    # Comandos para macOS/Linux
    VENV_ACTIVATE=$(VENV_DIR)/bin/activate
    PYTHON_EXEC=$(VENV_DIR)/bin/python
    PIP_EXEC=$(VENV_DIR)/bin/pip
endif

# Regla principal para ejecutar todo
all: venv install run

# Regla para crear un ambiente virtual
venv:
	$(PYTHON) -m venv $(VENV_DIR)

# Regla para instalar dependencias
install requirements: venv
	$(PIP_EXEC) install -r $(REQUIREMENTS)


# Reglas para descargar datos
download educacion:install
	$(PYTHON_EXEC) $(DOWNLOAD_SCRIPT_ED)

download salud:install
	$(PYTHON_EXEC) $(DOWNLOAD_SCRIPT_SM)

# Reglas para procesar datos
process educacion:install
	$(PYTHON_EXEC) $(PROCESS_SCRIPT_ED)

process salud:install
	$(PYTHON_EXEC) $(PROCESS_SCRIPT_SM)




# Regla para limpiar el ambiente virtual
clean:
	rm -rf $(VENV_DIR)

.PHONY: all venv install run clean
