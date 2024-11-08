import sys
sys.path.append("src")
from modelo.prenda import Prenda
from Controller.prendaDao import PrendaDAO
import os


class GestorPrenda:
    def __init__(self, prenda_dao: PrendaDAO, usuario_dao, gestor_imagen):
        self.prenda_dao= prenda_dao
        self.usuario_dao = usuario_dao
        self.gestor_imagen= gestor_imagen


    def obtener_usuario_por_nombre(self, nombre_usuario):
        return self.usuario_dao.obtener_usuario_por_nombre(nombre_usuario)

    def registrar_prenda_usuario(self, nombre_usuario):
        usuario= self.obtener_usuario_por_nombre(nombre_usuario)
        if not usuario:
            print("usuario no encontrado.")
            return
    
        print("Registro de nueva prenda:")
        nombre_prenda= input("Nombre de la prenda: ")
        talla= input("talla: ")
        ocasion= input("ocasion(ejemplo: elegante, fiesta)")
        temporada= input("temporda: (ejemplo: verano, invierno)")
        imagen_path= input("nombre de la imagen en la carpeta: (ej: camisaroja.jpg) ")
        color_prenda= input("color de la prenda: ")
        tipo_prenda= input("tipo de prenda(ejemplo: casual, formal, deportivo)")

    #llamar agreagar prenda para registar la prenda
        self.agregar_prenda(
            id_usuario= usuario.id_usuario,
            nombre_prenda= nombre_prenda,
            talla=talla,
            ocasion= ocasion,
            temporada= temporada,
            imagen_path= imagen_path,
            color_prenda= color_prenda,
            tipo_prenda= tipo_prenda

    )

    def agregar_prenda(self, id_usuario, nombre_prenda, talla, ocasion,temporada, imagen_path, color_prenda, tipo_prenda):
        imagen_path = self.gestor_imagen.guardar_imagen(imagen_path)

        if imagen_path is None:
            print("no se puede registrar la prenda por la imagen no existe en la carpeta imagenes.")
            return


        #creamos el objeto prenda con la ruta de la imagen
        nueva_prenda= Prenda(
            nombre_prenda= nombre_prenda,
            talla= talla,
            ocasion= ocasion,
            temporada= temporada,
            imagen_path= imagen_path,
            color_prenda= color_prenda,
            tipo_prenda=tipo_prenda,

        )
#insertamos la prenda en la base de datos
        self.prenda_dao.insertar_prenda(nueva_prenda, id_usuario)

    def ver_prendas(self):
        print("/nLISTADO DE PRENDAS")
        prendas= []
        for prendas in prendas:
            print (f"ID: {Prenda.id_prenda}, NOMBRE: {Prenda.nombre_prenda}, Talla: {Prenda.talla}, ocasion: {Prenda.ocasion}, imagen: {Prenda.ruta_imagen}, color: {Prenda.color_prenda}, tipo: {Prenda.tipo_prenda}")
        