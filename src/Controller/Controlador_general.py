import sys
import os
import shutil
from pathlib import Path
sys.path.append("src")
from  database.data_conexion import DBconexion
from  Controller.usuarioDao import UsuarioDAO
from Controller.prendaDao import PrendaDAO
from Controller.outfitDao import OutfitDAO
from Controller.prendaOutfitDao import OutfitPrendaDAO
from gestores.gestorUsuario import GestorUsuario
from gestores.gestorPrenda import GestorPrenda
from GUI.gui import MenuPrincipal


db_conexion = DBconexion(db_path="src/database/mycloset.db")

usuario_dao= UsuarioDAO(db_conexion)
prenda_dao = PrendaDAO(db_conexion)
outfit_dao= OutfitDAO(db_conexion)
Outfit_prenda_dao= OutfitPrendaDAO(db_conexion)

#registrar usuario
gestor_usuario = GestorUsuario(db_conexion)


#registro prenda
gestor_prenda= GestorPrenda(prenda_dao)


nombre_usuario= input("ingrese el nombre del usuario")
gestor_prenda.registrar_prenda_usuario(gestor_usuario, nombre_usuario )

menu = MenuPrincipal(gestor_prenda,gestor_usuario)
menu.mostrar_menu()