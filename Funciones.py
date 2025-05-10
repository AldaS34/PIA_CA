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

def confirmar_respuesta():
    while True:
        respuesta = input("¿Deseas continuar? (S/N): ").strip().upper()
        if respuesta == 'S':
            return True
        elif respuesta == 'N':
            return False
        else:
            print("Respuesta no válida. Por favor ingresa 'S' o 'N'.")

def separador():
    print('*'*10)

def anual_o_semestral():
    while True:
        print("Es anual o semestral")
        print("1. Anual")
        print("2. Semestral")
        opcion = input("Opcion: ")
        if opcion == "1":
            plazo = "anual"
            break
        elif opcion == "2":
            plazo = "semestral"
            break
        else:
            print("Ingrese una opcion valida")
    return plazo

def cantidades_SoA(periodo,cuenta):
    lista_temp = {}
    while True:
        if periodo == "semestral":
            try:
                print(cuenta)
                valor1 = Decimal(input("Ingrese cuanto vale en el primer semestre: "))
                valor2 = Decimal(input("Ingrese cuanto vale en el segundo semestre: "))
                lista_temp["Primer semestre"] = valor1
                lista_temp["Segundo semestre"] = valor2
                break
            except:
                print("Datos ingresados no permitidos")
        else:
            try:
                valor1 = Decimal(input("Ingrese cuanto vale anualmente: "))
                lista_temp["Anuales"] = valor1
                break
            except:
                print("Datos ingresados no permitidos")
    return lista_temp

def obtener_porcentaje():
    while True:
        try:
            print ("Ingrese el porcentaje requerido(Ingrese como numero entero)")
            porcentaje = int(input(": "))

            porcentaje = Decimal(porcentaje * Decimal(0.01))
            return porcentaje
        except:
            print("Datos ingresados invalidos")

def obtener_empresa():
    while True:    
        print("==== INGRESO DE DATOS DE LA EMPRESA ====")
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
        print("Ingrese la cantidad de la cuenta")
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
            elif opcion.upper() == 'N':
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
        print("==== ESTADO DE SITUACION FINANCIERA ====")
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
        print("==== INGRESO DE PRODUCTOS ====")
        separador()
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
        print("9. Registrar producto")
        print("10. Terminar registro de productos (Seleccionar una vez haya creado todos sus productos)")
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
                    precio_prod1 = input("Ingrese el precio del producto en su primer semestre: ")
                    precio_prod2 = input("Ingrese el precio del producto en su segundo semestre: ")
                    try:
                        precios["sem1"] = Decimal(precio_prod1)
                        precios["sem2"] = Decimal(precio_prod2)
                        nuevo_producto.set_precioXsem(precios)
                        print("Precios ingresados") 
                        break       
                    except:
                        print("Error en los datos")
            case "3":
                ventas = {}
                while True:
                    cant_1 = input("Ingrese la cantidad de productos que se espera vender en el primer semestre: ")
                    cant_2 = input("Ingrese la cantidad de productos que se espera vender en el segundo semestre: ")
                    try:
                        ventas["sem1"] = Decimal(cant_1)
                        ventas["sem2"] = Decimal(cant_2)
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
                    print("3. Salir(Ingrese todos los materiales que necesite antes de salir)")
                    materiales_creados(materiales_cons)
                    opcion = input("Opción: ")

                    if opcion == "1":
                        material = obtener_material()
                        materiales_cons.append(material)
                        materiales.append(material)
                    elif opcion == "2":
                        if len(materiales_cons) > 0:
                            print("Presione '0' en caso de que no se quiera seleccionar ninguna opcion")
                            while True:
                                opcion = input("¿Cuál material desea usar (número)? ")
                                req = input("¿Cuánto se requiere del material? ")
                                try:
                                    opcion = int(opcion)
                                    if 0 < opcion <= len(materiales_cons) :
                                        material = materiales_cons[opcion - 1]
                                        material.req_mat = Decimal(req)
                                        materiales.append(material)
                                        break
                                    elif opcion == '0':
                                        break
                                    else:
                                        print("Ingrese un número válido dentro de la lista.")
                                except:
                                    print("Error en los datos ingresados.")
                        else:
                            print("Aún no hay materiales registrados.")
                    elif opcion == '3':
                        nuevo_producto.set_materiales(materiales)
                        print("Materiales ingresados")
                        break
                    else:
                        print("Ingrese una opción válida.")
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
                    precio_mo1 = input("Ingrese el costo de mano de obra por hora en el primer semestre: ")
                    precio_mo2 = input("Ingrese el costo de mano de obra por hora en el primer semestre: ")
                    try:
                        costosXhora["sem1"] = Decimal(precio_mo1)
                        costosXhora["sem2"] = Decimal(precio_mo2)
                        nuevo_producto.set_costo_obra(costosXhora)
                        print("Costo de mano de obra registrado")
                        break
                    except:
                        print("Error en los datos")
            case "7":
                while True:
                    inv_inicial = input("Ingrese cuanto inventario se tiene del producto al inicio del primer semestre: ")
                    try:
                        inv_inicial = Decimal(inv_inicial)
                        nuevo_producto.set_inv_inicial(inv_inicial)
                        print("Inventario inicial registrado")
                        break
                    except:
                        print("Error en los datos")
            case "8":
                while True:
                    inv_final = input("Ingrese cuanto inventario se tiene del primer producto al final del segundo semestre: ")
                    try:
                        inv_final = Decimal(inv_final)
                        nuevo_producto.set_inv_final(inv_final)
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
                        nuevo_producto = Producto()
                        print("Producto agregado")
                        break
                    elif opcion == "2":
                        print("Regresando al menu")
                        break
                    else:
                        print("Ingrese alguna de las opciones disponibles")
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
            case _:
                print("Opcion no valida")


