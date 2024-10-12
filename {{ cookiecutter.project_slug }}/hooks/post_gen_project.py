'''
    import os
import subprocess

def init_git_repo():
    """Inicializa un repositorio Git en el directorio del proyecto."""
    if not os.path.exists(".git"):
        print("Inicializando un nuevo repositorio Git...")
        subprocess.run(["git", "init"])
        print("Repositorio Git inicializado.")
    else:
        print("El repositorio Git ya está inicializado.")

def make_initial_commit():
    """Hace un commit inicial después de agregar todos los archivos."""
    print("Añadiendo archivos al repositorio...")
    subprocess.run(["git", "add", "."])

    print("Haciendo el commit inicial...")
    subprocess.run(["git", "commit", "-m", "Initial commit"])

def link_remote_repo(remote_url):
    """Conecta el repositorio local al repositorio remoto."""
    print(f"Ligando el repositorio al remoto {remote_url}...")
    subprocess.run(["git", "remote", "add", "origin", remote_url])

    # Opcional: Establecer la rama principal como 'main'
    subprocess.run(["git", "branch", "-M", "main"])

def push_to_remote():
    """Hace push de los cambios al repositorio remoto."""
    print("Haciendo push de los cambios al repositorio remoto...")
    subprocess.run(["git", "push", "-u", "origin", "main"])

# Inicializar el repositorio Git
init_git_repo()

# Hacer el commit inicial
make_initial_commit()

# Definir la URL del repositorio remoto
remote_url = input("Introduce la URL del repositorio remoto: ")

# Ligar el repositorio local con el remoto
if remote_url:
    link_remote_repo(remote_url)
    push_to_remote()
else:
    print("No se proporcionó la URL del repositorio remoto. No se hará push.")
'''

if __name__ == "__main__":
    print("se ejecuta post")
