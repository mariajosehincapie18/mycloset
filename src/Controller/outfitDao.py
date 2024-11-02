class OutfitDAO:
    def __init__(self, db):
        self.db= db
        self.crear_tabla()

    def crear_tabla(self):
        cursor= self.db.get_cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Outfit(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_outfit VARCHAR,
            prendas Varchar);
            """
            )

        self.db.conector.commit()