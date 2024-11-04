class OutfitPrendaDAO:
    def __init__(self, db):
        self.db= db
        self.crear_tabla()
    
    def crear_tabla(self):
        cursor = self.db.get_cursor()
        cursor.execute(
            """ CREATE TABLE IF NOT EXISTS prenda_outfit(
        id_prenda_outfit INTEGER PRIMARY KEY AUTOINCREMENT ,
        prenda_id INTEGER NOT NULL REFERENCES prendas(id_prenda) ON DELETE CASCADE,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id_usuario) ON DELETE CASCADE);
        """)
        self.db.conector.commit()
        