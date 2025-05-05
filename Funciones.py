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
        nombre = input("Nombre de la cuenta: ").strip()
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
            opcion = input("Desea registrar los datos [S/N]: ").upper()
            if opcion == 'S':
                print("Datos registrados")
                break
            elif opcion == 'N':
                print("Se registraran los datos de nuevo")
            else:
                print("Ingrese S o N")
        else: 
            print("Su balance no cuadra, revise informacion")
    return nuevo_esf

def obtener_productos():
    materiales_cons = []
    productos = []
    nuevo_producto= Producto()
    while True:
        print("Apartado de productos")
        print("")
        print("Ingrese numero de la opcion:")
        print("1. Nombre del producto")
        print("2. Definir precios por semestre")
        print("3. Definir ventas planeadas por semestre")    
        print("4. Agregar Materiales")
        print("5. Definir horas de mano de obra")
        print("6. Definir costo de la hora por la mano de obra")
        print("7. Definir inventario inicial del primer semestre")
        print("8. Definir inventario final del segundo semestre")
        print("9. Finalizar creacion de producto")
        print("10. Terminar seccion de productos (Seleccionar una vez haya creado todos sus productos)")
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
                precios = {}
                while True:
                    precio_1 = input("Ingrese el precio del producto en su primer semestre: ")
                    precio_2 = input("Ingrese el precio del producto en su segundo semestre: ")
                    try:
                        precios["sem1"] = Decimal(precio_1)
                        precios["sem2"] = Decimal(precio_2)
                        nuevo_producto.set_precioXsem(precios)
                        print("Precios ingresados") 
                        break       
                    except:
                        print("Error en los datos")
            case "3":
                ventas = {}
                while True:
                    precio_1 = input("Ingrese la cantidad de productos que se espera vender en el primer semestre: ")
                    precio_2 = input("Ingrese la cantidad de productos que se espera vender en el segundo semestre: ")
                    try:
                        ventas["sem1"] = Decimal(precio_1)
                        ventas["sem2"] = Decimal(precio_2)
                        nuevo_producto.set_ventas_plan(ventas)
                        print("Ventas ingresadas")
                        break
                    except:
                        print("Error en los datos")
            case "4":
                materiales = []
                while True:
                    print("Menu:")
                    print("1. Agregar nuevo material")
                    print("2. Usar material ya creado")
                    materiales_creados(materiales_cons)
                    opcion = input("Opcion: ")
                    if opcion == "1":
                           material = obtener_material()
                           materiales_cons.append(material)
                           materiales.append(material)
                           break
                    elif opcion == "2":
                            if len(materiales_cons) > 0:
                                while True:
                                    opcion = input("Cual material desea usar: ")
                                    req = input("Cuanto se requiere del material: ")
                                    try:
                                        opcion = int(opcion)
                                        if opcion <= len(materiales_cons) and opcion > 0:
                                            material = materiales_cons[opcion]
                                            material.req_mat = req
                                            materiales.append(material)
                                            break
                                        else:
                                            print("Ingrese un numero que este dentro de la lista")
                                    except:
                                        print("Error en los datos")
                                break
                            else:
                                print("Aun no hay materiales registrados")
                    else:
                        print("Ingerse una opcion valida")
                while True:
                    print("¿Agregar otro material?")
                    opcion = input("[S/N]: ").upper()
                    if opcion == 'Y':
                        print("Agregando otro material")
                    elif opcion == 'N':
                        nuevo_producto.set_materiales(materiales)
                        print("Materiales agregados")
                        break
                    else:
                        print("Ingrese S o N")
            case "5":
                while True:
                    obra_horas = input("Ingrese las horas de mano de obra para realizar el producto: ")
                    try:
                        obra_horas = Decimal(obra_horas)
                        nuevo_producto.set_horas_obra(obra_horas)
                        print("Horas registradas")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
            case "6":
                costosXhora = {}
                while True:
                    precio_1 = input("Ingrese el costo de mano de obra por hora en el primer semestre: ")
                    precio_2 = input("Ingrese el costo de mano de obra por hora en el primer semestre: ")
                    try:
                        costosXhora["sem1"] = Decimal(precio_1)
                        costosXhora["sem2"] = Decimal(precio_2)
                        nuevo_producto.set_costo_obra(costosXhora)
                        print("Costo de mano de obra registrado")
                        break
                    except:
                        print("Error en los datos")
            case "7":
                while True:
                    inv_inicial = input("Ingrese cuanto inventario se tiene del primer producto al inicio del primer semestre")
                    try:
                        inv_inicial = Decimal(inv_inicial)
                        nuevo_producto.set_inv_inicial(inv_inicial)
                        print("Inventario inicial registrado")
                        break
                    except:
                        print("Error en los datos")
            case "8":
                while True:
                    inv_final = input("Ingrese cuanto inventario se tiene del primer producto al final del segundo semestre")
                    try:
                        inv_final = Decimal(inv_inicial)
                        nuevo_producto.set_inv_inicial(inv_final)
                        print("Inventario inicial registrado")
                        break
                    except:
                        print("Error en los datos")
            case "9":
                while True:
                    print("Revisar datos del producto para terminar su registro")
                    nuevo_producto.mostrar_producto()
                    separador()
                    print("1. Guardar producto")
                    print("2. Regresar a menu de creacion de producto")
                    opcion = input("Opcion: ")
                    if opcion == "1":
                        productos.append(nuevo_producto)
                        print("Producto agregado")
                    elif opcion == "2":
                        print("Regresando al menu")
                        break
                    else:
                        print("Ingrese alguna de las opciones disponibles")
                    print("Desea agregar otro producto o terminar con la seccion de productos")
            case "10":
                    print("Desea agregar otro producto o terminar con la seccion de productos")
                    for producto in productos:
                        print(f"-{producto.nombre}")
                    opcion = input("[S/N]: ").upper()
                    if opcion == "N":
                        print("Productos registrados")
                        return productos
                    elif opcion == "S":
                        print("Regresando a crear un nuevo producto")
                        nuevo_producto = Producto()
            case _:
                print("Opcion no valida")


def materiales_creados(materiales_cons):
        print("Lista de materiales ya creados")
        contador = 1
        for material in materiales_cons:
                print(f"    {contador}. {material.nombre}")
                contador += 1


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
                        break
                    else:
                        print("Ingrese S o N")
            case _:
                print("Opcion no valida")
