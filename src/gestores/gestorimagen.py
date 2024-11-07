from pathlib import Path
import os
import shutil


class GestorImagen:
    def __init__(self, imagen_directorio="imagenes/"):
        self.imagen_directorio= Path(imagen_directorio)
        self.imagen_directorio.mkdir(parents=True, exist_ok=True)#crea el directorio sino existe

    def guardar_imagen(self,imagen_prenda ):
        #define el nombre y la ruta de la imagen

        imagen_nombre= os.path.basename(imagen_prenda)
        nueva_imagen= self.imagen_directorio/ imagen_nombre

        #copia la imagen a la carpeta de imagenes
        shutil.copy(imagen_prenda, nueva_imagen)
        print(f"IMAGEN GUARDAD EN: {nueva_imagen}")

        return str(nueva_imagen) #ruta donde se guarda la imagen
