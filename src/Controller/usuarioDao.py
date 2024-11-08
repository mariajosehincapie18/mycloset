import sys
sys.path.append("src")
from modelo.usuario import Usuario

class UsuarioDAO:
    def __init__(self, db):
        self.db = db
        self.crear_tabla()
        

    def crear_tabla(self):
        cursor = self.db.get_cursor()
        cursor.execute( """
            CREATE TABLE  IF NOT EXISTS usuarios(
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usuario VARCHAR(100),
        contraseña VARCHAR(100),
        preferencia_estilo VARCHAR(100),
        colores_preferidos VARCHAR(100),
        ropa_favorita VARCHAR(100)
        )
        """)

        self.db.conector.commit()

    def registrar_usuario(self, usuario):
        cursor = self.db.get_cursor()
        cursor.execute("""
        INSERT INTO usuarios(nombre_usuario, contraseña, preferencia_estilo,
        colores_preferidos, ropa_favorita) VALUES (?,?,?,?,?)""", (usuario.nombre_usuario,
        usuario.contraseña, usuario.preferencia_estilo,",".join(usuario.colores_preferidos),
        ",".join(usuario.ropa_favorita))) 
        self.db.conector.commit()
        return cursor.lastrowid

    def obtener_usuario_por_nombre(self, nombre_usuario):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario= ?", (nombre_usuario,))
        row = cursor.fetchone()
        if row:
            return Usuario(id_usuario=row[0],
                nombre_usuario=row[1],
                contraseña=row[2],
                preferenicia_estilo=row[3],
                colores_preferidos=row[4].split(" , "),
                ropa_favorita=row[5].split(" , ")
            )
        return None
     
        


   
   