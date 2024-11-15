class GestorOutfit:
    def __init__(self, outfit_dao,prenda_outfit_dao ):
        self.outfit_dao= outfit_dao
        self.prenda_outfit_dao= prenda_outfit_dao
        

    def crear_outfit(self, nombre_outfit, prendas_seleccionadas, id_usuario):
        #guarda el outfit en la base de datos
        outfit_id= self.outfit_dao.insertar_outfit(nombre_outfit)
    
        for id_prenda in prendas_seleccionadas:
            self.prenda_outfit_dao.insertar_prenda_outfit(outfit_id, id_prenda, id_usuario)

        print("Outfit creado y guardado exitosamente.")

    def obtener_detalle_outfit(self, nombre_outfit):
        id_outfit= self.outfit_dao.obtener_id_outfit_por_nombre(nombre_outfit)
        if id_outfit is None:
            print("Outfit no encontrado")
            return[]
        
        detalles= self.prenda_outfit_dao.obtener_prendas_por_outfit(id_outfit)
        print("detalles del outfit", detalles)
        return[{"prenda": prenda["nombre"], "tipo":prenda["tipo"], "color": prenda["color"], "imagen_path":prenda["imagen_path"]} for prenda in detalles]
        

