from typing import Any, Tuple
from customtkinter import *
from PIL import Image



def Salir():
    ventana.destroy()
ventana = CTk(fg_color="white")
ventana.title("personal medico")
ventana.geometry("1250x500")


cuadrito = CTkFrame(
    master=ventana,
    width=1250,
    height=120,
    fg_color="#f5cac3",
    border_width=5,
    border_color="#fb6f92"

)

cuadrito.place(x=0, y=0)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Menu principal",
    text_color="black",
    font=("Ready For Fall", 30)
)
titulo.place(x=500, y=40) 




formularioIm = Image.open("C:\\Users\\linit\\OneDrive\Escritorio\\proyectoIpsKLYV\\hp.png")
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

    #     self.bind("<Button-1>", self.jajnxsj)




    # def jajnxsj(self, event):
    #     print("Frame clicked!")
    
    #     file_path = "C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\main.py"
    #     os.system(f'python "{file_path}"')









        
boton=CTkButton(ventana,width=300,height=50,border_width=5,border_color="#7209b7",fg_color="#e7c6ff",text="Salir",text_color="black",font=("Ready For Fall",20),command=lambda:Salir())
boton.place(x=470,y=400)

jose=Menu(ventana,"Registrar personal medico",350,170,"C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\frm2.png")
jose.place(x=50,y=150)

martha=Menu(ventana,"Consultar hoja de vida",350,170,"C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\fml m.png")

martha.place(x=450,y=150)

eduardo=Menu(ventana,"Actualizar hoja de vida",350,170,"C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\eduardo.png")
eduardo.place(x=850,y=150)


ventana.mainloop()