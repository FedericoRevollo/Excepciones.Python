# Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muetra.

def accederClaveDiccionario():
    diccionario = {}
    print("\n--------------------")
    # Se le pide al usuario que complete el diccionario
    while True:
        clave = input("\nIntroduce una clave (o escribe 'salir' para terminar): ")
        if clave.lower() == 'salir':
            break
        valor = input(f"Introduce el valor para la clave '{clave}': ")
        diccionario[clave] = valor
    
    print("\nDiccionario completo:")
    print(diccionario)

    # Se pide una clave que puede no existir
    try:
        claveBuscar = input("\nIntroduce la clave que quieres buscar en el diccionario: ")
        valor = diccionario[claveBuscar]
        print(f"El valor de la clave '{claveBuscar}' es: {valor}")
        
    except KeyError:
        print(f"Error: La clave '{claveBuscar}' no existe en el diccionario.")
    finally:
        print("\n--------------------\n")

accederClaveDiccionario()