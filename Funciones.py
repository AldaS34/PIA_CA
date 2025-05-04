from datos import *
from decimal import *
from tabulate import *

def menu():
    print("Menu")
    print("Seleccione la opcion indicanto el numero: ")
    print("1. Iniciar Presupuesto")
    print("2. Consultar Presupuesto")
    print("3. Eliminar Presupuesto")
    print("4. Salir")

def separador():
    print('*'*10)

def obtener_empresa():
    while True:    
        print("Dato de la empresa")
        nom_empresa=input("Ingrese el nombre de la empresa: ")
        anio_actual = input("Ingrese el año actual: ")
        anio_previo = input("Ingrese el año previo al actual: ")
        datos_empresa = Empresa(nom_empresa, anio_actual, anio_previo)
        datos_empresa.mostrar_empresa()
        separador()
        while True:
            opcion =input("Los datos son correctos [S/N]").upper()
            if opcion.upper() == 'S':
                print("Datos confirmados")
                return datos_empresa
            elif opcion.upper() == 'N':
                print("Reiniciando ingreso de datos")
                separador()
                break
            else:
                print("Ingrese S o N")
                separador()

def validar_cantidad(cuenta):   
    while True:
        entrada = input(f"{cuenta}: ")
        try:
            cantidad = Decimal(entrada)
            if cantidad > 0:
                return cantidad
            else:
                print("Cantidad inválida. Debe ser un número positivo.")
        except InvalidOperation:
            print("Entrada inválida. Ingresa solo números.")

def nueva_cuenta():
    while True:
        nombre = str(input("Nombre de la cuenta: ")).strip()
        cantidad = validar_cantidad(nombre)
        print(f"{nombre}: ${cantidad}")
        while True:
            opcion = input("¿Es correcto? [S/N]")
            if opcion.upper() == 'S':
                return nombre, cantidad
            elif opcion.upper == 'N':
                print("Reingresa los datos")
                separador()
                break
            else:
                print("Opcion invalida")
                separador()

def perdida_valor():
    while True:
        opcion = input("Genera alguna perdida de valor [S/N]").upper()
        if opcion == 'S':
            tipo = -1
            break
        elif opcion == 'N':
            tipo = 1
            break
        else:
            print("Ingrese S o N")
    return tipo 

def obtener_ESF(empresa):
    while True:
        activos_circulantes = {}
        activos_no_circulantes = {}
        pasivos_corto = {}
        pasivos_largo = {}
        capital = {}
        print("Ingrese el valor monetario de las cuentas")
        print("Activos: ")
        print("Circulante")
        clientes = validar_cantidad("clientes")
        while True:
            opcion = input("Desea agregar algun activo circulante [S/N] ").upper()
            if opcion == 'S':
                nombre, cantidad = nueva_cuenta()
                tipo = perdida_valor()
                activos_circulantes[nombre]= cantidad * tipo
            elif opcion == 'N':            
                print("Datos registrados")
                break
            else:
                print("Ingrese S o N")
        print("No circulante")
        while True:
            opcion = input("Desea agregar algun activo no circulante [S/N]").upper()
            if opcion == 'S':
                nombre,cantidad= nueva_cuenta()
                tipo = perdida_valor()
                activos_no_circulantes[nombre] = cantidad * tipo
            elif opcion == 'N':
                print("Datos Ingresados")
                break
            else:
                print("Ingrese S o N")
        print("Pasivos")
        print("Pasivos a Corto Plazo")
        proveedores = validar_cantidad("Proveedores")
        while True:
            opcion = input("Desea agregar algun pasivo a corto plazo [S/N]").upper()
            if opcion == 'S':
                nombre, cantidad = nueva_cuenta()
                pasivos_corto[nombre] = cantidad
            elif opcion == 'N':
                print("Datos Ingresados")
                break
            else:
                print("Ingrese S o N")
        print("Pasivos a Largo Plazo")
        while True:
            opcion = input("Desea agregar algun pasivo a largo plazo [S/N]").upper()
            if opcion == 'S':
                nombre, cantidad = nueva_cuenta()
                pasivos_largo[nombre] = cantidad
            elif opcion == 'N':
                print("Datos Ingresados")
                break
            else:
                print("Ingrese S o N")
        print("Capital Contable")
        while True:
            opcion = input("Desea agregar alguna cuenta de capital contable [S/N]").upper()
            if opcion == 'S':
                nombre, cantidad  = nueva_cuenta()
                capital[nombre] = cantidad
            elif opcion == 'N':
                print("Datos Ingresados")
                break
            else:
                print("Ingrese S o N")
        separador()
        nuevo_esf = ESF(clientes, proveedores,activos_circulantes
                        ,activos_no_circulantes,pasivos_corto,pasivos_largo,
                        capital)
            
        nuevo_esf.mostrar_ESF(empresa)
        confirmacion = nuevo_esf.balance_cuadrado()
        if confirmacion:
            opcion = input("Desea registrar los datos [S/N]").upper()
            if opcion == 'S':
                print("Datos registrados")
                break
            elif opcion == 'N':
                print("Se registraran los datos de nuevo")
            else:
                print("Ingrese S o N")
    return nuevo_esf

