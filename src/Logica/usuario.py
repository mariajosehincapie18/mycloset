from prenda import Prenda

class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str, preferenicia_estilo:str, colores_preferidos: str, combinacion_colores_preferidos: str, ropa_favorita: str, prendas_cargadas:Prenda):
        self.nombre_usuario: str = nombre_usuario
        self.contraseña: str= contraseña
        self.preferencia_estilo: str= preferenicia_estilo
        self.colores_preferidos:str = colores_preferidos
        self.combinacion_colores_preferidos: str = combinacion_colores_preferidos
        self.ropa_favorita: str = ropa_favorita
        self.prendas_cargadas : Prenda= prendas_cargadas
        