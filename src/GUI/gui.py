import sys
sys.path.append("src")
from gestores.gestorUsuario import GestorUsuario
from gestores.gestorPrenda import GestorPrenda


class MenuPrincipal:
    def __init__(self, gestor_prenda:GestorPrenda, gestor_usuario:GestorUsuario):
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
                self.gestor_prenda.agregar_prenda()
            elif opcion == "3":
                self.gestor_prenda.ver_prendas()
            elif opcion == "4":
                print("saliendo del programa")
                break
            else:
                print("opcion no valida, selecciona otra opcion")

