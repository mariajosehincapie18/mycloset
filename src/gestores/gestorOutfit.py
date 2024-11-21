import sys
sys.path.append("src")
class GestorOutfit:
    def __init__(self, outfit_dao,prenda_outfit_dao, prenda_dao ):
        self.outfit_dao= outfit_dao
        self.prenda_outfit_dao= prenda_outfit_dao
        self.prenda_dao = prenda_dao
        
        

    def crear_outfit(self, nombre_outfit,ids_prendas_seleccionadas, id_usuario):
        
        prendas_usuario = self.prenda_dao.obtener_prendas_por_usuario(id_usuario)

        
        nombres_prendas= [prenda["nombre_penda"] for prenda in prendas_usuario if prenda["id_prenda"] in ids_prendas_seleccionadas]
        nombres_prendas_str= " , ".join(nombres_prendas)

        outfit_id= self.outfit_dao.insertar_outfit(nombre_outfit, nombres_prendas_str)

    
        for id_prenda in ids_prendas_seleccionadas:
            self.prenda_outfit_dao.insertar_prenda_outfit(outfit_id, id_prenda)

        print("Outfit creado y guardado exitosamente.")


    def obtener_nombres_prendas(self, prendas_seleccionadas):
        nombres_prendas= []
        for id_prenda in prendas_seleccionadas:
            nombre_prenda= self.prenda_outfit_dao.obtener_nombre_prenda_por_id(id_prenda)

    def obtener_detalle_outfit(self, nombre_outfit):
        outfit= self.outfit_dao.obtener_outfit_por_nombre(nombre_outfit)
        if outfit is None:
            print("Outfit no encontrado")
            return None
        
        detalles= self.prenda_outfit_dao.obtener_prendas_por_outfit(outfit["id_outfit"])
        return{"nombre_outfit": outfit["nombre_outfit"], "nombres_prendas":outfit["nombres_prendas"], "detalles": detalles}
        



