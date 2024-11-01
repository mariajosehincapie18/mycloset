import sqlite3

class DBconexion:
    def __init__(self, db_path="databa/closet.db"):
        self.conector = sqlite3.connect(db_path)
        self.cursor = self.conector.cursor()

    def cerrar(self):
        self.conector.close()
        