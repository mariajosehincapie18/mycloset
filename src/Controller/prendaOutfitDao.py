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

    def insertar_prenda_outfit(self, prenda_id, usuario_id):
        cursor= self.db.get_cursor()
        cursor.execute("INSERT INTO prenda_outfit( prenda_id, usuario_id) VALUES (?,?)", ( prenda_id, usuario_id))
        self.db.conector.commit()
        

    def obtener_prendas_por_outfit(self, id_outfit):
        cursor= self.db.get_cursor()
        cursor.execute(
            """ SELECT  nombre_prenda, tipo_prenda, color_prenda
            FROM prendas AS p
            JOIN prenda_outfit AS op ON p.id_prenda= op.id_prenda
            WHERE op.id_outfit= ?""", (id_outfit)
        )
        
        detalles = cursor.fetchall()
        print("prendas obtenidas para el outfit: ", detalles)
        return [{"nombre": nombre, "tipo": tipo, "color": color } for nombre, tipo, color in detalles]