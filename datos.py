from tabulate import *
from decimal import *
import unicodedata

def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

class Empresa():
    def __init__(self,nombre,anio_actual,anio_siguiente):
        self.nombre = nombre
        self.anio_actual = anio_actual
        self.anio_siguiente = anio_siguiente

    def mostrar_empresa(self):
        print(f"{self.nombre:^10}")
        print(f"al 31 de diciembre de {self.anio_actual}")
        print(f"Presupuesto del 1 de Enero al 31 de Diciembre del {self.anio_siguiente}")
    

class ESF:
    def __init__(self,clientes,proveedores,activos_circulantes,activos_no_circulantes, pasivos_corto,pasivos_largo,capital_contable):
        self.clientes = clientes
        self.proveedores = proveedores
        self.activos_circulantes = activos_circulantes
        self.activos_no_circulantes = activos_no_circulantes
        self.pasivos_corto = pasivos_corto
        self.pasivos_largo = pasivos_largo
        self.capital_contable = capital_contable
        
    def total_activos_circulante(self):
        return sum(self.activos_circulantes.values()) + self.clientes

    def total_activos_no_circulantes(self):
        return sum(self.activos_no_circulantes.values())
    
    def total_activos(self):
        return self.total_activos_circulante() + self.total_activos_no_circulantes()
    
    def total_pasivos_corto(self):
        return sum(self.pasivos_corto.values()) + self.proveedores

    def total_pasivos_largo(self):
        return sum(self.pasivos_largo.values())
    
    def total_pasivos(self):
        return self.total_pasivos_corto() + self.total_pasivos_largo()
    
    def total_capital(self):
        return sum(self.capital_contable.values())
    
    def suma_pasivo_capital(self):
        return self.total_pasivos() + self.total_capital()


    def mostrar_activos_circulantes(self):
        print("ACTIVOS CIRCULANTES:")
        print(f"  1. Clientes: $ {self.clientes:.2f}")
        for i, (nombre, valor) in enumerate(self.activos_circulantes.items(), start=2):
            print(f"  {i}. {nombre}: $ {valor:.2f}")


    def mostrar_ESF(self,empresa):
        print(f"{empresa.nombre:^10}")
        tabla_esf = {"Activos":["Activos Circulantes:",
                             *list(self.activos_circulantes.keys()),
                             "Total de activo Circulante",
                             "",
                             "Activos No Circulantes:",
                             *list(self.activos_no_circulantes.keys()),
                             "Total de activo No Ciculante"],
                      "":[   "",
                             *ESF.lista_cuentas(self.activos_circulantes),
                             f"$ {self.total_activos_circulante()}",
                             "","",
                             *ESF.lista_cuentas(self.activos_no_circulantes),
                             f"$ {self.total_activos_no_circulantes()}"],
                      "Pasivos":["Pasivos a Corto Plazo",
                             "Proveedores",
                             *list(self.pasivos_corto.keys()),
                             "Total Pasivos Corto Plazo",
                             "",
                             "Pasivos a Largo Plazo",
                             *list(self.pasivos_largo.keys()),
                             "Total Pasivos Largo Plazo",
                             "Total Pasivo", "",
                             "Capital Contable",
                             *list(self.capital_contable.keys()),
                             "Total Capital Contable"],
                      " ":[  "",
                             self.proveedores,
                             *list(self.pasivos_corto.values()),
                             self.total_pasivos_corto(),
                             "", "",
                             *list(self.pasivos_largo.values()),
                             self.total_pasivos_largo(),
                             self.total_pasivos(), "", "",
                             *list(self.capital_contable.values()),
                             self.total_capital()]}
                            
        
        tabla_esf["Activos"].insert(1,"Clientes")
        tabla_esf[""].insert(1, f"$ {self.clientes}")

        tabla_esf = ESF.rellenar(tabla_esf)

        tabla_esf["Activos"].append("Total Activos")
        tabla_esf[""].append(self.total_activos())
        tabla_esf["Pasivos"].append("Suma Pasivo Capital")
        tabla_esf[" "].append(self.suma_pasivo_capital())

        print(tabulate(tabla_esf, headers="keys",tablefmt= "fancy_grid"))
       
    def balance_cuadrado(self):
        if self.total_activos() != self.suma_pasivo_capital():
            print("Su Balance no esta cuadrado, reingrese los datos porfavor")
            cuadrado = False
        else:
            print("Su balance esta cuadrado")
            cuadrado = True
        return cuadrado
    
    @staticmethod
    def rellenar(tabla):
        relleno = (len(tabla['Pasivos']) - len(tabla['Activos'])) +1
        if len(tabla['Activos']) < len(tabla['Pasivos']):
            for i in range(relleno):
                tabla['Activos'].append("")
                tabla[""].append("")
            
            tabla["Pasivos"].append("")
            tabla[" "].append("")

        elif len(tabla['Activos']) > len(tabla['Pasivos']):
            for i in range(relleno):
                tabla["Pasivos"].append("")
                tabla[" "].append("")
            tabla['Activos'].append("")
            tabla[""].append("")

        else:    
            tabla["Pasivos"].append("")
            tabla[" "].append("")
            tabla['Activos'].append("")
            tabla[""].append("")

        return tabla
    
    @staticmethod
    def lista_cuentas(lista):
        resultado = []
        for cuenta in lista.values():
            resultado.append(f"$ {abs(cuenta)}")
        return resultado 


class Producto:
    def __init__(self,nombre="None",precioXsem={'sem1':1,'sem2':1},ventas_plan={'sem1':1,'sem2':1},materiales=[],horas_obra=1,costo_obra={'sem1':1,'sem2':1},inv_inicial=0,inv_final=0):
        self.nombre= nombre
        self.precioXsem = precioXsem
        self.ventas_plan = ventas_plan
        self.materiales = materiales
        self.horas_obra = horas_obra
        self.costo_obra = costo_obra
        self.inv_inicial = inv_inicial
        self.inv_final = inv_final

    def mostrar_producto(self):
        print("=" * 50)
        print(f"Producto: {self.nombre}")
        print("-" * 50)
        
        print("Precios:")
        print(f"  - Primer semestre : {self.precioXsem['sem1']}")
        print(f"  - Segundo semestre: {self.precioXsem['sem2']}")
        print()
        
        print("Ventas planificadas:")
        print(f"  - Primer semestre : {self.ventas_plan['sem1']}")
        print(f"  - Segundo semestre: {self.ventas_plan['sem2']}")
        print()
        
        print("Materiales:")
        for idx, material in enumerate(self.materiales, start=1):
            print(f"  {idx}. {material.nombre}")
        print()
        
        print(f"Horas requeridas para elaboración: {self.horas_obra}")
        print()
        
        print("Costo de mano de obra:")
        print(f"  - Primer semestre : {self.costo_obra['sem1']}")
        print(f"  - Segundo semestre: {self.costo_obra['sem2']}")
        print()
        
        print("Inventarios:")
        print(f"  - Inicial: {self.inv_inicial}")
        print(f"  - Final  : {self.inv_final}")
        print("=" * 50)

    def get_nombre(self):
        return self.nombre

    def get_precioXsem(self):
        return self.precioXsem.values()

    def get_ventas_plan(self):   
        return self.ventas_plan["sem1"]
    
    def get_materiales(self): 
        pass

    def set_nombre(self, valor):
         if  not isinstance(valor,(str)):
            raise TypeError("Tiene que ser texto")
         if valor == "":
              raise ValueError("No puedes dejar el nombre vacio")
         self.nombre = valor

    def set_precioXsem(self, lista):
         for valor in lista.values():
              if not isinstance(valor,(int,float,Decimal)):
                   raise TypeError("Debe ser un numero") 
              if valor <= 0:
                   raise ValueError("No puedes tener un precio menor a 0")
         self.precioXsem = lista
    
    def set_ventas_plan(self,lista):
         for valor in lista.values():
              if not isinstance(valor,(int,float,Decimal)):
                   raise TypeError("Debe ser un numero")
              if valor <= 0:
                   raise ValueError("No puedes tener un precio menor a 0")
         self.ventas_plan = lista
    
    def set_materiales(self,lista):
         for valor in lista:
              if not isinstance(valor, (Material)):
                   raise TypeError("Debe ser de la clase material")
         self.materiales = lista

    def set_horas_obra(self,valor):
         if not isinstance(valor, (str,float, Decimal)):
              raise TypeError("Debe ser un numero")
         if valor <= 0:
              raise ValueError("No pueden ser horas negativas o iguales a cero")
         self.horas_obra = valor

    def set_costo_obra(self, lista):
        for valor in lista.values():
              if not isinstance(valor,(int,float,Decimal)):
                   raise TypeError("Debe ser un numero")
              if valor <= 0:
                   raise ValueError("No puedes tener un precio menor a 0")
        self.costo_obra = lista

    def set_inv_inicial(self,valor):
         if not isinstance(valor,(int,float,Decimal)):
              raise TypeError("Debe ser un numero")
         if valor <= 0:
              raise ValueError("No puedes tener un precio menor a 0")
         self.inv_inicial = valor

    def set_inv_final(self,valor):
         if not isinstance(valor,(int,float,Decimal)):
              raise TypeError("Debe ser un numero")
         if valor <= 0:
              raise ValueError("No puedes tener un precio menor a 0")
         self.inv_final = valor
         
