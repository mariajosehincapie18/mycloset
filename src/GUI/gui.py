import sys
sys.path.append("src")



class MenuPrincipal:
    def __init__(self, gestor_prenda, gestor_usuario):
        self.gestor_prenda = gestor_prenda
        self.gestor_usuario= gestor_usuario
        

    def mostrar_menu(self):
        while True:
            print("/n*** MENU PRINCIPAL ***")
            print("1. Registrar usuario")
            print("2. Agregar prenda")
            print("3, ver prendas")
            print("4. salir")

            opcion= input("seleccione una opcion:  ")

            if opcion == "1":
                self.gestor_usuario.registrar_usuario()
            elif opcion == "2":
                nombre_usuario= input(" INGRESE EL NOMBRE DEL USUARIO: ")
                self.gestor_prenda.registrar_prenda_usuario(nombre_usuario)
            elif opcion == "3":
                self.gestor_prenda.ver_prendas()
            elif opcion == "4":
                print("saliendo del programa")
                break
            else:
                print("opcion no valida, selecciona otra opcion")

