from Funciones import *
import pickle
import os


def guardar_presupuestos(lista):
    with open("presupuestos.pkl", "wb") as f:
        pickle.dump(lista, f)

def cargar_presupuestos():
    if os.path.exists("presupuestos.pkl"):
        with open("presupuestos.pkl", "rb") as f:
            return pickle.load(f)
    return []


lista_presupuestos = cargar_presupuestos()

while True:
    menu()
    opcion = input("Opción: ")
    match opcion:
        case '1':
            empresa = obtener_empresa()
            esf = obtener_ESF(empresa)
            productos = obtener_productos()
            gastos_ayv = obtener_gastosAyV()
            gif = obtener_gif()
            extras = obtener_extras()
            nueva_cedula = Cedulas(empresa, esf, productos, gastos_ayv, gif, extras)
            lista_presupuestos.append(nueva_cedula)
            guardar_presupuestos(lista_presupuestos)
            print("Datos de presupuesto registrados.")
        
        case '2':
            if lista_presupuestos:
                cedula_actual = lista_presupuestos[-1]  
                cedula_actual.gif.set_mantenimiento({"Primer semestre": Decimal("33000"), "Segundo semestre": Decimal("25000")})
                print("1. Ver cedulas")
                print("2. Ver presupuesto financiero")
                opcion = input("Ingrese el numero de la opcion: ")
                if opcion == "1":
                    cedula_actual.mostrar_P_ventas()
                    cedula_actual.mostrar_saldo_clientes()
                    cedula_actual.mostrar_presupuesto_prod()
                    cedula_actual.mostrar_req_mat()
                    cedula_actual.mostrar_compra_mat()
                    cedula_actual.mostrar_saldo_proveedores()
                    cedula_actual.mostrar_MOD()
                    cedula_actual.mostrar_GIF()
                    cedula_actual.mostrar_GDO()
                    cedula_actual.mostrar_CUPT()
                    cedula_actual.mostrar_inv_final()
                elif opcion == '2':
                    cedula_actual.mostrar_PresupuestoFinanciero()
                else:
                    print("Ingrese opcion valida")
            else:
                print("No hay presupuestos registrados todavía.")
        
        case '3':
            print("Saliendo del programa")
            break
        
        case _:
            separador()
            print("Ingrese una opción válida.")
            separador()
            




