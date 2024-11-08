import sys
sys.path.append("src")
import tkinter as tk
from PIL import Image, ImageTk


class Gui:
    def __init__(self, gestor_prenda):
        self.gestor_prenda= gestor_prenda


    def mostrar_prendas_en_ventana(self, id_usuario):
        #obtiene todas las prendas de la base de datos
        prendas= self.gestor_prenda.prenda_dao.obtener_todas_las_prendas(id_usuario)

        if not prendas:
            print("No hay prendas disponibles. ")
            return
#ventana de tkinter
        ventana= tk.Tk()
        ventana.title("*** MIS PRENDAS ***")
#creamos un frame en la ventana para mostrar las imagenes y nombres
        frame= tk.Frame(ventana)
        frame.pack()

#recorremos cada prenda para mostrar su nombre e imagen

        for prenda in prendas:
            nombre_prenda= prenda[0]
            imagen_prenda= prenda[1]

            label_nombre = tk.Label(frame, text= nombre_prenda)
            label_nombre.pack()

            try:
                imagen= Image.open(imagen_prenda)#abre el archivo de imagen de la ruta imagen_prenda
                imagen.thumbnail((100,100))#redimensiona la imagen , matiene la proporcion
                imagen_tk = ImageTk.PhotoImage(imagen)#convierte la imagen en un objeto compatible con tk

                label_imagen= tk.Label(frame, image= imagen_tk)#guarda una referencia de la imagen para evitar qeu se elimine cuando se muestre
                label_imagen.image = imagen_tk #guarda referencias para tk
                label_imagen.pack()
            except Exception as e:
                print(f"Error al cargar la imagen {imagen_prenda}: {e}")

        ventana.mainloop()