class Material:
    def __init__(self, nombre="None", unidad="None", req_mat=1, inv_inicial=0, inv_final=0, costoXsem={"sem1":0,"sem2":0}):
        self.nombre = nombre
        self.unidad = unidad
        self.req_mat = req_mat  
        self.inv_inicial = inv_inicial 
        self.inv_final = inv_final  
        self.costoXsem = costoXsem  

    def info_material(self):
        print(f"Material:               {self.nombre}")
        print(f"Unidad de medida:      {self.unidad}")
        print(f"Requerimiento:         {self.req_mat}")
        print(f"Inventario inicial S1: {self.inv_inicial}")
        print(f"Inventario final S2:   {self.inv_final}")
        print(f"Costo S1:              ${self.costoXsem['sem1']}")
        print(f"Costo S2:              ${self.costoXsem['sem2']}")

    def validar_cadena(self,valor):
        if not isinstance(valor,(str)):
             raise TypeError("Tiene que ser texto")
        if valor == "":
            raise ValueError("No puedes dejar el nombre vacio")
    
    def validar_numero(self,valor):
        if not isinstance(valor, (int,float,Decimal)):
                raise TypeError("Debe ser un numero")
        if valor <= 0:
                raise ValueError("No puede ser cero o menor")

    def set_nombre(self, valor):
        self.validar_cadena(valor)
        self.nombre = valor
    

    def set_unidad(self, valor):
        self.validar_cadena(valor)
        self.unidad = valor  


    def set_req_mat(self,valor):
        self.validar_numero(valor)
        self.req_mat = valor


    def set_inv_inicial(self, valor):
        if not isinstance(valor, (int,float,Decimal)):
                raise TypeError("Debe ser un numero")
        if valor < 0:
                raise ValueError("No puede ser cero o menor")

        self.inv_inicial = valor


    def set_inv_final(self, valor):
        if not isinstance(valor, (int,float,Decimal)):
                raise TypeError("Debe ser un numero")
        if valor < 0:
                raise ValueError("No puede ser cero o menor")
        self.inv_final = valor

    def set_costoXsem(self, lista):
        for valor in lista.values():
                if not isinstance(valor,(int,float,Decimal)):
                    raise TypeError("Debe ser un numero")
                if valor < 0:
                    raise ValueError("No puede ser cero o menor")
        self.costoXsem = lista

class GastosAyV:
    def __init__(self,depreciacion={},sueldosYsal={},comisiones=0,varios={},intereses={}):
        self.depreciacion = depreciacion
        self.sueldosYsal = sueldosYsal
        self.comisiones = comisiones
        self.varios = varios
        self.intereses = intereses

    def mostrar_gastosAyV(self):
         for periodo, cantidad in self.depreciacion.items():
              print("Depreciacion")
              print(f"{periodo}: {cantidad}")
         for periodo, cantidad in self.sueldosYsal.items():
              print("Sueldos y salarios")
              print(f"{periodo}: {cantidad}")
         print(f"Comisiones: {Decimal(100)*self.comisiones}%")
         for periodo, cantidad in self.varios.items():
              print("Varios")
              print(f"{periodo}: {cantidad}")
         for periodo, cantidad in self.intereses.items():
              print("Intereses")
              print(f"{periodo}: {cantidad}")
        
    def validar_valores(self, valores):
        for cantidad in valores.values():
            if not isinstance(cantidad, (int, float, Decimal)):
                raise TypeError("Debe ser un número")
            if cantidad < 0:
                raise ValueError("No puede ser cero o menor")

    def set_depreciacion(self,valores):
        self.validar_valores(valores)
        self.depreciacion = valores
    
    def set_sueldosYsal(self,valores):
        self.validar_valores(valores)
        self.sueldosYsal = valores
    
    def set_comisiones(self,valor):
        if not isinstance(valor,(int,float,Decimal)):
            raise TypeError("Debe ser un numero")
        if valor < 0:
            raise ValueError("No puede ser cero o menor")
        self.comisiones = valor

    def set_varios(self,valores):
        self.validar_valores(valores) 
        self.varios = valores
            
    def set_intereses(self,valores):
        self.validar_valores(valores) 
        self.intereses = valores

class GIF:
    def __init__(self,depreciacion={},seguros={},mantenimiento={},energeticos={},varios={}):
        self.depreciacion = depreciacion
        self.seguros = seguros
        self.mantenimiento = mantenimiento
        self.energeticos = energeticos
        self.varios = varios

    def mostrar_gif(self):
         for periodo, cantidad in self.depreciacion.items():
              print("Depreciacion")
              print(f"{periodo}: {cantidad}")
         for periodo, cantidad in self.seguros.items():
              print("Seguros")
              print(f"{periodo}: {cantidad}")
         for periodo, cantidad in self.mantenimiento.items():
              print("Mantenimiento")
              print(f"{periodo}: {cantidad}")
         for periodo, cantidad in self.energeticos.items():
              print("Energéticos")
              print(f"{periodo}: {cantidad}")
         for periodo, cantidad in self.varios.items():
              print("Varios")
              print(f"{periodo}: {cantidad}")

    def validar_valores(self, valores):
        for cantidad in valores.values():
            if not isinstance(cantidad, (int, float, Decimal)):
                raise TypeError("Debe ser un número")
            if cantidad < 0:
                raise ValueError("No puede ser cero o menor")

    def set_depreciacion(self,valores):
        self.validar_valores(valores)
        self.depreciacion = valores
    
    def set_seguros(self,valores):
        self.validar_valores(valores)
        self.seguros = valores
    
    def set_mantenimiento(self,valores):
        self.validar_valores(valores)
        self.mantenimiento = valores

    def set_energeticos(self,valores):
        self.validar_valores(valores) 
        self.energeticos = valores
            
    def set_varios(self,valores):
        self.validar_valores(valores)
        self.varios = valores


