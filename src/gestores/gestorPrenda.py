import sys
sys.path.append("src")
from modelo.prenda import Prenda
from Controller.prendaDao import PrendaDAO
from pathlib import Path
import os
import shutil #biblioteca para copiar archivos


class GestorPrenda:
    def __init__(self, prenda_dao: PrendaDAO):
        self.prenda_dao= prenda_dao


    def agregar_prenda(self,id_usuario, nombre_prenda, talla, ocasion, imagen_prenda, color_prenda, tipo_prenda ):
        #guardamos la imagen en la carpeta "imagenes"
        saved_image_path= self.guardar_imagen(imagen_prenda)

        #creamos el objeto prenda con la ruta de la imagen
        nueva_prenda= Prenda(nombre_prenda=nombre_prenda, talla=talla, ocasion=ocasion, imagen_prenda=saved_image_path, color_prenda=color_prenda, tipo_prenda=tipo_prenda)
        #guardar la prenda en la base de datos
        self.prenda_dao.insertar_prenda(nueva_prenda, id_usuario)

     
    def guardar_imagen(self, imagen_prenda):
        #definimos los directorios para guardar las imagenes:
        imagen_directorio= Path("imagenes/")
        #se crea el directorio si no existe
        imagen_directorio.mkdir(parents=True, exist_ok=True) 
        

        #se define la unica ruta del archivo de la imagen
        imagen_filename= os.path.basename(imagen_prenda)
        nueva_imagen= imagen_directorio / imagen_filename

        #copiamos el archivo de a imagen a la carpeta de imagenes
        shutil.copy(imagen_prenda, nueva_imagen)

        return str(nueva_imagen)



        