'''

import os
import subprocess
import sys

def is_installed(command):
    """Verifica si un comando está disponible en el sistema."""
    try:
        subprocess.run([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def install_anaconda():
    """Instala Anaconda en el sistema si no está instalado."""
    anaconda_installer_url = "https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh"
    
    if sys.platform.startswith("win"):
        print("Descargando e instalando Anaconda para Windows...")
        # Aquí puedes definir un script o método para instalar Anaconda en Windows
    elif sys.platform.startswith("darwin"):
        print("Descargando e instalando Anaconda para macOS...")
        anaconda_installer_url = "https://repo.anaconda.com/archive/Anaconda3-latest-MacOSX-x86_64.sh"
    else:
        print("Descargando e instalando Anaconda para Linux...")
    
    installer_file = "AnacondaInstaller.sh"
    
    # Descargar el instalador
    subprocess.run(["curl", "-o", installer_file, anaconda_installer_url])
    
    # Hacer el archivo ejecutable
    subprocess.run(["chmod", "+x", installer_file])
    
    # Ejecutar el instalador
    subprocess.run([f"./{installer_file}"])

    # Eliminar el instalador después de la instalación
    os.remove(installer_file)

def install_git():
    """Instala Git si no está presente."""
    if sys.platform.startswith("win"):
        print("Por favor instala Git manualmente en Windows desde https://git-scm.com/")
    elif sys.platform.startswith("darwin"):
        print("Instalando Git con Homebrew en macOS...")
        subprocess.run(["brew", "install", "git"])
    else:
        print("Instalando Git en Linux...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "git"])

def create_conda_env():
    """Crea el entorno de conda a partir del archivo environment.yml."""
    if os.path.exists("environment.yml"):
        print("Creando entorno conda desde environment.yml...")
        subprocess.run(["conda", "env", "create", "-f", "environment.yml"])
        subprocess.run(["conda", "run", "-n", "virtualEnvIngCarac", "python3", "--version"])
    else:
        print("El archivo environment.yml no existe.")

# Verificar si Anaconda está instalado
if not is_installed("conda"):
    print("Anaconda no está instalado. Procediendo a la instalación.")
    install_anaconda()
else:
    print("Anaconda ya está instalado.")

# Verificar si Git está instalado
if not is_installed("git"):
    print("Git no está instalado. Procediendo a la instalación.")
    install_git()
else:
    print("Git ya está instalado.")

# Crear entorno conda a partir del archivo environment.yml
create_conda_env()


'''


def main():
    print("se ejecuta pre")

if __name__ == "__main__":
    main()
