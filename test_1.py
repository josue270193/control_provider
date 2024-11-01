#Crear un programa para el control de proveedores y listas de precios de productos alimenticios
# teniendo en cuenta los siguientes aspectos: 
#1) El sistema debe ser de acceso restringido sólo para algunas opciones 
# especiales(a considerar según el grupo de trabajo) 
#2) Variaciones de precios según IPC 
#3) Salida de comprobantes por pantalla.
# 4) Altas, bajas y modificaciones de proveedores.

#import sys
# from models.autenticacion import Autenticacion
# from models.proveedores import GestorProveedores #importa la clase GestorProveedores del modulo proveedores
# from models.productos import GestorProductos #importa la clase GestorProductos del modulo productos
# from models.comprobantes import GeneradorComprobantes #importa la clase GeneradorComprobantes del modulo comprobantes
# from models.ipc import CalculadorIPC #importa la clase CalculadorIPC del modulo ipc     


class GestorProveedores:   #clase que gestiona los proveedores alta, baja y modificacion de proveedores    
    def __init__(self):
        self.proveedores = {}
    def alta_proveedor(self): #metodo que permite registrar un nuevo proveedor
        try:
            if not hasattr(self, 'proveedores'):
                self.proveedores = {}
                
            id_proveedor = input("Ingrese ID del proveedor: ")
            nombre = input("Ingrese nombre del proveedor: ")
            direccion = input("Ingrese dirección del proveedor: ")
            telefono = input("Ingrese teléfono del proveedor: ")
            
            if not id_proveedor or not nombre or not direccion or not telefono:
                print("Error: Todos los campos son obligatorios")
                return False
                
            if id_proveedor in self.proveedores:
                print(f"Error: Ya existe un proveedor con el ID {id_proveedor}")
                return False
                
            self.proveedores[id_proveedor] = {
                "nombre": nombre,
                "direccion": direccion,
                "telefono": telefono
            }
            
            print(f"Proveedor registrado exitosamente:")
            print(f"ID: {id_proveedor}")
            print(f"Nombre: {nombre}")
            print(f"Dirección: {direccion}") 
            print(f"Teléfono: {telefono}")
            print(f"Total proveedores en sistema: {len(self.proveedores)}")
            return True
            
        except Exception as e:
            print(f"Error al registrar proveedor: {str(e)}")
            return False
    def baja_proveedor(self):
        try:
            if not hasattr(self, 'proveedores'):
                print("Error: No hay proveedores registrados")
                return False
                
            id_proveedor = input("Ingrese ID del proveedor a eliminar: ")
            
            if id_proveedor not in self.proveedores:
                print(f"Error: No se encontró proveedor con ID {id_proveedor}")
                return False
                
            proveedor_eliminado = self.proveedores.pop(id_proveedor)
            print(f"Proveedor eliminado exitosamente:")
            print(f"ID: {id_proveedor}")
            print(f"Nombre: {proveedor_eliminado['nombre']}")
            print(f"Dirección: {proveedor_eliminado['direccion']}")
            print(f"Teléfono: {proveedor_eliminado['telefono']}")
            print(f"Total proveedores en sistema: {len(self.proveedores)}")
            return True
            
        except Exception as e:
            print(f"Error al eliminar proveedor: {str(e)}")
            return False
    def modificacion_proveedor(self):
        try:
            if not hasattr(self, 'proveedores'):
                print("Error: No hay proveedores registrados")
                return False
                
            id_proveedor = input("Ingrese ID del proveedor a modificar: ")
            
            if id_proveedor not in self.proveedores:
                print(f"Error: No se encontró proveedor con ID {id_proveedor}")
                return False
                
            nombre = input("Ingrese nuevo nombre: ")
            direccion = input("Ingrese nueva dirección: ")
            telefono = input("Ingrese nuevo teléfono: ")
            
            if not nombre or not direccion or not telefono:
                print("Error: Todos los campos son obligatorios")
                return False
                
            self.proveedores[id_proveedor]["nombre"] = nombre
            self.proveedores[id_proveedor]["direccion"] = direccion
            self.proveedores[id_proveedor]["telefono"] = telefono
            
            print(f"Proveedor modificado exitosamente:")
            print(f"ID: {id_proveedor}")
            print(f"Nuevo nombre: {nombre}")
            print(f"Nueva dirección: {direccion}")
            print(f"Nuevo teléfono: {telefono}")
            return True
            
        except Exception as e:
            print(f"Error al modificar proveedor: {str(e)}")
            return False

