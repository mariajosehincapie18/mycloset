class OutfitDAO:
    def __init__(self, db):
        self.db= db
        self.crear_tabla()

    def crear_tabla(self):
        cursor= self.db.get_cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Outfit(
            id_outfit INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_outfit VARCHAR,
            prendas Varchar);
            """
            )

        self.db.conector.commit()

    def insertar_outfit(self, nombre_outfit):
        cursor= self.db.get_cursor()
        cursor.execute("INSERT INTO Outfit (nombre_outfit) VALUES (?)", (nombre_outfit,))
        self.db.conector.commit()
        return cursor.lastrowid
    

    def obtener_id_outfit_por_nombre(self, nombre_outfit):
        cursor= self.db.get_cursor()
        cursor.execute("SELECT id_outfit From Outfit WHERE nombre_outfit = ? ", (nombre_outfit,))
        result= cursor.fetchone()
        if result:
            return result[0]
        return None