from typing import Any, Tuple
from customtkinter import *
from tkcalendar import DateEntry
from tkcalendar import *


class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20))
        tituloE.place(x=20,y=0)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2)
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



ventana = CTk(fg_color="white")
ventana.title("personal medico")
ventana.geometry("700x700")





cuadrito=CTkFrame(
    master=ventana,
    width=700,
    height=150,
    fg_color="#44E3D3"

)

titulo=CTkLabel(
    master=cuadrito,
    text="Registro del Medico",
    text_color="black",
    font=("coolvetica rg",30)


)
titulo.place(x=220,y=50)
cuadrito.place(x=0,y=0)

cuadrito2=CTkFrame(
    master=ventana,
    width=250,
    height=100,
    fg_color="white"
)

text=CTkLabel(
    master=cuadrito2,
    text="Fecha de nacimiento:",
    text_color="black",
    font=("coolvetica rg",20)
)
text.place(x=20,y=5)

fecha_na=DateEntry(
    master=cuadrito2,
    width=30,
    background='#FF81D0',
    foreground='white', 
    borderwidth=6,
    border_color="#FF81D0",
    height=50
    
    
)
fecha_na.place(x=20,y=50)

cuadrito2.place(x=350,y=200)


# cuadrito.place(x=0,y=0)


# titulo.place(x=220,y=50)


nombre=Sipi(ventana,"Nombres completos:",250,100,200)
nombre.place(x=50,y=200)

apellido1=Sipi(ventana,"Apellido 1:",250,100,200)
apellido1.place(x=50,y=280)

apellido2=Sipi(ventana,"Apellido 2:",250,100,200)
apellido2.place(x=50,y=360)

identificacion=Sipi(ventana,"Numero identificacion:",250,100,200,)
identificacion.place(x=50,y=440)
identificacion.validar()


fecha_exp=Sipi(ventana,"Fecha expedicion:",250,100,200)
fecha_exp.place(x=50,y=520)

lugar_exp=Sipi(ventana,"Lugar expedicion:",250,100,200)
lugar_exp.place(x=50,y=600)

# fecha_na=Sipi(ventana,"Fecha de Nacimiento:",250,100,200)
# fecha_na.place(x=350,y=200)

genero=Sipi(ventana,"Genero:",250,100,200)
genero.place(x=350,y=280)

sexo=Sipi(ventana,"Sexo:",250,100,200)
sexo.place(x=350,y=360)

telefono=Sipi(ventana,"Telefono:",250,100,200)
telefono.place(x=350,y=440)
telefono.validar()

email=Sipi(ventana,"Email:",250,100,200)
email.place(x=350,y=520)

especialidad=Sipi(ventana,"Especialidad:",250,100,200)
especialidad.place(x=350,y=600)

def prueba (entrada):
    with open("datos.txt","a") as file:
        file.write(entrada.getEntri())

def hola ():
    print("hola suacha")

btn = CTkButton(ventana,text="vive la vida",command=lambda:prueba(nombre))
btn.place(x=0,y=0)

# ejemplo = Sipi(ventana,"lina la mas bonita",100,200)
# ejemplo.place(x=10,y=10)

# ejmeplo2 = CTkLabel(ventana,text="kenen es menos bonito que lina")
# ejmeplo2.place(x=10,y=50)

# ejmeplo3 = Sipi(ventana,"yhoneida no se baña",200,300)
# ejmeplo3.place(x=10,y=80)

ventana.mainloop()