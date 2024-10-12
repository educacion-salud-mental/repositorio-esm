# Define variables
VENV_DIR=venv
PYTHON=python3
REQUIREMENTS=requirements.txt
SCRIPT=your_script.py  # Reemplaza con el nombre de tu archivo .py

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
install: venv
	$(PIP_EXEC) install -r $(REQUIREMENTS)

# Regla para ejecutar el script
run: install
	$(PYTHON_EXEC) $(SCRIPT)

# Regla para limpiar el ambiente virtual
clean:
	rm -rf $(VENV_DIR)

.PHONY: all venv install run clean
