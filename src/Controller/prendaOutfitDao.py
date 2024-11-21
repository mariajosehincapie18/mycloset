class OutfitPrendaDAO:
    def __init__(self, db):
        self.db= db
        self.crear_tabla()
    
    def crear_tabla(self):
        cursor = self.db.get_cursor()
        cursor.execute(
            """ CREATE TABLE IF NOT EXISTS prenda_outfit(
        id_prenda_outfit INTEGER PRIMARY KEY AUTOINCREMENT ,
        id_outfit INTEGER NOT NULL REFERENCES Outfit(id_outfit) ON DELETE CASCADE,
        id_prenda INTEGER NOT NULL REFERENCES prendas(id_prenda) ON DELETE CASCADE,
        id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario) ON DELETE CASCADE);
        """)

        self.db.conector.commit()

    def insertar_prenda_outfit(self,id_outfit, id_prenda, id_usuario):
        cursor= self.db.get_cursor()
        cursor.execute("INSERT INTO prenda_outfit( id_outfit, id_prenda, id_usuario) VALUES (?,?,?)", (id_outfit, id_prenda, id_usuario))
        self.db.conector.commit()
        

    def obtener_prendas_por_outfit(self, id_outfit, id_usuario):
        cursor= self.db.get_cursor()
        cursor.execute(
            """ SELECT  p.nombre_prenda, p.tipo_prenda, p.color_prenda, p.imagen_prenda
            FROM prendas AS p
            JOIN prenda_outfit AS op ON p.id_prenda= op.id_prenda
            WHERE op.id_outfit= ? AND op.id_usuario= ?""", (id_outfit, id_usuario)
        )
        
        detalles = cursor.fetchall()
        print("prendas obtenidas para el outfit: ", detalles)
        return [{"nombre": nombre, "tipo": tipo, "color": color, "imagen_prenda": imagen_prenda} for nombre, tipo, color , imagen_prenda in detalles]