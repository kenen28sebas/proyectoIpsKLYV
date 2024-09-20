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
    fg_color="#9ceaef",
    border_width=5,
    border_color="#118ab2"

)

cuadrito.place(x=0, y=0)  


titulo = CTkLabel(
    master=cuadrito, 
    text="Buscar hoja de vida",
    text_color="black",
    font=("Ready For Fall", 30)
)
titulo.place(x=280, y=40) 




<<<<<<< HEAD
formularioIm = Image.open("hp.png")
=======
formularioIm = Image.open("C:\\Users\\linit\\OneDrive\Escritorio\\proyectoIpsKLYV\\hp.png")
>>>>>>> 3639aeb3aa837912906f993307bed7f1f9b078e0
formularioIm = formularioIm.resize((100, 100))
imagen = CTkImage(light_image=formularioIm, size=(100, 100))

lblformulario = CTkLabel(
    master=cuadrito, 
    image=imagen,
    text=""
)
lblformulario.place(x=40, y=10)


frame2=CTkFrame(ventanitaa,width=500,height=200,fg_color="white")
frame2.place(x=50,y=200)

busqueda=CTkEntry(frame2,border_width=3,border_color="#a53860",placeholder_text="Numero de identificacion",width=200)
busqueda.place(x=0,y=0)

boton=CTkButton(frame2,border_width=3,border_color="#a53860",fg_color="#ff90b3",text="Buscar",text_color="black",font=("coolvetica rg",15))
boton.place(x=200,y=0)



ventanitaa.mainloop()