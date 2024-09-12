from typing import Any, Tuple
from customtkinter import *

class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20))
        tituloE.place(x=20,y=0)
        caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2)
        caja.place(x=20,y=30)


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

cuadrito.place(x=0,y=0)


titulo.place(x=220,y=50)


nombre=Sipi(ventana,"Nombres completos:",250,100,200)
nombre.place(x=50,y=200)

apellido1=Sipi(ventana,"Apellido 1:",250,100,200)
apellido1.place(x=50,y=280)

apellido2=Sipi(ventana,"Apellido 2:",250,100,200)
apellido2.place(x=50,y=360)

identificacion=Sipi(ventana,"Numero identificacion:",250,100,200)
identificacion.place(x=50,y=440)

fecha_exp=Sipi(ventana,"Fecha expedicion:",250,100,200)
fecha_exp.place(x=50,y=520)

lugar_exp=Sipi(ventana,"Lugar expedicion:",250,100,200)
lugar_exp.place(x=50,y=600)

fecha_na=Sipi(ventana,"Fecha de Nacimiento:",250,100,200)
fecha_na.place(x=350,y=200)

genero=Sipi(ventana,"Genero:",250,100,200)
genero.place(x=350,y=280)

sexo=Sipi(ventana,"Sexo:",250,100,200)
sexo.place(x=350,y=360)

telefono=Sipi(ventana,"Telefono:",250,100,200)
telefono.place(x=350,y=440)

email=Sipi(ventana,"Email:",250,100,200)
email.place(x=350,y=520)

especialidad=Sipi(ventana,"Especialidad:",250,100,200)
especialidad.place(x=350,y=600)



# ejemplo = Sipi(ventana,"lina la mas bonita",100,200)
# ejemplo.place(x=10,y=10)

# ejmeplo2 = CTkLabel(ventana,text="kenen es menos bonito que lina")
# ejmeplo2.place(x=10,y=50)

# ejmeplo3 = Sipi(ventana,"yhoneida no se baña",200,300)
# ejmeplo3.place(x=10,y=80)

ventana.mainloop()