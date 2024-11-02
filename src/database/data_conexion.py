import sqlite3

class DBconexion:
    def __init__(self, db_path="src/database/closet.db"):
        self.conector = None
        self.db_path = db_path
        self.conectar()


    def conectar(self):
        try:
            self.conector = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print("error al conectra la base de datos")


    def get_cursor(self):
        if self.conector:
            return self.conector.cursor()
        else:
            raise Exception("no hay conexion activa de la base de datos")
        
    def cerrar(self):
        if self.conector:
            self.conector.close()
        