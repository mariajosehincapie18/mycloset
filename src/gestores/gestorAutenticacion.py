import sys
sys.path.append("src")

class Autenticacion:
    def __init__(self, gestor_usuario, gestor_prenda):
        self.gestor_usuario= gestor_usuario
        self.gestor_prenda= gestor_prenda
        

    def mostrar_menu_principal(self):
        while True:
            print("\n**** menu principal***")
            print("1. Registrar usuario")
            print("2. Ingresar")
            opcion= input("selccione una opcion: ")


            if opcion == "1":
                self.gestor_usuario.registrar_usuario()
            elif opcion == "2":
                usuario= self.ingresar_usuario()
                if usuario:
                    self.mostrar_menu_usuarios(usuario)
                else: 
                    print("Nombre de usuario o contraseña incorrectos")

            else:
                print("opcion no valida. intente de nuevo. ")

    def ingresar_usuario(self):
        nombre_usuario= input("Nombre de usuario: ")
        contraseña= input("ingrese contraseña: ")
#buscamos el usuario en la base de datos
        usuario= self.gestor_usuario.obtener_usuario_por_nombre(nombre_usuario)

#verificamos si el usuario existe y la contraseña es correcta
        if usuario and usuario.contraseña == contraseña:
            print("autenticacion existosa. ")
            return usuario
        else:
            return None
        
    def mostrar_menu_usuarios(self, usuario):
        while True:
            print("\n*** MICLOSET***")
            print("1. Registrar prenda")
            print("2. Ver prendas")
            print("3. salir")
            opcion= input("Seleccione una opcion: ")

            if opcion== "1":
                self.gestor_prenda.registrar_prenda_usuario(usuario.nombre_usuario)
            elif opcion == "2":
                self.gestor_prenda.ver_prendas()
            elif opcion == "3":
                print("cerrar sesion")
                break
            else:
                print("opcion no valida. intente de nuevo.")