class Autenticacion:
    def __init__(self):
        self.usuarios = {"admin": {"contraseña": "admin", "rol": "Administrador"},
                         "gerente": {"contraseña": "gerente", "rol": "Gerente"},
                         "operador": {"contraseña": "operador", "rol": "Operador"},
                         "empleado": {"contraseña": "empleado", "rol": "Empleado"}}

    def iniciar_sesion(self):
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        if usuario in self.usuarios and self.usuarios[usuario]["contraseña"] == contrasena:
            self.rol = self.usuarios[usuario]["rol"]
            print(f"Acceso concedido: {self.rol}")
            return True
        else:
            print("Acceso denegado.")
            return False

    def verificar_acceso(self, rol_preciso):
        if self.rol == rol_preciso or self.rol == "Administrador":
            return True
        else:
            print(f"Acceso denegado: Se requiere rol {rol_preciso}.")
            return False

class GestorProductos:  #clase que gestiona los productos alta, baja y modificacion
    def __init__(self):
        self.productos = []
        
    def alta_producto(self, nombre, descripcion, precio, stock):
        try:
            if not hasattr(self, 'productos'):
                self.productos = []
                
            if not nombre or not descripcion or precio <= 0 or stock < 0:
                print("Error: Datos de producto inválidos")
                return False
                
            nuevo_producto = {
                "nombre": nombre,
                "descripcion": descripcion, 
                "precio": precio,
                "stock": stock
            }
            
            self.productos.append(nuevo_producto)
            
            print(f"Producto registrado exitosamente:")
            print(f"Nombre: {nombre}")
            print(f"Descripción: {descripcion}")
            print(f"Precio: ${precio}")
            print(f"Stock: {stock} unidades")
            print(f"Total productos en lista: {len(self.productos)}")
            return True
            
        except Exception as e:
            print(f"Error al registrar producto: {str(e)}")
            return False
    def baja_producto(self, nombre):
        try:
            if not hasattr(self, 'productos'):
                print("Error: No hay productos registrados")
                return False
                
            for i, producto in enumerate(self.productos):
                if producto["nombre"] == nombre:
                    producto_eliminado = self.productos.pop(i)
                    print(f"Producto eliminado exitosamente:")
                    print(f"Nombre: {producto_eliminado['nombre']}")
                    print(f"Descripción: {producto_eliminado['descripcion']}")
                    print(f"Precio: ${producto_eliminado['precio']}")
                    print(f"Stock: {producto_eliminado['stock']} unidades")
                    print(f"Total productos en lista: {len(self.productos)}")
                    return True
                    
            print(f"Error: No se encontró el producto '{nombre}'")
            return False
            
        except Exception as e:
            print(f"Error al eliminar producto: {str(e)}")
            return False
    def modificacion_producto(self, nombre, descripcion, precio, stock):
        try:
            if not hasattr(self, 'productos'):
                print("Error: No hay productos registrados")
                return False
                
            if not nombre or not descripcion or precio <= 0 or stock < 0:
                print("Error: Datos de producto inválidos")
                return False
                
            for producto in self.productos:
                if producto["nombre"] == nombre:
                    producto["descripcion"] = descripcion
                    producto["precio"] = precio 
                    producto["stock"] = stock
                    
                    print(f"Producto modificado exitosamente:")
                    print(f"Nombre: {nombre}")
                    print(f"Nueva descripción: {descripcion}")
                    print(f"Nuevo precio: ${precio}")
                    print(f"Nuevo stock: {stock} unidades")
                    return True
                    
            print(f"Error: No se encontró el producto '{nombre}'")
            return False
            
        except Exception as e:
            print(f"Error al modificar producto: {str(e)}")
            return False

class GeneradorComprobantes:
    def __init__(self):
        self.comprobantes = []  

    def generar_comprobante(self):
        try:
            if not hasattr(self, 'comprobantes'):
                self.comprobantes = []  
            print("Generando comprobante.")
            return True
        except Exception as e:
            print(f"Error al generar comprobante: {str(e)}")
            return False

    def mostrar_comprobantes(self):
        try:
            if not hasattr(self, 'comprobantes'): 
                print("No hay comprobantes registrados")
                return False
            for comprobante in self.comprobantes:
                print(comprobante)          
            return True
        except Exception as e:
            print(f"Error al mostrar comprobantes: {str(e)}")
            return False
        
    def modificar_comprobante(self):
        try:
            print("Modificando comprobante.")
            return True
        except Exception as e:
            print(f"Error al modificar comprobante: {str(e)}")
            return False
        
    def eliminar_comprobante(self):
        try:
            print("Eliminando comprobante.")
            return True
        except Exception as e:
            print(f"Error al eliminar comprobante: {str(e)}")
            return False