class Extras:
    def __init__(self, cuentas_extra={}, isr=0, ptu=0, cobrar_clientes=0,
                 cobrar_ventas=0, pagar_prov=0, pagar_comp=0):
        self.cuentas_extra = cuentas_extra
        self.isr = isr
        self.ptu = ptu
        self.cobrar_clientes =cobrar_clientes
        self.cobrar_ventas = cobrar_ventas
        self.pagar_prov = pagar_prov
        self.pagar_comp = pagar_comp

    def mostrar_extras(self):
        for periodo, cantidad in self.cuentas_extra.items():
              print("Adquisiciones")
              print(f"{periodo}: {cantidad}")
        print(f"Porcentaje ISR: {self.isr*Decimal("100")}%")
        print(f"Porcentaje PTU: {self.ptu*Decimal("100")}%")
        print(f"Se cobrará el {self.cobrar_clientes*Decimal("100")}% del saldo de clientes")
        print(f"Se cobrará el {self.cobrar_ventas*Decimal("100")}% de las ventas presupuestadas")
        print(f"Se pagará el {self.pagar_prov*Decimal("100")}% del saldo de proveedores")
        print(f"Se pagará el {self.pagar_comp*Decimal("100")}% de las compras presupuestadas")

    def validar_numero(self,valor):
        if not isinstance(valor, (int,float,Decimal)):
                raise TypeError("Debe ser un numero")
        if valor < 0:
                raise ValueError("No puede ser cero o menor")

    def set_cuentas_extra(self, valor):
         self.cuentas_extra = valor

    def set_isr(self, valores):
        self.validar_numero(valores)
        self.isr = valores

    def set_ptu(self, valores):
        self.validar_numero(valores)
        self.ptu = valores

    def set_cobrar_clientes(self, valores):
        self.validar_numero(valores)
        self.cobrar_clientes = valores

    def set_cobrar_ventas(self, valores):
        self.validar_numero(valores)
        self.cobrar_ventas = valores

    def set_pagar_prov(self, valores):
        self.validar_numero(valores)
        self.pagar_prov = valores

    def set_pagar_comp(self, valores):
        self.validar_numero(valores)
        self.pagar_comp = valores

    def set_isr_a_pagar(self, valores):
        self.isr_a_pagar = valores




