class Usuario:
    def __init__(self,nombre_usuario: str, contraseña: str, preferenicia_estilo:str, colores_preferidos: str,  ropa_favorita: str, id_usuario= None):
        self.id_usuario= id_usuario
        self.nombre_usuario: str = nombre_usuario
        self.contraseña: str= contraseña
        self.preferencia_estilo: str= preferenicia_estilo
        self.colores_preferidos:str = colores_preferidos
        self.ropa_favorita: str = ropa_favorita
        
       

        