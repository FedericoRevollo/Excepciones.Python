# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra el error al usuario. Sin embargo, también intenta crear el archivo si no existe.

def abrirArchivo():
    archivo = "archivo.txt"
    print("\n--------------------\n")
    try:
        # Intentamos abrir el archivo
        with open(archivo, 'r') as f:
            contenido = f.read()
            print("Contenido del archivo:")
            print(contenido)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
        print("Creando el archivo...")
        
        # Si el archivo no existe, lo creamos
        with open(archivo, 'w') as f:
            f.write("Contenido del archivo recién creado-->>Federico Revollo.\n")
            print(f"El archivo '{archivo}' ha sido creado exitosamente.")
    finally:
        print("\n--------------------\n")
        
abrirArchivo()