def obtener_producto():
    nuevo_producto= Producto()
    while True:
        print("Apartado de productos")
        print("")
        print("Ingrese numero de la opcion:")
        print("1. Nombre del producto")
        print("2. Definir precios por semestre")
        print("3. Definir ventas planeadas por semestre")    
        print("4. Agregar Material (Se pueden agregar multiples materiales)")
        print("5. Definir horas de mano de obra")
        print("6. Definir costo de la hora por la mano de obra")
        print("7. Definir inventario inicial del primer semestre")
        print("8. Definir inventario final del segundo semestre")
        print("9. Finalizar creacion de producto")
        opcion = input("Opcion: ")
        match opcion:
            case "1":
                while True:
                    nombre= str(input("Ingrese nombre del producto: ")).strip()
                    if nombre == "":
                        print("No puede dejar el nombre vacio")
                    else:
                        nuevo_producto.set_nombre(nombre)
                        print("Nombre registrado")
                        break
            case "2":
                while True:
                    pass
            case "3":
                pass

            case "4":
                pass

            case "5":
                pass

            case "6":
                pass
            
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass






def obtener_material():
    nuevo_mat= Material()
    while True:
        print("Iniciando nuevo Material")
        print("Ingrese numero de la opcion:")
        print("1. Nombre del material")
        print("2. Unidad de medida del material")
        print("3. Requerimiento del material")
        print("4. Definir inventario inicial del primer semestre")
        print("5. Definir inventario final del segundo semestre")
        print("6. Definir costos por semestre")
        print("7. Finalizar material")
        opcion = input("Opcion: ")
        match opcion:
            case "1":
                while True:
                    nombre = input("Ingrese nombre del material: ")
                    try:
                        nuevo_mat.set_nombre(nombre)
                        print("Nombre Ingresado")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
            case "2":
                while True:
                    unidad = input("Ingrese la unidad del material: ")
                    try:
                        nuevo_mat.set_unidad(unidad)
                        print("Unidad ingresada")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
            case "3":
                while True:
                    req_mat = input("Ingrese cuanto se requiere del material")
                    try:
                        req_mat = Decimal(req_mat)
                        nuevo_mat.set_req_mat(req_mat)
                        print("Material requerido ingresado")
                        break
                    except:
                        print("Error en los datos")
            case "4":
                while True:
                    inv_inicial = input("Ingrese cuanto hay en inventario del material al inicio el primer semestre: ")
                    try:
                        inv_inicial = Decimal(inv_inicial)
                        nuevo_mat.set_inv_inicial(inv_inicial)
                        print("Inventario inicial ingresado")
                        break
                    except:
                        print("Error en los datos")
            case "5":
                while True:
                    inv_final = input("Ingrese cuanto hay de inventario del material al final del segundo semestre: ")
                    try:
                        inv_final = Decimal(inv_final)
                        nuevo_mat.set_inv_final(inv_final)
                        print("Inventario final ingresado")
                        break
                    except:
                        print("Error en los datos")
            case "6":
                while True:
                    costosXsem = {}
                    try:
                        costo_1 = Decimal(input("Ingrese cuanto cuesta el material en su primer semestre: "))
                        costo_2 = Decimal(input("Ingrese cuanto cuesta el material en su segundo semestre: "))
                        costosXsem["sem1"] = costo_1
                        costosXsem["sem2"] = costo_2
                        nuevo_mat.set_costoXsem(costosXsem)
                        print("Costos por semestre ingresados")
                        break
                    except:
                        print("Error en los datos")
            case "7":
                while True:
                    nuevo_mat.info_material()
                    separador()
                    print("Confirme la informacion para terminar el registro")
                    opcion = input("[S/N]: ").upper()
                    if opcion == 'S':
                        print("Material agregado")
                        return nuevo_mat
                    elif opcion == 'N':
                        print('Regresando al menu de Materiales')
                    else:
                        print("Ingrese S o N")
