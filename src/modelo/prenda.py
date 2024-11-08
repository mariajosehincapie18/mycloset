
class Prenda:
    LAVADAYLISTA = "Lista"
    SUCIA = "Sucia"
    ARREGLO = "Arreglo"
    def __init__(self,nombre_prenda: str, talla: str, ocasion: str,temporada,  imagen_path: str, color_prenda:str, tipo_prenda: str):
        self.nombre_prenda = nombre_prenda
        self.talla = talla
        self.ocasion = ocasion 
        self.estado = None
        self.temporada= temporada
        self.imagen_path= imagen_path
        self.color_prenda = color_prenda
        self.tipo_prenda = tipo_prenda


    def cambiar_estado(self, tipo:int):
        if tipo == 1:
            self.estado = Prenda.LAVADAYLISTA
        elif tipo == 2:
            self.estado = Prenda.SUCIA
        elif tipo == 3:
            self.estado = Prenda.ARREGLO
        return 