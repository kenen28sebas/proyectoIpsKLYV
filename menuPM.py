from typing import Any, Tuple
from customtkinter import *
from PIL import Image

ventanita =CTk(fg_color="white")
ventanita.title("Menu personal medico")
ventanita.geometry("1250x500")
ventanita.resizable(False,False)
def salir():
    ventanita.destroy()

cuadrito = CTkFrame(
    master=ventanita,
    width=1250,
    height=120,
    fg_color="#f5cac3",
    border_width=5,
    border_color="#fb6f92"

)

cuadrito.place(x=0, y=0)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Menu principal personal medico",
    text_color="black",
    font=("Ready For Fall", 30)
)
titulo.place(x=400, y=40) 




formularioIm = Image.open("hp.png")
formularioIm = formularioIm.resize((100, 100))
imagen = CTkImage(light_image=formularioIm, size=(100, 100))

lblformulario = CTkLabel(
    master=cuadrito, 
    image=imagen,
    text=""
)
lblformulario.place(x=40, y=10)


class Menu(CTkFrame):


    def __init__(self, master,titulo,ancho,largo,imagen):
        super().__init__(master,width=ancho,height=largo,fg_color="#BBF5BF",border_color="#386641",border_width=5)
        self.titulo=titulo
        # self.titulo.place(x=50,y=45)
        image = Image.open(imagen)
        image = image.resize((100, 100)) 
        
        
        self.ctk_image = CTkImage(light_image=image, size=(100, 100))
        
    
        lblimg = CTkLabel(self, image=self.ctk_image, text="")
        lblimg.place(x=125, y=55)

        self.title_label = CTkLabel(self, text=titulo,font=("Ready For Fall",25))
        self.title_label.place(x=17, y=10)


opcion1=Menu(ventanita,"Consultar mi hoja de vida",350,170,"lupa.png")

opcion1.place(x=50,y=150)

opcion2=Menu(ventanita,"Solicitar Actualizacion",350,170,"update.png")
opcion2.place(x=450,y=150)

opcion3=Menu(ventanita,"Actualizar Datos Basicos",350,170,"update2.png")

opcion3.place(x=850,y=150)


botonS=CTkButton(ventanita,width=300,height=50,fg_color="#deaaff",border_width=3,border_color="#5a189a",text="salir",font=("Ready For Fall",20),text_color="black",command=lambda:salir())
botonS.place(x=500,y=400)
ventanita.mainloop()

    