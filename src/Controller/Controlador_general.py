import sys
sys.path.append("src")
from  database.data_conexion import DBconexion
from  Controller.usuarioDao import UsuarioDAO
from Controller.prendaDao import PrendaDAO
from Controller.outfitDao import OutfitDAO
from Controller.prendaOutfitDao import OutfitPrendaDAO


db_conexion = DBconexion(db_path="src/database/closet.db")

usuario_dao= UsuarioDAO(db_conexion)
prenda_dao = PrendaDAO(db_conexion)
outfit_dao= OutfitDAO(db_conexion)
Outfit_prenda_dao= OutfitPrendaDAO(db_conexion)