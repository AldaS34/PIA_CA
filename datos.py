from tabulate import *
from decimal import *

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
         self.ventas_plan = lista

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
        self.ventas_plan = lista

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
         print(f"{self.nombre} se mide en {self.unidad}")
         print(f"Tiene un requerimiento de {self.req_mat}")
         print(f"Primer semestre al inicio tiene {self.inv_inicial} y al final del segundo {self.inv_final}")
         print(f"Su costo en el primer semestre es {self.costoXsem['sem1']}")
         print(f"Su costo en el segundo semestre es {self.costoXsem['sem2']}")

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
         print(f"Comisiones: {100*self.comisiones}%")
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
        print(f"Porcentaje ISR: {self.isr}%")
        print(f"Porcentaje PTU: {self.ptu}%")
        print(f"Se cobrará el {self.cobrar_clientes}% del saldo de clientes")
        print(f"Se cobrará el {self.cobrar_ventas}% de las ventas presupuestadas")
        print(f"Se pagará el {self.pagar_prov}% del saldo de proveedores")
        print(f"Se pagará el {self.pagar_comp}% de las compras presupuestadas")

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
        