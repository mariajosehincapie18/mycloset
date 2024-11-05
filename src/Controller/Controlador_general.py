import sys
sys.path.append("src")
from  database.data_conexion import DBconexion
from  Controller.usuarioDao import UsuarioDAO
from Controller.prendaDao import PrendaDAO
from Controller.outfitDao import OutfitDAO
from Controller.prendaOutfitDao import OutfitPrendaDAO
from gestores.gestorUsuario import GestorUsuario


db_conexion = DBconexion(db_path="src/database/mycloset.db")

usuario_dao= UsuarioDAO(db_conexion)
prenda_dao = PrendaDAO(db_conexion)
outfit_dao= OutfitDAO(db_conexion)
Outfit_prenda_dao= OutfitPrendaDAO(db_conexion)

#registrar usuario
gestor_usuario = GestorUsuario(db_conexion)

gestor_usuario.registrar_usuario()
usuario_actual= gestor_usuario.obtener_usuario_por_nombre("majo")
gestor_usuario.agregar_prenda_usuario(usuario_actual)
