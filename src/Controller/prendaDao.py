class PrendaDAO:
    def __init__(self, db):
        self.db = db
        self.crear_tabla ()


    def crear_tabla(self):
        cursor = self.db.get_cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS prendas (
        id_prenda SERIAL  PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
        nombre_prenda VARCHAR(100),
        ocasion VARCHAR(50),
        talla VARCHAR(10),
        temporada VARCHAR(50)
        );
        """
    )

        self.db.conector.commit()

    