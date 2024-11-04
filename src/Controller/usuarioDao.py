class UsuarioDAO:
    def __init__(self, db):
        self.db = db
        self.crear_tabla()
        

    def crear_tabla(self):
        cursor = self.db.get_cursor()
        cursor.execute( """
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
     
        


   
   