# Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

def sumar():
    try:
        print("\n--------------------\n")
        num = float(input("Introduce un número: "))
        texto = input("\nIntroduce un texto: ")
        
        resultado = num + texto
        print(f"\nEl resultado de la suma es: {resultado}")
        
    except TypeError:
        print("\nError: No se puede sumar un número y un texto.")
    except ValueError:
        print("\nError: Introduce valores numéricos válidos.")
    finally:
        print("\n--------------------\n")

sumar()