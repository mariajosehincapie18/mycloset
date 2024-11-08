from pathlib import Path
import os
import shutil


class GestorImagen:
    def __init__(self, imagen_directorio="imagenes/"):
        self.imagen_directorio= Path(imagen_directorio)
        self.imagen_directorio.mkdir(parents=True, exist_ok=True)#crea el directorio sino existe

    def guardar_imagen(self,imagen_nombre ):
       #construir la ruta completa usando el nombre del archivo dentro de la carpeta de imagenes
        ruta_imagen= self.imagen_directorio / imagen_nombre

        if not ruta_imagen.is_file():
            print("la no existe en la carpeta imagenes: intentalo de nuevo. ")
            return None
        
        print(f"IMAGEN ENCONTRADA Y REGISTRADA EN : {ruta_imagen}")
        return str(ruta_imagen)
            
        
        