def materiales_creados(materiales_cons):
        print("Lista de materiales ya creados")
        contador = 1
        if len(materiales_cons) == 0:
            print("N/A")
        else:
            for material in materiales_cons:
                    print(f"    {contador}. {material.nombre}")
                    contador += 1

def obtener_material():
    nuevo_mat= Material()
    while True:
        separador()
        print("Iniciando nuevo Material")
        print("")
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
                    nombre_mat = input("Ingrese nombre del material: ")
                    try:
                        nuevo_mat.set_nombre(nombre_mat)
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
                    req_mat = input("Ingrese cuanto se requiere del material: ")
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
                    separador()
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


def obtener_gastosAyV():
    gastos_ayv = GastosAyV()
    while True:
        print("==== INGRESO DE GASTOS DE ADMINISTRACIÓN Y VENTAS ====")    
        print("Menu")
        print("Seleccione la opcion indicanto el numero: ")
        print("1. Datos de Depeciacion")
        print("2. Datos de sueldos y salarios")
        print("3. Procentaje de comisiones")
        print("4. Datos de gastos varios")
        print("5. Datos de intereses por obligaciones")
        print("6. Terminar")
        opcion = input("Opcion: ")
        match opcion:
            case '1':
                print("Ingresar datos Depreciacion")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo,"Depreciacion" )
                gastos_ayv.set_depreciacion(cantidad)
            case '2':
                print("Ingresar datos para sueldos y salarios")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Sueldos y salarios")
                gastos_ayv.set_sueldosYsal(cantidad)
            case '3':
                print("Ingresar datos del porcentaje de comisiones")
                comisiones = obtener_porcentaje()
                gastos_ayv.set_comisiones(comisiones)
            case '4':
                print("Ingresar los datos de gastos varios")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Varios")
                gastos_ayv.set_varios(cantidad)
            case '5':
                print("Ingresar los datos de intereses por obligaciones")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Intereses por obligaciones")
                gastos_ayv.set_intereses(cantidad)
            case '6':
                print("Confirmar datos")
                gastos_ayv.mostrar_gastosAyV()
                if confirmar_respuesta():
                    return gastos_ayv
                else:
                    print("Regresando al menu")
            case _:
                print("Opcion invalida")