class SistemaControlProveedores:#clase principal del sistema que administra los modulos y ejecuta el menu principal
    def __init__(self):#constructor de la clase y se inicializan los modulos
        self.autenticacion = Autenticacion()#se instancia la clase Autenticacion para verificar el acceso al sistema desde el menu principal
        self.gestor_proveedores = GestorProveedores()#se instancia la clase GestorProveedores para gestionar los proveedores desde el menu principal        
        self.gestor_productos = GestorProductos()#se instancia la clase GestorProductos para gestionar los productos desde el menu principal
        self.generador_comprobantes = GeneradorComprobantes()#se instancia la clase GeneradorComprobantes para generar comprobantes desde el menu principal
        # self.calculador_ipc = CalculadorIPC()#se instancia la clase CalculadorIPC para ajustar los precios segun el IPC desde el menu principal

    def ejecutar(self):#metodo que ejecuta el menu principal y llama a los metodos de los modulos correspondientes a cada opcion
        while True:
            opcion = self.mostrar_menu_principal()
            if opcion == '1':
                self.gestionar_proveedores()
            elif opcion == '2':
                self.gestionar_productos()
            elif opcion == '3':
                self.generar_comprobante()
            elif opcion == '4':
                self.ajustar_precios_ipc()
            elif opcion == '5':
                print("Saliendo del sistema...")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")

    def mostrar_menu_principal(self):#metodo que muestra el menu principal y retorna la opcion seleccionada para ejecutar el metodo correspondiente con el modulo
        print("\n--- Menú Principal ---")
        print("1. Gestionar Proveedores")
        print("2. Gestionar Productos")
        print("3. Generar Comprobante")
        print("4. Ajustar Precios según IPC")
        print("5. Salir")
        return input("Seleccione una opción: ")

    def gestionar_proveedores(self):#metodo que gestiona los proveedores y llama a los metodos de los modulos correspondientes a cada opcion del menu proveedores Alta, Baja y Modificacion
        if not self.autenticacion.iniciar_sesion():#verifica si el usuario tiene acceso para gestionar los proveedores
            print("Acceso denegado.")
            return
        # Implementar lógica para gestionar proveedores
        while True:
            print("\n--- Gestión de Proveedores ---")
            print("1. Alta de Proveedor")
            print("2. Baja de Proveedor")
            print("3. Modificación de Proveedor")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.gestor_proveedores.alta_proveedor()
            elif opcion == '2':
                self.gestor_proveedores.baja_proveedor()
            elif opcion == '3':
                self.gestor_proveedores.modificacion_proveedor()
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def gestionar_productos(self):#metodo que gestiona los productos y llama a los metodos de los modulos correspondientes a cada opcion del menu productos Alta, Baja y Modificacion
        if not self.autenticacion.iniciar_sesion():
            print("Acceso denegado.")
            return
        # Implementar lógica para gestionar productos
        while True:
            print("\n--- Gestión de Productos ---")
            print("1. Alta de Producto")
            print("2. Baja de Producto")
            print("3. Modificación de Producto")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.gestor_productos.alta_producto()
            elif opcion == '2':
                self.gestor_productos.baja_producto()
            elif opcion == '3':
                self.gestor_productos.modificacion_producto()
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def generar_comprobante(self):#metodo que genera comprobantes y llama al metodo del modulo correspondiente y verifica si el usuario tiene acceso para generar comprobantes
        if not self.autenticacion.iniciar_sesion():
            print("Acceso denegado.")
            return
        # Implementar lógica para generar comprobantes
        self.generador_comprobantes.generar_comprobante()
        #mostrar los comprobantes
        self.generador_comprobantes.mostrar_comprobantes()
        #modificar un comprobante
        self.generador_comprobantes.modificar_comprobante()
        #eliminar un comprobante
        self.generador_comprobantes.eliminar_comprobante() 

    def ajustar_precios_ipc(self):#metodo que ajusta los precios segun el IPC y llama al metodo del modulo correspondiente y verifica si el usuario tiene acceso para ajustar los precios
        if not self.autenticacion.iniciar_sesion():
            print("Acceso denegado.")
            return
        # Implementar lógica para ajustar precios según IPC
        # self.calculador_ipc.ajustar_precios()   
        #mostrar el IPC
        # self.calculador_ipc.mostrar_ipc()


#metodo que ejecuta el programa principal y llama al metodo ejecutar de la clase SistemaControlProveedores
sistema = SistemaControlProveedores()#se instancia la clase SistemaControlProveedores para ejecutar el programa y se llama al metodo ejecutar   
sistema.ejecutar()#se ejecuta el programa en un bucle infinito hasta que el usuario seleccione la opcion 5 para salir, inicia el menu principal
#fin del programa
