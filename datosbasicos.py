from customtkinter import *
from PIL import Image





ventanitaa=CTk(fg_color="white")
ventanitaa.title("actualizacion datos basicos")
ventanitaa.geometry("900x500")
ventanitaa.resizable(False,False)

cuadrito = CTkFrame(
    master=ventanitaa,
    width=900,
    height=120,
    fg_color="#f5cac3",
    border_width=5,
    border_color="#fb6f92"

)

cuadrito.place(x=0, y=0)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Actualización de datos basicos",
    text_color="black",
    font=("Ready For Fall", 30)
)
titulo.place(x=220, y=40) 




formularioIm = Image.open("C:\\Users\\linit\\OneDrive\Escritorio\\proyectoIpsKLYV\\hp.png")
formularioIm = formularioIm.resize((100, 100))
imagen = CTkImage(light_image=formularioIm, size=(100, 100))

lblformulario = CTkLabel(
    master=cuadrito, 
    image=imagen,
    text=""
)
lblformulario.place(x=40, y=10)

class Update(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20))
        tituloE.place(x=20,y=12)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2)
        self.caja.place(x=20,y=50)

    # def getCaja(self):
    #     return self.caja.get()


class Box(CTkFrame):
    def __init__(self, master, titulo,ancho,largo,opciones,largo2):
        super().__init__(master,width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        ttlo=CTkLabel(self,text=self.titulo,font=("coolvetica rg",20))
        ttlo.place(x=30,y=12)
        self.combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18))
        self.combo.place(x=20,y=50)



nombres=Update(ventanitaa,"Nombres completos",280,100,250)
nombres.place(x=50,y=140)

tip_doc=Box(ventanitaa, "Tipo de documento:", 280, 100, ["CC", "TI"], 200)
tip_doc.place(x=340,y=140)

direccion=Update(ventanitaa,"Direccion",280,100,200)
direccion.place(x=590,y=140)

telefono=Update(ventanitaa,"Telefono",280,100,200)
telefono.place(x=50,y=250)

email=Update(ventanitaa,"Email",280,100,200)
email.place(x=340,y=250)

especialidad=Update(ventanitaa,"Especialidad",280,100,200)
especialidad.place(x=590,y=250)


botonS=CTkButton(ventanitaa,width=300,height=50,fg_color="#deaaff",border_width=3,border_color="#5a189a",text="Actualizar",font=("Ready For Fall",20),text_color="black")
botonS.place(x=300,y=400)

# identificacion=Ob(ventana,"numero de identificacion:",280,100,200)
# identificacion.place(x=30,y=140)

ventanitaa.mainloop()