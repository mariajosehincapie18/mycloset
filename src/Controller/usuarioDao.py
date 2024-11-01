
class UsuarioDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion
        self.crear_tabla()
        

    def crear_tabla(self):
        self.db.cursor.execute( """
            CREATE TABLE  IF NOT EXISTS usuarios(
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        contraseña VARCHAR(100),
        preferenica_estilo VARCHAR(100),
        colores preferidos VARCHAR(100),
        ropa favorita VARCHAR(100)
        )
        """)

        self.db.conector.commit()
        