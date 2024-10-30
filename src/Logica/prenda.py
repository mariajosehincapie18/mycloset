
class Prenda:
    LAVADAYLISTA = "Lista"
    SUCIA = "Sucia"
    ARREGLO = "Arreglo"
    def __init__(self,nombre: str, tipo_prenda: str, color_prenda: str, talla: str, ocasion: str):
        self.nombre = nombre
        self.tipo_prenda = tipo_prenda
        self.color_prenda = color_prenda
        self.talla = talla
        self.ocasion = ocasion 
        self.estado = None

    def cambiar_estado(self, tipo:int):
        if tipo == 1:
            self.estado = Prenda.LAVADAYLISTA
        elif tipo == 2:
            self.estado = Prenda.SUCIA
        elif tipo == 3:
            self.estado = Prenda.ARREGLO
        return