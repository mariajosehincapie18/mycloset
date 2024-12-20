import sys
sys.path.append("src")
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


class Gui:
    def __init__(self, gestor_prenda, gestor_outfit):
        self.gestor_prenda= gestor_prenda
        self.gestor_outfit= gestor_outfit

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

    def seleccionar_prendas_para_outfit(self, id_usuario):

        prendas= self.gestor_prenda.prenda_dao.obtener_todas_las_prendas(id_usuario)

        ventana= tk.Tk()
        ventana.title("seleccionar prendas para Outfit")
        seleccionadas= []

        for prenda in prendas:
            nombre_prenda= prenda.get("nombre_prenda")
            imagen_prenda= prenda.get("imagen_prenda")

        
            try:
                if imagen_prenda:
                    imagen= Image.open(imagen_prenda)

                else:
                    imagen= Image.open(r"C:\Users\USUARIO\Desktop\PROYECTO\imagen_predeterminada.jpg")


                imagen.thumbnail((80, 80))
                imagen_tk = ImageTk.PhotoImage(imagen)

                var = tk.BooleanVar()
                chk= tk.Checkbutton(ventana, text= nombre_prenda, variable=var, image=imagen_tk, compound='left')
                chk.image= imagen_tk
                chk.pack()

                seleccionadas.append((var, prenda))
            except Exception as e:
                print(f"Error al cargar la imagen {imagen_prenda}: {e}")

            
        btn_confirmar= tk.Button(ventana, text="Confirmar seleccion", command=lambda: self.mostrar_prendas_seleccionadas(ventana, seleccionadas, id_usuario))
        btn_confirmar.pack()

        ventana.mainloop()


    def mostrar_prendas_seleccionadas(self, ventana_anterior, seleccionadas, id_usuario):
        ventana_anterior.destroy()


        ventana_outfit= tk.Toplevel()
        ventana_outfit.title("prenda seleccionadas para el outfit")
        tk.Label(ventana_outfit, text="prendas selecionadas", font=("Arial", 12, "bold")).pack(pady=10)

        for var, prenda in seleccionadas:
            if var.get():
                nombre_prenda= prenda[0]
                imagen_prenda= prenda[1]

                try:
                    imagen= Image.open(imagen_prenda)
                    imagen.thumbnail((100,100))
                    imagen_tk= ImageTk.PhotoImage(imagen)

                    label_imagen = tk.Label(ventana_outfit, image=imagen_tk)
                    label_imagen.image= imagen_tk
                    label_imagen.pack(pady= 5)
                    tk.Label(ventana_outfit, text=nombre_prenda).pack()
                except Exception as e:
                    print(f"error al cargar la imagen{imagen_prenda}:{e}")

        btn_crear_outfit = tk.Button(
            ventana_outfit, text="crear outfit",
            command=lambda: self.crear_outfit( id_usuario, seleccionadas)
        )
        btn_crear_outfit.pack(padx=10)

    def crear_outfit(self, id_usuario, seleccionadas):

        if isinstance(id_usuario, list) and len(id_usuario)==1:
            id_usuario= id_usuario[0]

    
        ventana_nombre= tk.Toplevel()
        ventana_nombre.title("crear outfit")

        tk.Label(ventana_nombre, text="nombre del outfit: ").pack(pady=10)
        nombre_entery= tk.Entry(ventana_nombre)
        nombre_entery.pack(pady=10)

        def confirmar_creacion_de_outfit():

            nombre_outfit= nombre_entery.get()
            if not nombre_outfit or not any(var.get() for var, _ in seleccionadas):
                
                messagebox.showwarning("porfavor ingresa un nombre para el outfit. ")
                return

            prendas_seleccionadas =[prenda["id_prenda"] for var, prenda in seleccionadas if var.get()]
            

            self.gestor_outfit.crear_outfit(nombre_outfit, prendas_seleccionadas, id_usuario)
            ventana_nombre.destroy()
            messagebox.showinfo("Exito", "outfit  creado y guardado exitosamente. ")

            self.visualizar_outfit_completo(nombre_outfit, id_usuario)
        
        btn_confirmar_outfit_completo= tk.Button(ventana_nombre, text="crear outfit", command=confirmar_creacion_de_outfit)
        btn_confirmar_outfit_completo.pack(pady=10)
    
    def visualizar_outfit_completo(self, nombre_outfit,id_usuario):

        ventana_outfit= tk.Toplevel()
        ventana_outfit.title(f"vizualizacion del outfit {nombre_outfit}")
        tk.Label(ventana_outfit, text=f"Outfit: {nombre_outfit}", font=("Arial", 14, "bold")).pack(pady=10)
        
        id_outfit= self.gestor_outfit.outfit_dao.obtener_id_outfit_por_nombre(nombre_outfit)
        if not id_outfit:
            tk.Label(ventana_outfit, text="no se encontro el outfit seleccionado").pack(pady=10)
            return
        
        detalles_outfit= self.gestor_outfit.obtener_detalle_outfit(id_outfit, id_usuario)
        if not detalles_outfit:
            tk.Label(ventana_outfit, text="no se encontraron prendas para este outfit").pack(pady=5)
            return

        for detalle in detalles_outfit:
            tk.Label(ventana_outfit, text=f"prenda: {detalle['prenda']} - tipo: {detalle['tipo']}- color: {detalle['color']}").pack(pady=5)
            try:
                imagen = Image.open(detalle["imagen_path"])
                imagen.thumbnail((100,100))
                imagen_tk = ImageTk.PhotoImage(imagen)

                label_imagen= tk.Label(ventana_outfit, image=imagen_tk)
                label_imagen.image = imagen_tk
                label_imagen.pack(pady=5)
            except Exception as e:
                print(f"Error al cargar la imagen{detalle['imagen_path']}: {e}")
                
            
 
        ventana_outfit.mainloop()
           
            

    

        


        


