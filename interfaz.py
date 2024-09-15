from typing import Any, Tuple
from PIL import Image,ImageTk
from customtkinter import *
from tkcalendar import *
from tkcalendar import *
from clases.th import *
from clases.personalM import *

ventana = CTk(fg_color="white")
ventana.title("personal medico")
ventana.geometry("800x900")

barra=CTkScrollableFrame(master=ventana,width=720,height=630,fg_color="white")
barra.place(x=50,y=150)





class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20),text_color="black")
        tituloE.place(x=20,y=0)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2,fg_color="white",text_color="black")
        self.caja.place(x=20,y=30)

        
        # self.caja = CTkEntry(self, border_color="#38184C", border_width=3, width=largo2)
        # self.caja.place(x=20, y=30)

    def getEntri(self):
        return self.caja.get()
    


    



    


    def validar (self):

        NumerosV = (self.register(self.numeros), '%P')
        self.caja.configure(validate='key', validatecommand=NumerosV)



    def numeros (self,numeros):
        return (numeros.isdigit() and len(numeros) <= 10) or numeros == ""
    



p1=TalentoH("cc",12548,"20-05-2024","Bogota","jose alberto","perez","caedenas","03-12-2005","indefinido","travesti","3115698569","kdjskdks@gmail.com")






cuadrito = CTkFrame(
    master=ventana,
    width=800,
    height=150,
    fg_color="#44E3D3"
)

cuadrito.place(x=0, y=0)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Registro del Médico",
    text_color="black",
    font=("coolvetica rg", 30)
)
titulo.place(x=280, y=50)  


formularioIm = Image.open("formulario.png")
formularioIm = formularioIm.resize((100, 100))
imagen = CTkImage(light_image=formularioIm, size=(100, 100))

lblformulario = CTkLabel(
    master=cuadrito, 
    image=imagen,
    text=""
)
lblformulario.place(x=50, y=30)



# hospital=Image.open("C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\hospital.png")
# hospital=hospital.resize((100,100))
# imagen2=CTkImage(light_image=hospital,size=(100,100))

# cuadrito2 = CTkFrame(
#     master=ventana,
#     width=100,
#     height=100,
#     fg_color="#44E3D3"
# )

# cuadrito2.place(x=400, y=300) 

# lblhosp=CTkLabel(
#     master=cuadrito2,
#     image=imagen2,
#     text=""

# )
# lblhosp.place(x=100,y=150)





class Nopi(CTkFrame):
    def __init__(self, master, titulo,ancho,largo,opciones,largo2):
        super().__init__(master,width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        ttlo=CTkLabel(self,text=self.titulo,font=("coolvetica rg",18))
        ttlo.place(x=20,y=12)
        combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18))
        combo.place(x=20,y=40)


class Date(CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master, width=250, height=250, fg_color="white")
        self.titulo = titulo
    
        ttlD = CTkLabel(self, text=self.titulo, font=("coolvetica rg", 20))
        ttlD.grid(row=1,column=1)
        
        self.j = DateEntry(self, width=20, background='lightblue', foreground='black', borderwidth=2, font=('coolvetica rg', 12))
        self.j.grid(row=2, column=1,pady=5)
        
        




