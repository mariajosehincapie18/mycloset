class PrendaDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion
        self.crear_tabla ()


    def crea_tabla(self):
        self.db.cursor.execute()