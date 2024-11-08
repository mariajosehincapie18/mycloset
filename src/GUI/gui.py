import sys
sys.path.append("src")
import tkinter as tk
from PIL import Image, ImageTk


class Gui:
    def __init__(self, gestor_prenda):
        self.gestor_prenda= gestor_prenda


    def mostrar_prendas_en_ventana(self):
        #obtiene todas las prendas de la base de datos
        prendas= self.gestor_prenda.prenda_dao.obtener_todas_las_prendas()

        if not prendas:
            print("No hay prendas disponibles. ")
            return
#ventana de tkinter
        ventana= tk.Tk()
        ventana.title("*** MIS PRENDAS ***")
#creamos un frame en la ventana para mostrar las imagenes y nombres
        frame= tk.Frame(ventana)
        frame.pack

#recorremos cada prenda para mostrar su nombre e imagen

        for prenda in prendas:
            nombre_prenda= prenda[0]
            imagen_prenda= prenda[1]

        label_nombre = tk.Label(frame, text= nombre_prenda)
        label_nombre.pack

        try:
            imagen= Image.open(imagen_prenda)
            imagen.thumbnail((100,100))
            imagen_tk = ImageTk.PhotoImage(imagen)

            label_imagen= tk.Label(frame, image= imagen_tk)
            label_imagen.image = imagen_tk
            label_imagen.pack()
        except Exception as e:
            print(f"Error al cargar la imagen {imagen_prenda}: {e}")

        ventana.mainloop()



