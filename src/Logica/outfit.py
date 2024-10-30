from prenda import Prenda

class Outfit:
    def __init__(self,  nombre_outfit: str, prendas:Prenda):
        self.nombre_outfit:str = nombre_outfit
        self.prendas: Prenda = prendas
    
    def agregar_prenda(self):
        pass

    def quitar_prenda(self):
        pass