class Cedulas:
    def __init__(self, empresa, esf,productos,gastosAyV,gif,extras):
          self.empresa = empresa
          self.esf = esf
          self.productos = productos
          self.gastosAyV = gastosAyV
          self.gif = gif
          self.extras = extras
    @staticmethod
    def importe_venta1(producto):
         return  producto.ventas_plan['sem1'] * producto.precioXsem['sem1']
    @staticmethod
    def importe_venta2(producto):
         return  producto.ventas_plan['sem2'] * producto.precioXsem['sem2']
    @staticmethod
    def importe_total(producto):
         return Cedulas.importe_venta1(producto) + Cedulas.importe_venta2(producto)

    
    def total_ventas(self):
        total_final = 0        
        for producto in self.productos:
                total_final += Cedulas.importe_total(producto)
        return total_final
    

    def divide_productos(self):
        productos_col1 = []
        productos_col2 = []
        productos_col3 = []
        productos_col4 = []       
        total_ventas1 = 0
        total_ventas2 = 0
        total_final = 0        
        for producto in self.productos:
                total_ventas1 += Cedulas.importe_venta1(producto)
                total_ventas2 += Cedulas.importe_venta2(producto)
                total_final += Cedulas.importe_total(producto)
                productos =[f"Producto {producto.nombre}",
                            "Unidades a vender",
                            "Precio de venta",
                            "Importe de venta",
                            ""]
                sem1      =["",
                            producto.ventas_plan['sem1'],
                            producto.precioXsem['sem1'],
                            Cedulas.importe_venta1(producto),
                            ""]
                sem2      =["",
                            producto.ventas_plan['sem2'],
                            producto.precioXsem['sem2'],
                            Cedulas.importe_venta2(producto),
                            ""]
                
                total = ["","","",
                         Cedulas.importe_total(producto),
                         ""]
                productos_col1 += productos
                productos_col2 += sem1
                productos_col3 += sem2
                productos_col4 += total

        productos_col1.append("Total de ventas por semestre")
        productos_col2.append(total_ventas1)
        productos_col3.append(total_ventas2)
        productos_col4.append(total_final)
        return productos_col1,productos_col2,productos_col3,productos_col4
    
    @staticmethod
    def total_unidades(ventas,inventario):
         return ventas + inventario

    @staticmethod
    def unidadesAproducir_sem1(producto,inventario_inicial):
         return Cedulas.total_unidades(producto.ventas_plan['sem1'],producto.inv_inicial) - inventario_inicial

    @staticmethod
    def unidadesAproducir_sem2(producto,inventario_inicial):
         return Cedulas.total_unidades(producto.ventas_plan['sem2'],producto.inv_final) - inventario_inicial

    def productos_produccion(self):
        productos_col1 = []
        productos_col2 = []
        productos_col3 = []
        productos_col4 = []       
        for producto in self.productos:

                productos =[f"Producto {producto.nombre}",
                            "Unidades a vender",
                            "Inventario Final",
                            "Total de Unidades",
                            "Inventario Inicial",
                            "Unidades a Producir",
                            ""]
                sem1      =["",
                            producto.ventas_plan['sem1'],
                            producto.inv_inicial,
                            Cedulas.total_unidades(producto.ventas_plan['sem1'],producto.inv_inicial),
                            producto.inv_inicial,
                            Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial),""]
                sem2      =["",
                            producto.ventas_plan['sem2'],
                            producto.inv_final,
                            Cedulas.total_unidades(producto.ventas_plan['sem2'],producto.inv_final),
                            producto.inv_inicial,
                            Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial),""]
                total     = ["",
                            producto.ventas_plan['sem1'] + producto.ventas_plan['sem2'],
                            producto.inv_final,
                            producto.ventas_plan['sem1'] + producto.ventas_plan['sem2'] + producto.inv_final,
                            producto.inv_inicial,
                            Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial) + Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial)
                            ,""]
                productos_col1 += productos
                productos_col2 += sem1
                productos_col3 += sem2
                productos_col4 += total

        return productos_col1,productos_col2,productos_col3,productos_col4
  
    def entrada_efectivo(self):
         return (self.esf.clientes * self.extras.cobrar_clientes) + (self.total_ventas() * self.extras.cobrar_ventas)

    def saldo_clientes(self):
         return (self.esf.clientes + self.total_ventas()) - self.entrada_efectivo()

    def mostrar_P_ventas(self):
        col1, col2, col3, col4 = self.divide_productos()
        print(f"1. Presupuesto de ventas")
        tabla_PV = {"":col1,
                      "1er.Semestre":col2,
                      "2.do.Semestre":col3,                      
                      f"{self.empresa.anio_siguiente}":col4}
        print(tabulate(tabla_PV, headers="keys",tablefmt= "fancy_grid"))
        
    def mostrar_saldo_clientes(self):
         print("2.Determinación del saldo de Clientes y Flujo de Entradas")
         tabla_SC= {"Descripción":[f"Saldo de clientes 31-Dic-2015{self.empresa.anio_actual}",
                                  f"Ventas {self.empresa.anio_siguiente}",
                                  f"Total de Clientes{self.empresa.anio_siguiente}",
                                  "",
                                  "Entradas de Efectivo:",
                                  f"Por Cobranza del {self.empresa.anio_actual}",
                                  f"Por cobranza del {self.empresa.anio_siguiente}",
                                  "","",
                                  f"Saldo de Clientes del {self.empresa.anio_siguiente}"],
                        "Importe":["","","","","",
                                    self.esf.clientes * self.extras.cobrar_clientes,
                                    self.total_ventas() * self.extras.cobrar_ventas,
                                    "","",""],
                        "Total":[self.esf.clientes,
                                 self.total_ventas(),
                                 self.esf.clientes + self.total_ventas(),
                                 "","","","",
                                 self.entrada_efectivo(),
                                 "",
                                 self.saldo_clientes()]}
         print(tabulate(tabla_SC, headers="keys",tablefmt= "fancy_grid"))

    def mostrar_presupuesto_prod(self):
         col_1, col_2,col_3,col_4=self.productos_produccion()
         print("3. Presupuesto de Producción")
         tabla_Pprod ={"":col_1,
                       "1er. Semestre":col_2,
                       "2do. Semestre":col_3,
                       f"Total {self.empresa.anio_siguiente}": col_4}
         print(tabulate(tabla_Pprod, headers="keys",tablefmt= "fancy_grid"))

    def material_requerido(self):
        descripcion = []
        sem_1 = []
        sem_2 = []
        total = []
        for producto in self.productos:
             descripcion += [f"Producto {producto.nombre}",
                            "Unidades a producir",
                            ""]
             sem_1 += ["",
                      Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial),
                      ""]
             sem_2 += ["",
                      Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial),
                      ""]
             total += ["",
                      Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial) + Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial),
                      ""]
             for material in producto.materiales:
                  descripcion += [material.nombre,
                                  "Requerimiento de material",
                                  f"Total de {material.nombre} requerido"]
                  sem_1 += ["",
                            material.req_mat,
                            Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial) * material.req_mat]
                  sem_2 += ["",
                            material.req_mat,
                            Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial) * material.req_mat]
                  
                  total += ["",
                           material.req_mat,
                           (Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial)*material.req_mat) + (Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial) * material.req_mat)]

        return descripcion,sem_1,sem_2,total
                  
    def Total_req(self):
        requerimientos_acumulados = {}
        for producto in self.productos:
             for material in producto.materiales:
                if material.nombre not in requerimientos_acumulados: 
                        requerimientos_acumulados[material.nombre] = {
                             "sem1":0,
                             "sem2":0,
                             "total":0,
                             "objeto": material
                        }
                sem1_req =  Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial) * material.req_mat
                sem2_req = Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial) * material.req_mat
                requerimientos_acumulados[material.nombre]["sem1"] += sem1_req
                requerimientos_acumulados[material.nombre]["sem2"] += sem2_req
                requerimientos_acumulados[material.nombre]["total"] += sem1_req + sem2_req
                  
        tabla = []
        tabla = [[nombre, datos["sem1"], datos["sem2"], datos["total"], datos["objeto"]] 
                    for nombre, datos in requerimientos_acumulados.items()]
        tabla_Alt = [[nombre, datos["sem1"], datos["sem2"], datos["total"]] 
                    for nombre, datos in requerimientos_acumulados.items()]
        return tabla, tabla_Alt


    def mostrar_req_mat(self):
        col_1, col_2,col_3,col_4=self.material_requerido()
        print("4. Presupuesto de Requerimiento de Materiales")
        tabla_req_mat= {"":col_1,
                        "1.Semestre":col_2,
                        "2do.Semestre":col_3,
                        f"Total {self.empresa.anio_siguiente}":col_4}
        tabla_tq, tabla_tqA = self.Total_req()
        print(tabulate(tabla_req_mat, headers="keys",tablefmt= "fancy_grid"))
        print(tabulate(tabla_tqA, headers=["Total de requerimientos", "", "  "], tablefmt="grid"))
        

    def encontrar_compra_mat(self):
            datos, tabla_tqA = self.Total_req()
            compras_Totales1 = 0
            compras_Totales2 = 0
            compras_TotalesA = 0
            col_1 = []
            col_2 = []
            col_3 = []
            col_4 = []
            for fila in datos:
                    req_sem1 = fila[1]
                    req_sem2 = fila[2]
                    req_total = fila[3]
                    material = fila[4]
                    material_total1 = req_sem1 + material.inv_inicial - material.inv_inicial
                    material_total2 = req_sem2 + material.inv_final - material.inv_inicial
                    total_materiales = (req_sem1 + material.inv_final) + (req_sem2 + material.inv_inicial)
                    compra_total = (material_total1 * material.costoXsem['sem1']) + (material_total2 * material.costoXsem['sem2'])
                    col_1 += [material.nombre,
                                "Requerimiento de materiales",
                                "Inventario Final",
                                "Total de Materiales",
                                "Inventario Inicial",
                                "Material a Comprar",
                                "Precio de Compra",
                                f"Total de {material.nombre} en $",
                                ""]
                    col_2 +=["",
                            req_sem1,
                            material.inv_inicial,
                            req_sem1 + material.inv_inicial,
                            material.inv_inicial,
                            material_total1,
                            material.costoXsem['sem1'],
                            material_total1 * material.costoXsem['sem1'],""]
                    
                    col_3 +=["",
                            req_sem2,
                            material.inv_final,
                            req_sem2 + material.inv_final,
                            material.inv_inicial,
                            material_total2,
                            material.costoXsem['sem2'],
                            material_total2 * material.costoXsem['sem2'],""]
                    col_4 += ["",
                             req_total,
                            material.inv_final,
                            total_materiales,
                            material.inv_inicial,
                            total_materiales + req_sem1 + material.inv_inicial,
                            "",
                            compra_total,""]
                    
                    compras_Totales1 += material_total1 * material.costoXsem['sem1']
                    compras_Totales2 += material_total2 * material.costoXsem['sem2']
                    compras_TotalesA += compra_total
            col_1.append("Compras totales:")
            col_2.append(compras_Totales1)
            col_3.append(compras_Totales2)
            col_4.append(compras_TotalesA)

            return col_1, col_2, col_3, col_4
    
    def suma_compra_mat(self):
            datos, tabla_tqA = self.Total_req()
            compras_Totales1 = 0
            compras_Totales2 = 0
            compras_TotalesA = 0

            for fila in datos:
                    req_sem1 = fila[1]
                    req_sem2 = fila[2]
                    material = fila[4]
                    material_total1 = req_sem1 + material.inv_inicial - material.inv_inicial
                    material_total2 = req_sem2 + material.inv_final - material.inv_inicial
                    compra_total = (material_total1 * material.costoXsem['sem1']) + (material_total2 * material.costoXsem['sem2'])

                    compras_TotalesA += compra_total

            return compras_TotalesA

    def mostrar_compra_mat(self):
         print("5. Presupuesto de Compra de Mateirles")
         col_1, col_2, col_3, col_4 = self.encontrar_compra_mat()
         tabla_cm = {"":col_1,
                     "1er.Semestre": col_2,
                     "2de.Semestre":col_3,
                     f"Total {self.empresa.anio_siguiente}":col_4} 
         print(tabulate(tabla_cm, headers="keys",tablefmt= "fancy_grid"))

    def mostrar_saldo_proveedores(self):
         compra_total = self.suma_compra_mat()
         sal_total =(self.esf.proveedores * self.extras.pagar_prov)+ (compra_total * self.extras.pagar_comp) 
         print("6.Determinación de saldo de Proveedores y Flujo de Salidas")
         tabla_SP= {"Descripción":[f"Saldo de Proveedores 31-Dic-{self.empresa.anio_actual}",
                                  f"Compras {self.empresa.anio_siguiente}",
                                  f"Total de Proveedores {self.empresa.anio_siguiente}",
                                  "",
                                  "Salidas de Efectivo:",
                                  f"Por Proveedores del {self.empresa.anio_actual}",
                                  f"Por Proveedores del {self.empresa.anio_siguiente}",
                                  f"Total de Salidas {self.empresa.anio_siguiente}","",
                                  f"Saldo de Proveedores del {self.empresa.anio_siguiente}"],
                        "Importe":["","","","","",
                                    self.esf.proveedores * self.extras.pagar_prov,
                                    compra_total * self.extras.pagar_comp,
                                    "","",""],
                        "Total":[self.esf.proveedores,
                                 compra_total,
                                 self.esf.proveedores + compra_total,
                                 "","","","",
                                  (compra_total * self.extras.pagar_comp)+(self.esf.proveedores * self.extras.pagar_prov),
                                 "",
                                 (self.esf.proveedores + compra_total)-sal_total]}
         print(tabulate(tabla_SP, headers="keys",tablefmt= "fancy_grid"))
    

    def obtener_MOD(self):
         col_1 =[]
         col_2 =[]
         col_3 =[]
         col_4 =[]
         horas1 = 0
         horas2 = 0
         horaTotal = 0
         horas_acum1 = 0
         horas_acum2 = 0
         horas_acumTotal = 0
         mod1= 0
         mod2 = 0
         modTotal = 0
         mod_acum1= 0
         mod_acum2= 0
         mod_acumTotal = 0
         for producto in self.productos:
                horas1 = Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial)*producto.horas_obra
                horas2 = Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial)*producto.horas_obra
                horaTotal = horas1 + horas2
                mod1 = horas1 * producto.costo_obra["sem1"]
                mod2 = horas2 * producto.costo_obra["sem2"]
                modTotal =mod1 + mod2
                col_1 +=[producto.nombre,
                       "Unidades a producir",
                       "Horas requeridas por unidades",
                       "Total de horas requeridas",
                       "Cuota por hora",
                       "Importe de M.O.D.",""]
                col_2 +=["",
                        Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial),
                        producto.horas_obra,
                        horas1,
                        producto.costo_obra["sem1"],
                        mod1,""]
                col_3 +=["",Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial),
                         producto.horas_obra,
                         horas2,
                         producto.costo_obra["sem2"],
                         mod2,""]
                col_4 +=["",Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial) + Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial),
                         producto.horas_obra,
                         horaTotal,
                         "",
                         modTotal,""]
                horas_acum1 += horas1
                horas_acum2 += horas2
                horas_acumTotal += horaTotal
                mod_acum1+= mod1
                mod_acum2+= mod2
                mod_acumTotal+= modTotal
         col_1.append("Total de horas requeridas por semestre")
         col_2.append(horas_acum1)
         col_3.append(horas_acum2)
         col_4.append(horas_acumTotal)
         col_1.append("Total de M.O.D. por semestre")
         col_2.append(mod_acum1)
         col_3.append(mod_acum2)
         col_4.append(mod_acumTotal)
         return col_1,col_2,col_3,col_4
        
    def mostrar_MOD(self):
         col_1,col_2,col_3,col_4 = self.obtener_MOD()
         print("7.Presupuesto de Mano de Obra Directa")
         tabla_MOD ={"":col_1,
                    "1er.Semestre":col_2,
                    "2do.Semestre":col_3,
                    f"Total {self.empresa.anio_siguiente}":col_4}
         print(tabulate(tabla_MOD, headers="keys",tablefmt= "fancy_grid"))

    def horas_req(self):
         horas1 = 0
         horas2 = 0
         horaTotal = 0
         horas_acumTotal = 0
         for producto in self.productos:
                horas1 = Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial)*producto.horas_obra
                horas2 = Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial)*producto.horas_obra
                horaTotal = horas1 + horas2
                horas_acumTotal += horaTotal
         return horas_acumTotal
    
         
    def AnualoSemestral(self):
            col_2 = []
            col_3 = []
            col_4 = []
            sem_1 = Decimal(0)
            sem_2 = Decimal(0)
            if "Anuales" in self.gif.depreciacion:
                dep = self.gif.depreciacion["Anuales"]
                col_2 += [dep / Decimal(2)]
                col_3 += [dep / Decimal(2)]
                col_4 += [dep]
                sem_1 += dep / Decimal(2)
                sem_2 += dep / Decimal(2)
            else:
                sem1_val = self.gif.depreciacion["Primer semestre"]
                sem2_val = self.gif.depreciacion["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.seguros:
                seg = self.gif.seguros["Anuales"]
                col_2 += [seg / Decimal(2)]
                col_3 += [seg / Decimal(2)]
                col_4 += [seg]
                sem_1 += seg / Decimal(2)
                sem_2 += seg / Decimal(2)
            else:
                sem1_val = self.gif.seguros["Primer semestre"]
                sem2_val = self.gif.seguros["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.mantenimiento:
                man = self.gif.mantenimiento["Anuales"]
                col_2 += [man / Decimal(2)]
                col_3 += [man / Decimal(2)]
                col_4 += [man]
                sem_1 += man / Decimal(2)
                sem_2 += man / Decimal(2)
            else:
                sem1_val = self.gif.mantenimiento["Primer semestre"]
                sem2_val = self.gif.mantenimiento["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.energeticos:
                ener = self.gif.energeticos["Anuales"]
                col_2 += [ener / Decimal(2)]
                col_3 += [ener / Decimal(2)]
                col_4 += [ener]
                sem_1 += ener / Decimal(2)
                sem_2 += ener / Decimal(2)
            else:
                sem1_val = self.gif.energeticos["Primer semestre"]
                sem2_val = self.gif.energeticos["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.varios:
                var = self.gif.varios["Anuales"]
                col_2 += [var / Decimal(2)]
                col_3 += [var / Decimal(2)]
                col_4 += [var]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gif.varios["Primer semestre"]
                sem2_val = self.gif.varios["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val
         
            col_2.append(sem_1)
            col_3.append(sem_2)
            col_4.append(sem_1 + sem_2)
            suma_total = sem_1 + sem_2
            return col_2, col_3, col_4, suma_total
    def mostrar_GIF(self):
         col_2, col_3, col_4, suma_total = self.AnualoSemestral() 
         print("8.Presupuesto de Gastos Indirectos de Fabricación")
         tabla_gif ={"":["Depreciacion",
                         "Seguros",
                         "Mantenimiento",
                         "Energeticos",
                         "Varios",
                         "Total G.I.F. por semestre"],
                     "1er.Semestre":col_2,
                     "2do.Semestre":col_3,
                     f"Total {self.empresa.anio_siguiente}":col_4}  
         horas_req = self.horas_req()
         print(tabulate(tabla_gif, headers="keys",tablefmt= "fancy_grid"))
         print(f"Total de G.I.F.           ${suma_total}")
         print(f"Total horas M.O.D. Anual   {horas_req}")
         print(f"Costo por Hora de G.I.F.  ${suma_total/horas_req}")


    def ventas_proy(self):    
            total_ventas1 = 0
            total_ventas2 = 0
            total_final = 0        
            for producto in self.productos:
                    total_ventas1 += Cedulas.importe_venta1(producto)
                    total_ventas2 += Cedulas.importe_venta2(producto)
                    total_final += Cedulas.importe_total(producto)
            return total_ventas1, total_ventas2, total_final

    def AnualoSemestral2(self):
            col_2 = []
            col_3 = []
            col_4 = []
            sem_1 = Decimal(0)
            sem_2 = Decimal(0)
            if "Anuales" in self.gastosAyV.depreciacion:
                dep = self.gastosAyV.depreciacion["Anuales"]
                col_2 += [dep / Decimal(2)]
                col_3 += [dep / Decimal(2)]
                col_4 += [dep]
                sem_1 += dep / Decimal(2)
                sem_2 += dep / Decimal(2)
            else:
                sem1_val = self.gastosAyV.depreciacion["Primer semestre"]
                sem2_val = self.gastosAyV.depreciacion["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gastosAyV.sueldosYsal:
                seg = self.gastosAyV.sueldosYsal["Anuales"]
                col_2 += [seg / Decimal(2)]
                col_3 += [seg / Decimal(2)]
                col_4 += [seg]
                sem_1 += seg / Decimal(2)
                sem_2 += seg / Decimal(2)
            else:
                sem1_val = self.gastosAyV.sueldosYsal["Primer semestre"]
                sem2_val = self.gastosAyV.sueldosYsal["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val

            total_ventas1, total_ventas2, total_final = self.ventas_proy()
            sem1_val = total_ventas1 * self.gastosAyV.comisiones
            sem2_val = total_ventas2 * self.gastosAyV.comisiones 
            col_2 += [sem1_val]
            col_3 += [sem2_val]
            col_4 += [sem1_val + sem2_val]
            sem_1 += sem1_val
            sem_2 += sem2_val

            if "Anuales" in self.gastosAyV.varios:
                var = self.gastosAyV.varios["Anuales"]
                col_2 += [var / Decimal(2)]
                col_3 += [var / Decimal(2)]
                col_4 += [var]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gastosAyV.varios["Primer semestre"]
                sem2_val = self.gastosAyV.varios["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val
            
            if "Anuales" in self.gastosAyV.intereses:
                var = self.gastosAyV.intereses["Anuales"]
                col_2 += [var / Decimal(2)]
                col_3 += [var / Decimal(2)]
                col_4 += [var]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gastosAyV.intereses["Primer semestre"]
                sem2_val = self.gastosAyV.intereses["Segundo semestre"]
                col_2 += [sem1_val]
                col_3 += [sem2_val]
                col_4 += [sem1_val + sem2_val]
                sem_1 += sem1_val
                sem_2 += sem2_val
         
            col_2.append(sem_1)
            col_3.append(sem_2)
            col_4.append(sem_1 + sem_2)
            return col_2, col_3, col_4


    def mostrar_GDO(self):
         col_2, col_3, col_4 = self. AnualoSemestral2()
         print("9.Presupuesto de Operación")
         tabla_gfo = {"":["Depreciacion",
                         "Sueldos y Salarios",
                         "Comisiones",
                         "Varios",
                         "Intereses del Prestamo",
                         "Total de Gastos de Operacion"],
                     "1er.Semestre":col_2,
                     "2do.Semestre":col_3,
                     f"Total {self.empresa.anio_siguiente}":col_4}
         print(tabulate(tabla_gfo, headers="keys",tablefmt= "fancy_grid"))

    def hora_gif(self):
            sem_1 = Decimal(0)
            sem_2 = Decimal(0)
            if "Anuales" in self.gif.depreciacion:
                dep = self.gif.depreciacion["Anuales"]
                sem_1 += dep / Decimal(2)
                sem_2 += dep / Decimal(2)
            else:
                sem1_val = self.gif.depreciacion["Primer semestre"]
                sem2_val = self.gif.depreciacion["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.seguros:
                seg = self.gif.seguros["Anuales"]
                sem_1 += seg / Decimal(2)
                sem_2 += seg / Decimal(2)
            else:
                sem1_val = self.gif.seguros["Primer semestre"]
                sem2_val = self.gif.seguros["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.mantenimiento:
                man = self.gif.mantenimiento["Anuales"]
                sem_1 += man / Decimal(2)
                sem_2 += man / Decimal(2)
            else:
                sem1_val = self.gif.mantenimiento["Primer semestre"]
                sem2_val = self.gif.mantenimiento["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.energeticos:
                ener = self.gif.energeticos["Anuales"]
                sem_1 += ener / Decimal(2)
                sem_2 += ener / Decimal(2)
            else:
                sem1_val = self.gif.energeticos["Primer semestre"]
                sem2_val = self.gif.energeticos["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.varios:
                var = self.gif.varios["Anuales"]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gif.varios["Primer semestre"]
                sem2_val = self.gif.varios["Segundo semestre"]

                sem_1 += sem1_val
                sem_2 += sem2_val

            suma_total = sem_1 + sem_2
            horas = self.horas_req()
            gif_horas = suma_total/horas
            # gif_horas = gif_horas.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
            return gif_horas


    def mostrar_CUPT(self):
         print("10.Determinacion del Costo Unitario de Productos Terminados")
         hora_gif = self.hora_gif()
         for producto in self.productos:
              print(f"{producto.nombre:^10}")
              col_1 = []
              col_2 = []
              col_3 = []
              col_4 = []
              costo_unitario = 0
              for material in producto.materiales:
                    col_1 += [material.nombre]
                    col_2 += [material.costoXsem["sem2"]]
                    col_3 += [material.req_mat]
                    col_4 += [material.costoXsem["sem2"]*material.req_mat]
                    costo_unitario += material.costoXsem["sem2"]*material.req_mat
              costo_unitario += (producto.costo_obra["sem2"]*producto.horas_obra) + producto.horas_obra*hora_gif
              col_1 += ["Mano de Obra",
                        "Gastos Indirectos de Fabricación",
                        "Costo Unitario"]
              col_2 += [producto.costo_obra["sem2"],
                        hora_gif,""]
              col_3 += [producto.horas_obra,
                        producto.horas_obra,""]
              col_4 += [producto.costo_obra["sem2"]*producto.horas_obra,
                        producto.horas_obra*hora_gif,
                        costo_unitario]
              tabla_CPT= {"Descripción":col_1,
                          "Costo": col_2,
                          "Cantidad": col_3,
                          "Costo Unitario":col_4}
              print(tabulate(tabla_CPT, headers="keys",tablefmt= "fancy_grid"))

    def costos_unitarios(self):
         hora_gif = self.hora_gif()
         lista_costos = []
         for producto in self.productos:
              costo_unitario = 0
              for material in producto.materiales:
                    costo_unitario += material.costoXsem["sem2"]*material.req_mat              
              costo_unitario += (producto.costo_obra["sem2"]*producto.horas_obra) + producto.horas_obra*hora_gif
              lista_costos.append(f"{costo_unitario:.4f}")
         return lista_costos

    def mostrar_inv_final(self):
         print("11.Valuación de Inventarios Finales")
         print("Inventario final de Materiales")
         col_1 = []
         col_2 = []
         col_3 = []
         col_4 = []
         costo_total = 0
         for material in self.productos[0].materiales:
                col_1 += [material.nombre]
                col_2 += [material.inv_final]
                col_3 += [material.costoXsem["sem2"]]
                col_4 += [material.inv_final*material.costoXsem["sem2"]]
                costo_total += material.inv_final*material.costoXsem["sem2"]
         col_1 += ["Invetario Final de Materiales"]
         col_4 += [costo_total] 
         tabla_mat = {"Descripción":col_1,
                      "Unidades":col_2,
                      "Costo Unitario":col_3,
                      "Costo Total": col_4}
         print(tabulate(tabla_mat, headers="keys",tablefmt= "fancy_grid"))
         col_1 = []
         col_2 = []
         col_3 = []
         col_4 = []
         costo_total = Decimal(0)
         lista_costos = self.costos_unitarios() 
         print("Inventario Final de Producto Terminado")
         for index, producto in enumerate(self.productos):
                num_sec = Decimal(lista_costos[index])
                col_1 += [producto.nombre]
                col_2 += [producto.inv_final]
                col_3 += [lista_costos[index]]
                col_4 += [producto.inv_final*num_sec]
                costo_total += producto.inv_final*num_sec
                
         col_1 += ["Invetario Final de Producto Terminado"]
         col_4 += [costo_total] 
         tabla_prod = {"Descripción":col_1,
                      "Unidades":col_2,
                      "Costo Unitario":col_3,
                      "Costo Total": col_4}
         print(tabulate(tabla_prod, headers="keys", tablefmt="rounded_grid",floatfmt=".2f"))

    def averiguar_cuenta_pasivo_corto(self, cuenta):
        print(f"Ingrese la cuenta que pertenece al {cuenta}:")

        # Obtener las cuentas desde self.esf
        cuentas = [("Proveedores", self.esf.proveedores)] + list(self.esf.pasivos_corto.items())

        # Mostrar cuentas enumeradas
        for i, (nombre, valor) in enumerate(cuentas, start=1):
            print(f"  {i}. {nombre}: $ {valor:.2f}")

        # Pedir selección
        try:
            opcion = int(input("Opción: "))
            if 1 <= opcion <= len(cuentas):
                nombre, valor = cuentas[opcion - 1]
                print(f"\nHas seleccionado: {nombre} con un valor de $ {valor:.2f}")
                return valor
            else:
                print("Opción fuera de rango.")
                return None
        except ValueError:
            print("Por favor ingresa un número válido.")
            return None

        
    def averiguar_cuenta(self,cuenta):
        print(f"Ingrese la cuenta que pertenece al {cuenta}:")
        
        # Crear lista de cuentas: [(nombre, valor)]
        cuentas = [("Clientes", self.esf.clientes)] + list(self.esf.activos_circulantes.items())
        
        # Mostrar enumeradas
        for i, (nombre, valor) in enumerate(cuentas, start=1):
            print(f"  {i}. {nombre}: $ {valor:.2f}")
        
        # Pedir selección
        try:
            opcion = int(input("Opción: "))
            if 1 <= opcion <= len(cuentas):
                nombre, valor = cuentas[opcion - 1]
                print(f"\nHas seleccionado: {nombre} con un valor de $ {valor:.2f}")
                return valor  # <- Devuelve directamente el value (Decimal)
            else:
                print("Opción fuera de rango.")
                return None
        except ValueError:
            print("Por favor ingresa un número válido.")
            return None

    def inv_final_mat(self):
                costo_total = 0
                for material in self.productos[0].materiales:
                        costo_total += material.inv_final*material.costoXsem["sem2"]
                return costo_total

    def mod_acum_total(self):
            horas_acum1 = 0
            horas_acum2 = 0
            horas_acumTotal = 0
            mod1= 0
            mod2 = 0
            modTotal = 0
            mod_acum1= 0
            mod_acum2= 0
            mod_acumTotal = 0
            for producto in self.productos:
                    horas1 = Cedulas.unidadesAproducir_sem1(producto, producto.inv_inicial)*producto.horas_obra
                    horas2 = Cedulas.unidadesAproducir_sem2(producto, producto.inv_inicial)*producto.horas_obra
                    horaTotal = horas1 + horas2
                    mod1 = horas1 * producto.costo_obra["sem1"]
                    mod2 = horas2 * producto.costo_obra["sem2"]
                    modTotal =mod1 + mod2

                    horas_acum1 += horas1
                    horas_acum2 += horas2
                    horas_acumTotal += horaTotal
                    mod_acum1+= mod1
                    mod_acum2+= mod2
                    mod_acumTotal+= modTotal
            return mod_acumTotal
            

    def prod_terminado(self):
         costo_total = Decimal(0)
         lista_costos = self.costos_unitarios() 
         for index, producto in enumerate(self.productos):
                num_sec = Decimal(lista_costos[index])
                costo_total += producto.inv_final*num_sec
         return costo_total

    def consigue_ventas(self):
        total_final = 0        
        for producto in self.productos:
                total_final += Cedulas.importe_total(producto)
        return total_final


    def consigue_GdO(self):
            sem_1 = Decimal(0)
            sem_2 = Decimal(0)
            if "Anuales" in self.gastosAyV.depreciacion:
                dep = self.gastosAyV.depreciacion["Anuales"]
                sem_1 += dep / Decimal(2)
                sem_2 += dep / Decimal(2)
            else:
                sem1_val = self.gastosAyV.depreciacion["Primer semestre"]
                sem2_val = self.gastosAyV.depreciacion["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gastosAyV.sueldosYsal:
                seg = self.gastosAyV.sueldosYsal["Anuales"]
                sem_1 += seg / Decimal(2)
                sem_2 += seg / Decimal(2)
            else:
                sem1_val = self.gastosAyV.sueldosYsal["Primer semestre"]
                sem2_val = self.gastosAyV.sueldosYsal["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            total_ventas1, total_ventas2, total_final = self.ventas_proy()
            sem1_val = total_ventas1 * self.gastosAyV.comisiones
            sem2_val = total_ventas2 * self.gastosAyV.comisiones 
            sem_1 += sem1_val
            sem_2 += sem2_val

            if "Anuales" in self.gastosAyV.varios:
                var = self.gastosAyV.varios["Anuales"]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gastosAyV.varios["Primer semestre"]
                sem2_val = self.gastosAyV.varios["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val
            
            if "Anuales" in self.gastosAyV.intereses:
                var = self.gastosAyV.intereses["Anuales"]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gastosAyV.intereses["Primer semestre"]
                sem2_val = self.gastosAyV.intereses["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val
         
            total = sem_1 + sem_2
            return total
    
    def encontrar_GIF(self):
            sem_1 = Decimal(0)
            sem_2 = Decimal(0)
            if "Anuales" in self.gif.seguros:
                seg = self.gif.seguros["Anuales"]
                sem_1 += seg / Decimal(2)
                sem_2 += seg / Decimal(2)
            else:
                sem1_val = self.gif.seguros["Primer semestre"]
                sem2_val = self.gif.seguros["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.mantenimiento:
                man = self.gif.mantenimiento["Anuales"]
                sem_1 += man / Decimal(2)
                sem_2 += man / Decimal(2)
            else:
                sem1_val = self.gif.mantenimiento["Primer semestre"]
                sem2_val = self.gif.mantenimiento["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.energeticos:
                ener = self.gif.energeticos["Anuales"]
                col_2 += [ener / Decimal(2)]
                col_3 += [ener / Decimal(2)]
                col_4 += [ener]
                sem_1 += ener / Decimal(2)
                sem_2 += ener / Decimal(2)
            else:
                sem1_val = self.gif.energeticos["Primer semestre"]
                sem2_val = self.gif.energeticos["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            if "Anuales" in self.gif.varios:
                var = self.gif.varios["Anuales"]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gif.varios["Primer semestre"]
                sem2_val = self.gif.varios["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val
            suma_total = sem_1 + sem_2
            return suma_total
    
    def encontrar_GDO(self):
            sem_1 = Decimal(0)
            sem_2 = Decimal(0)
            if "Anuales" in self.gastosAyV.sueldosYsal:
                seg = self.gastosAyV.sueldosYsal["Anuales"]
                sem_1 += seg / Decimal(2)
                sem_2 += seg / Decimal(2)
            else:
                sem1_val = self.gastosAyV.sueldosYsal["Primer semestre"]
                sem2_val = self.gastosAyV.sueldosYsal["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val

            total_ventas1, total_ventas2, total_final = self.ventas_proy()
            sem1_val = total_ventas1 * self.gastosAyV.comisiones
            sem2_val = total_ventas2 * self.gastosAyV.comisiones 
            sem_1 += sem1_val
            sem_2 += sem2_val

            if "Anuales" in self.gastosAyV.varios:
                var = self.gastosAyV.varios["Anuales"]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gastosAyV.varios["Primer semestre"]
                sem2_val = self.gastosAyV.varios["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val
            
            if "Anuales" in self.gastosAyV.intereses:
                var = self.gastosAyV.intereses["Anuales"]
                sem_1 += var / Decimal(2)
                sem_2 += var / Decimal(2)
            else:
                sem1_val = self.gastosAyV.intereses["Primer semestre"]
                sem2_val = self.gastosAyV.intereses["Segundo semestre"]
                sem_1 += sem1_val
                sem_2 += sem2_val
         
            total = sem_1 + sem_2
            return total
    
    def titulo(self):
        print("=" * 80)
        print(f"{self.empresa.nombre.upper():^80}")
        print(f"{f'Presupuesto del 1 de Enero al 31 de Diciembre del {self.empresa.anio_siguiente}':^80}")
        print("=" * 80)



    def  mostrar_PresupuestoFinanciero(self):
            cuenta_ini_mat = self.averiguar_cuenta("Saldo Inicial de materiales")
            cuenta_terprod = self.averiguar_cuenta("Inventario Inicial de Productos Terminados")
            comp_total = self.suma_compra_mat()
            invf_mat = self.inv_final_mat()
            mod_acumTotal = self.mod_acum_total()
            col_2, col_3, col_4, suma_total = self.AnualoSemestral() 
            inv_prod = self.prod_terminado()
            mat_disponible = cuenta_ini_mat + comp_total
            mat_utilizado = mat_disponible - invf_mat
            costo_produccion = mat_utilizado + mod_acumTotal + suma_total
            total_disp =costo_produccion + cuenta_terprod
            costo_ventas = total_disp - inv_prod
            self.titulo()
            print("Estado de Costo de Produccion y Ventas")
            tabla_CdPV ={"":["Saldo Inicial de Materiales",
                             "Compras de Materiales",
                             "Material Disponible",
                             "Inventario Final de Materiales",
                             "Materiales Utilizados",
                             "Mano de Obra Directa",
                             "Gastos de Fabricacion Indirectos",
                             "Costo de Produccion",
                             "Inventario Inicial de Productos Terminados",
                             "Total de Produccion Disponible",
                             "Inventario Final de Productos Terminados",
                             "Costo de Ventas"],
                         " ":[ cuenta_ini_mat,
                              comp_total,
                              mat_disponible,
                               invf_mat,
                                mat_utilizado,
                                mod_acumTotal,
                                suma_total,
                                  costo_produccion,
                                  cuenta_terprod,
                                  total_disp,
                                  inv_prod,
                                  costo_ventas]}
            print(tabulate(tabla_CdPV, headers="keys", tablefmt="rounded_grid",floatfmt=".2f"))
            ventas = self.consigue_ventas()
            gastos_operacion = self.consigue_GdO()
            utilidad_bruta = ventas - costo_ventas
            utilidad_operacion = utilidad_bruta - gastos_operacion
            Isr = utilidad_operacion * self.extras.isr
            Ptu = utilidad_operacion * self.extras.ptu
            utilidad_neta = utilidad_operacion - Isr - Ptu
            self.titulo()
            print("Estado de Resultados")
            tabla_EdR ={"":["Ventas",
                            "Costo de Ventas",
                            "Utilidad Bruta",
                            "Gastos de Operación",
                            "Utilidad de Operación",
                            "ISR",
                            "PUT",
                            "Utilidad Neta"],
                        " ":[ventas,
                             costo_ventas,
                             utilidad_bruta,
                             gastos_operacion,
                             utilidad_operacion,
                             Isr,
                             Ptu,
                             utilidad_neta]}
            print(tabulate(tabla_EdR, headers="keys", tablefmt="rounded_grid",floatfmt=".2f"))
            compra_total = self.suma_compra_mat()
            saldo_inicial = self.averiguar_cuenta("Saldo Inicial de efectivo")
            saldo_ISR = self.averiguar_cuenta_pasivo_corto("ISR Por Pagar")
            cobranza_ant =self.esf.clientes * self.extras.cobrar_clientes
            cobranza_nuevo = self.total_ventas() * self.extras.cobrar_ventas
            proveedores_ant = self.esf.proveedores * self.extras.pagar_prov
            proveedores_nuevo =  compra_total * self.extras.pagar_comp
            pago_gif = self.encontrar_GIF()
            pago_gdo = self.encontrar_GDO()
            lista_cuentas_nombres = list(self.extras.cuentas_extra.keys())
            lista_cuentas_valores = list(self.extras.cuentas_extra.values())
            lista_suma = sum(lista_cuentas_valores)
            Total_entradas = cobranza_nuevo + cobranza_ant
            Efectivo_disponible = Total_entradas + saldo_inicial
            total_salidas = proveedores_ant + proveedores_nuevo +mod_acumTotal + pago_gif + pago_gdo + lista_suma + saldo_ISR + Isr
            Flujo_efectivo = Efectivo_disponible - total_salidas
            self.titulo()
            print(self.empresa.anio_siguiente)
            print(self.empresa.anio_actual)
            print("Estado de Flujo de Efectivo")
            tabla_Efe ={"":["Saldo Inicial de Efectivo",
                            "Entradas:",
                            f"Cobranza {self.empresa.anio_siguiente}",
                            f"Cobranza {self.empresa.anio_actual}",
                            "Total de Entradas",
                            "Efectivo Disponible",
                            "Salidas:",
                            f"Proveedores {self.empresa.anio_siguiente}",
                            f"Proveedores {self.empresa.anio_actual}",
                            "Pago de mano de Obra Directa",
                            "Pago de Gastos Indirectos de Fabricación",
                            "Pago de Gastos de Operación",
                            *lista_cuentas_nombres,
                            f"Pago de ISR {self.empresa.anio_actual}",
                            f"Pago de ISR {self.empresa.anio_siguiente}","",
                            "Total de Salidas",
                            "Flujo de Efectivo Actual"],
                        " ":["","",
                             cobranza_nuevo,
                             cobranza_ant,
                             "","","",
                             proveedores_nuevo,
                             proveedores_ant,
                             mod_acumTotal,
                             pago_gif,
                             pago_gdo,
                             *lista_cuentas_valores,
                             saldo_ISR,
                             Isr],
                        "   ":[saldo_inicial,"","","",
                               Total_entradas,
                               Efectivo_disponible,"","","","","","","","","","",
                               total_salidas,
                               Flujo_efectivo]}
            print(tabulate(tabla_Efe, headers="keys", tablefmt="rounded_grid",floatfmt=".2f"))
            dep_acum = -(self.gastosAyV.depreciacion["Anuales"] + self.gif.depreciacion["Anuales"]) + self.esf.activos_no_circulantes['Depreciación Acumulada'] 
            planta_equipo = self.esf.activos_no_circulantes['Planta y Equipo'] + self.extras.cuentas_extra['Planta y Equipo']
            total_activo_circulante = Flujo_efectivo + self.saldo_clientes()+self.esf.activos_circulantes['Deudores Diversos']+self.esf.activos_circulantes['Funcionarios y Empleados']+invf_mat+inv_prod
            total_activo_nocirculante = self.esf.activos_no_circulantes['Terreno']+planta_equipo+dep_acum
            activo_total = total_activo_circulante + total_activo_nocirculante
            total_corto_plazo = proveedores_nuevo+self.esf.pasivos_corto['Documentos por Pagar']+Ptu
            total_largo_plazo = self.esf.pasivos_largo['Préstamos Bancarios']
            total_pasivo = total_largo_plazo + total_corto_plazo
            capital =  self.esf.capital_contable['Capital Contribuido']+self.esf.capital_contable['Capital Ganado']+utilidad_neta
            pasivo_capital = total_pasivo + capital
            self.titulo()
            print("Balance General")
            tabla_bl = {"":["Activo",
                            "Circulante",
                            "Efectivo",
                            "Clientes",
                            "Deudores Diversos",
                            "Funcionarios y Empleados",
                            "Inventario de Materiales",
                            "Inventario de Producto Terminado",
                            "Total de Activos Circulantes",
                            "",
                            "No Circulante",
                            "Terreno",
                            "Planta y Equipo",
                            "Depreciacion Acumulada",
                            "Total Activos no Circulante",
                            "",
                            "Activo Total",
                            "",
                            "Pasivo",
                            "Corto Plazo",
                            "Proveedores",
                            "Documento por Pagar",
                            "ISR por Pagar",
                            "PTU por Pagar",
                            "Total de Pasivo Corto Plazo",
                            "",
                            "Largo Plazo",
                            "Prestamos Bancarios",
                            "Total ed Pasivo Largo Plazo",
                            "",
                            "Pasivo Total",
                            "Capital Contable",
                            "Capital Aportado",
                            "Capital Ganado",
                            "Utilidad del Ejercicio",
                            "Total de Capital Contable",
                            "",
                            "Suma de Pasivo y Capital"],
                        " ":["","",
                             Flujo_efectivo,
                             self.saldo_clientes(),
                             self.esf.activos_circulantes['Deudores Diversos'],
                             self.esf.activos_circulantes['Funcionarios y Empleados'],
                             invf_mat,
                             inv_prod,
                             "","","",
                             self.esf.activos_no_circulantes['Terreno'],
                             planta_equipo,
                             dep_acum,
                             "","","","","","",
                             proveedores_nuevo,
                             self.esf.pasivos_corto['Documentos por Pagar'],
                             0,
                             Ptu,
                             "",
                             "",
                             "",
                             self.esf.pasivos_largo['Préstamos Bancarios'],
                             "","","","","",
                             self.esf.capital_contable['Capital Contribuido'],
                             self.esf.capital_contable['Capital Ganado'],
                             utilidad_neta],
                        "   ":["","","","","","","","",
                               total_activo_circulante,
                               "","","","","",
                               total_activo_nocirculante,
                               "",
                               activo_total,
                               "","","","","","","",
                               total_corto_plazo,
                               "","","",
                               total_largo_plazo,
                               "",
                               total_pasivo,
                               "","","","","",
                               capital,"",
                               pasivo_capital]}
            print(tabulate(tabla_bl, headers="keys", tablefmt="rounded_grid",floatfmt=".2f"))



