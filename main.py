from Funciones import *


lista_presupuestos = []
while True:
    while True:
        menu()
        opcion = input("Opcion: ")
        match opcion:
            case '1':
                empresa = obtener_empresa()
                esf = obtener_ESF(empresa)
                productos = obtener_productos()
                gastos_ayv = obtener_gastosAyV()
                gif = obtener_gif()
                extras = obtener_extras()
                nueva_cedula= Cedulas(empresa,esf,gastos_ayv,gif,extras)
                lista_presupuestos.append(nueva_cedula)
                print("Datos de presupuesto Registrados")
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