def obtener_gif():
    gif = GIF()
    while True:
        print("==== GASTOS INDIRECTOS DE FABRICACION ====")
        print("Menu")
        print("Seleccione la opcion indicanto el numero: ")
        print("1. Datos de Depeciacion")
        print("2. Datos de Seguros")
        print("3. Datos de mantenimieto")
        print("4. Datos de energéticos")
        print("5. Datos de intereses por obligaciones")
        print("6. Terminar")
        opcion = input("Opcion: ")
        match opcion:
            case '1':
                print("Ingresar datos Depreciacion")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo,"Depreciacion" )
                gif.set_depreciacion(cantidad)
            case '2':
                print("Ingresar datos para seguros")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Seguros")
                gif.set_seguros(cantidad)
            case '3':
                print("Ingresar datos de mantenimieto")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Mantenimiento")
                gif.set_mantenimiento(cantidad)
            case '4':
                print("Ingresar los datos de Energéticos")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Energéticos")
                gif.set_varios(cantidad)
            case '5':
                print("Ingresar los datos de intereses por obligaciones")
                periodo = anual_o_semestral()
                cantidad = cantidades_SoA(periodo, "Intereses por obligaciones")
                gif.set_intereses(cantidad)
            case '6':
                print("Confirmar datos")
                gif.mostrar_gif()
                if confirmar_respuesta():
                    return gif
                else:
                    print("Regresando al menu")
            case _:
                print("Opcion invalida")

def obtener_extras():
    extras = Extras()
    while True:
        print("==== Extras ====")
        print("Menu")
        print("Seleccione la opcion indicanto el numero: ")
        print("1. Datos de adquicisiones")
        print("2. Datos de Seguros")
        print("3. Datos de mantenimieto")
        print("4. Datos de energéticos")
        print("5. Datos de intereses por obligaciones")
        print("6. Terminar")
        opcion = input("Opcion: ")
        match opcion:
            case '1':
                n_cuentas = {}
                while True:
                    print("Registrar adquiciciones nuevas")
                    cuenta, cantidad =nueva_cuenta()
                    n_cuentas[cuenta] = cantidad
                    print("Presione tecla 'Enter' si quiere parar de ingresar nuevas adquisiciones")
                    opcion = input()
                    if opcion == "":
                        extras.set_cuentas_extra(n_cuentas)
                        break
            case '2':
                    print("Registrar tasa de ISR")
                    cantidad = obtener_porcentaje()
                    extras.set_isr(cantidad)
            case '3':        
                    print("Registrar tasa de PTU")
                    cantidad = obtener_porcentaje()
                    extras.set_ptu(cantidad)
            case '4':
                    print("Regitrar porcentaje que se cobrara del saldo de clientes")
                    cantidad = obtener_porcentaje()
                    extras.set_cobrar_clientes(cantidad)
            case '5':
                    print("Registrar porcentaje que se cobrara de ventas presupuestadas")
                    cantidad = obtener_porcentaje()
                    extras.set_cobrar_ventas(cantidad)
            case '6':
                    print("Registrar porcentaje que se pagara del saldo de proveedores ")
                    cantidad = obtener_porcentaje()
                    extras.set_pagar_prov(cantidad)
            case '7':
                    print("Registrar porcentaje que se pagara de compras presupuestadas ")
                    cantidad = obtener_porcentaje()
                    extras.set_pagar_comp(cantidad)
            case '8':
                    print("Confirmar datos")
                    extras.mostrar_extras()
                    if confirmar_respuesta():
                        return extras
                    else:
                        print("Regresando al menu")
            case _:
                print("Opcion invalida")
