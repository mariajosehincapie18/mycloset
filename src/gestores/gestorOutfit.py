class GestorOutfit:
    def __init__(self, outfit_dao,prenda_outfit_dao ):
        self.outfit_dao= outfit_dao
        self.prenda_outfit_dao= prenda_outfit_dao
        

    def crear_outfit(self, nombre_outfit, prendas_seleccionadas, id_usuario):
        #guarda el outfit en la base de datos
        outfit_id= self.outfit_dao.insertar_outfit(nombre_outfit)
    
        for prenda_id in prendas_seleccionadas:
            self.prenda_outfit_dao.insertar_prenda_outfit(outfit_id,prenda_id, id_usuario)

        print("Outfit creadoy guardado exitosamente.")

        

