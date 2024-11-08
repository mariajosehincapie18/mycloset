import sys
sys.path.append("src")
from Controller.usuarioDao import UsuarioDAO
from modelo.usuario import Usuario
from Controller.prendaDao import PrendaDAO
from modelo.prenda import Prenda


class GestorUsuario:
    def __init__(self, db):
        self.usuario_dao = UsuarioDAO(db)
        self.prenda_dao = PrendaDAO(db)

    def registrar_usuario(self):
        print("REGISTRO DE USUARIO")

        nombre_usuario = input("NOMBRE DE USUARIO: ")
        contraseña = input("CONTRASEÑA: ")
        preferencia_estilo = input("PREFERENCIA DE ESTILO(formal, cuasual, deportivo):")
        colores_preferidos= input("COLORES FAVORITOS(azul, negro, blanco, etc)").split(",")
        ropa_favorita =input ("TIPOS DE ROPA FAVORITOS(jens, camisas, tenis, sacos):").split(";")

        nuevo_usuario =Usuario( nombre_usuario=nombre_usuario, 
        contraseña=contraseña, preferenicia_estilo=preferencia_estilo,colores_preferidos= colores_preferidos,
        ropa_favorita= ropa_favorita)

        self.usuario_dao.registrar_usuario(nuevo_usuario)
        print("usuario registrado exitosamente")

    def obtener_usuario_por_nombre(self, nombre_usuario):
        return self.usuario_dao.obtener_usuario_por_nombre(nombre_usuario)  

    
    
   
    