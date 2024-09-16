from customtkinter import *
from PIL import Image
from tkcalendar import *


ventana=CTk(fg_color="white")
ventana.title("Formulario solicitud de actualizacion")
ventana.geometry("950x700")
ventana.resizable(False,False)

cuadrito = CTkFrame(
    master=ventana,
    width=950,
    height=120,
    fg_color="#a9def9",
    border_width=5,
    border_color="#17c3b2"

)

cuadrito.place(x=0, y=0)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Formulario Solicitud de actualizacion",
    text_color="black",
    font=("Ready For Fall", 30)
)
titulo.place(x=200, y=40) 




formularioIm = Image.open("C:\\Users\\linit\\OneDrive\Escritorio\\proyectoIpsKLYV\\hp.png")
formularioIm = formularioIm.resize((100, 100))
imagen = CTkImage(light_image=formularioIm, size=(100, 100))

lblformulario = CTkLabel(
    master=cuadrito, 
    image=imagen,
    text=""
)
lblformulario.place(x=40, y=10)

class Ob(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20))
        tituloE.place(x=20,y=12)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2)
        self.caja.place(x=20,y=50)


class ComboB(CTkFrame):
    def __init__(self, master, titulo,ancho,largo,opciones,largo2):
        super().__init__(master,width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        ttlo=CTkLabel(self,text=self.titulo,font=("coolvetica rg",20))
        ttlo.place(x=30,y=12)
        self.combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18))
        self.combo.place(x=20,y=50)



identificacion=Ob(ventana,"numero de identificacion:",280,100,200)
identificacion.place(x=30,y=140)

tip_doc=ComboB(ventana, "Tipo de documento:", 280, 100, ["CC", "TI"], 200)
tip_doc.place(x=330,y=140)

nombres=Ob(ventana,"Nombres completos",280,100,250)
nombres.place(x=630,y=140)

apellido1=Ob(ventana,"Apellido 1:",280,100,200)
apellido1.place(x=30,y=260)

apellido2=Ob(ventana,"Apellido 2:",280,100,200)
apellido2.place(x=330,y=260)

especialidad=Ob(ventana,"Especialidad:",280,100,200)
especialidad.place(x=630,y=260)


cuadrito = CTkFrame(
    master=ventana,
    width=950,
    height=50,
    fg_color="#fcd5ce",
    border_width=5,
    border_color="#ff7096"

)

cuadrito.place(x=0, y=400)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Datos de la solicitud",
    text_color="black",
    font=("Ready For Fall", 20)
)
titulo.place(x=350, y=10)

class Date(CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master, width=250, height=250, fg_color="white")
        self.titulo = titulo
    
        ttlD = CTkLabel(self, text=self.titulo, font=("coolvetica rg", 20))
        ttlD.place(x=20,y=12)
        
        self.j = DateEntry(self, width=20, background='#ff477e', foreground='black', borderwidth=2, font=('coolvetica rg', 12))
        self.j.place(x=20,y=60)

fecha=Date(ventana,"Fecha de la solicitud:")
fecha.place(x=50,y=470)

motivo=Ob(ventana,"Motivo de la solicitud:",280,100,200)
motivo.place(x=330,y=470)

soporte=Ob(ventana,"Motivo de la solicitud:",280,100,200)
soporte.place(x=630,y=470)

botonS=CTkButton(ventana,width=300,height=50,fg_color="#deaaff",border_width=3,border_color="#5a189a",text="Enviar",font=("Ready For Fall",20),text_color="black")
botonS.place(x=300,y=600)





# tip_doc = Nopi(ventana, "Tipo de documento:", 230, 100, ["CC", "TI"], 200)
# tip_doc.place(x=30,y=180)

ventana.mainloop()

