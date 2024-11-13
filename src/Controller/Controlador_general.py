import sys
sys.path.append("src")
from  database.data_conexion import DBconexion
from  Controller.usuarioDao import UsuarioDAO
from Controller.prendaDao import PrendaDAO
from Controller.outfitDao import OutfitDAO
from Controller.prendaOutfitDao import OutfitPrendaDAO
from gestores.gestorUsuario import GestorUsuario
from gestores.gestorPrenda import GestorPrenda
from gestores.gestorimagen import GestorImagen
from gestores.gestorAutenticacion import Autenticacion
from gestores.gestorOutfit import GestorOutfit
from GUI.gui import Gui




db_conexion = DBconexion(db_path="src/database/mycloset.db")

usuario_dao= UsuarioDAO(db_conexion)
prenda_dao = PrendaDAO(db_conexion)
outfit_dao= OutfitDAO(db_conexion)
Outfit_prenda_dao= OutfitPrendaDAO(db_conexion)

#registrar usuario
gestor_usuario = GestorUsuario(db_conexion)


#registro prenda
gestor_imagen= GestorImagen()
gestor_prenda= GestorPrenda(prenda_dao, usuario_dao, gestor_imagen )
gestor_outfit= GestorOutfit(outfit_dao, Outfit_prenda_dao)
gui= Gui(gestor_prenda, gestor_outfit)

gestor_autenticacion = Autenticacion(gestor_usuario, gestor_prenda,gestor_outfit, gui)

gestor_autenticacion. mostrar_menu_principal()
