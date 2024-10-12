# Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

def division():
    try:
        print("\n--------------------\n")
        numerador = float(input("Introduce el primer número (numerador): "))
        denominador = float(input("\nIntroduce el segundo número (denominador): "))
        
        resultado = numerador / denominador
        print(f"\nEl resultado de la división es: {resultado}")
        
    except ZeroDivisionError:
        print("\nError: No se puede dividir por cero.")
    except ValueError:
        print("\nError: Introduce valores numéricos válidos.")
    finally:
        print("\n--------------------\n")

division()
