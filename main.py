from Funciones import *

while True:
    while True:
        menu()
        opcion = input("Opcion: ")
        match opcion:
            case '1':
                # empresa = obtener_empresa()
                # esf = obtener_ESF(empresa)
                productos = obtener_productos()
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case _:
                separador()
                print("Ingrese una opcion valida")
                separador()




