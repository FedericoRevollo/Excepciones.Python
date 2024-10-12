# Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

def division():
    try:
        print("\n--------------------\n")
        numerador = float(input("Introduce el primer número (numerador): "))
        denominador = float(input("\nIntroduce el segundo número (denominador): "))
        
        resultado = numerador / denominador
        print(f"\nEl resultado de la división es: {resultado}")
        
    except ZeroDivisionError:
        print("\nError: No se puede dividir por cero.")
    finally:
        print("\n--------------------\n")

division()