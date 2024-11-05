import sys
sys.path.append("src")
from modelo.usuario import Usuario
class PrendaDAO:
    def __init__(self, db):
        self.db = db
        self.crear_tabla ()


    def crear_tabla(self):
        cursor = self.db.get_cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS prendas (
        id_prenda INTEGER  PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
        nombre_prenda VARCHAR(100),
        ocasion VARCHAR(50),
        talla VARCHAR(10),
        temporada VARCHAR(50),
        imagen_prenda TEXT
        color_prenda TEXT
        tipo_prenda TEXT
        );
        """ )

        self.db.conector.commit()

    def agregar_prenda(self, prenda, usuario_id:Usuario):
        cursor= self.db.get_cursor()
        self.usuario_id= usuario_id
        cursor.execute(""" 
        INSERT INTO prendas(usuario_id, nombre_prenda, ocasion,
        talla, temporada, imagen_prenda, color_prenda, tipo_prenda) VALUES(?,?,?,?,?,?)""",
        (prenda.usuario_id, prenda.nombre_prenda, prenda.ocasion,
        prenda.talla, prenda.temporada, prenda.imagen_prenda, prenda.color_prenda, prenda.tipo_prenda))
        self.db.conector.commit()
         
        

    