# from typing import Any, Tuple
# # from PIL import Image,ImageTk
# from customtkinter import *
# from tkcalendar import *
# from tkcalendar import *


# ventana = CTk(fg_color="white")
# ventana.title("personal medico")
# ventana.geometry("800x900")


# barra=CTkScrollableFrame(master=ventana,width=770,height=630,fg_color="white",corner_radius=5)
# barra.place(x=0,y=150)


# class OpcionesBig(CTkButton):
#     def __init__(self, master, titulo, evento):
#         super().__init__(master, text=titulo, width=200, height=200, command=evento)
#         self.lbl = CTkLabel(self, text=titulo)
#         self.lbl.place(x=100,y=200)
        

# class Usuario(CTkButton):
#     def __init__(self, master, nombre,apelidos,nod,tipod,evento):
#         super().__init__(master, text="", width=300, height=80,command=evento)
#         self.lbln = CTkLabel(self,text="Nombre :")
#         self.lbln.place(x=20,y=10)
#         self.lblNombre = CTkLabel(self,text=nombre)
#         self.lblNombre.place(x=75,y=10)
        
#         self.lbla = CTkLabel(self,text="Apellido :")
#         self.lbla.place(x=20,y=30)
#         self.lblApellido = CTkLabel(self,text=apelidos)
#         self.lblApellido.place(x=75,y=30)
        
#         self.lbltd = CTkLabel(self,text="Tipo de documento:")
#         self.lbltd.place(x=20,y=50)
#         self.lbltipd = CTkLabel(self,text=tipod)
#         self.lbltipd.place(x=150,y=50)
        
#         self.lbld = CTkLabel(self,text="No.:")
#         self.lbld.place(x=170,y=50)
#         self.lblnd = CTkLabel(self,text=nod)
#         self.lblnd.place(x=200,y=50)


# class Sipi(CTkFrame):
#     def __init__(self, master,titulo,ancho,largo,largo2):
#         super().__init__(master, width=ancho,height=largo,fg_color="white")
#         self.titulo=titulo
#         tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20),text_color="black")
#         tituloE.place(x=20,y=0)
#         self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2,fg_color="white",text_color="black")
#         self.caja.place(x=20,y=30)

        
#         # self.caja = CTkEntry(self, border_color="#38184C", border_width=3, width=largo2)
#         # self.caja.place(x=20, y=30)

#     def getEntri(self):
#         return self.caja.get()
    


    



    


def validar (self):

    NumerosV = (self.register(self.numeros), '%P')
    self.caja.configure(validate='key', validatecommand=NumerosV)



def numeros (self,numeros):
    return (numeros.isdigit() and len(numeros) <= 10) or numeros == ""
    










# cuadrito = CTkFrame(
#     master=ventana,
#     width=800,
#     height=150,
#     fg_color="#cbf3f0",
#     border_width=5,
#     border_color="#2ec4b6"

# )

# cuadrito.place(x=0, y=0)  


# titulo = CTkLabel(
#     master=cuadrito, 
#     text="Registro del Médico",
#     text_color="black",
#     font=("coolvetica rg", 30)
# )
# titulo.place(x=280, y=50)  


# formularioIm = Image.open("C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\formulario.png")
# formularioIm = formularioIm.resize((100, 100))


# imagen = CTkImage(light_image=formularioIm, size=(100, 100))


# lblformulario = CTkLabel(master=cuadrito, image=imagen, text="")
# lblformulario.place(x=50, y=30)






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





# class Nopi(CTkFrame):
#     def __init__(self, master, titulo,ancho,largo,opciones,largo2):
#         super().__init__(master,width=ancho,height=largo,fg_color="white")
#         self.titulo=titulo
#         ttlo=CTkLabel(self,text=self.titulo,font=("coolvetica rg",18))
#         ttlo.place(x=20,y=12)
#         self.combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18))
#         self.combo.place(x=20,y=40)

#     def getEntri(self):
#         return self.combo.get()


# class Date(CTkFrame):
#     def __init__(self, master, titulo):
#         super().__init__(master, width=250, height=250, fg_color="white")
#         self.titulo = titulo
    
#         ttlD = CTkLabel(self, text=self.titulo, font=("coolvetica rg", 20))
#         ttlD.grid(row=1,column=1)
        
#         self.j = DateEntry(self, width=20, background='lightblue', foreground='black', borderwidth=2, font=('coolvetica rg', 12))
#         self.j.grid(row=2, column=1,pady=5)
#     def getEntri(self):
#         return self.j.get()
        
# class Calendario (CTkFrame):
#     def __init__(self, master):
#         super().__init__(master, width=1060, height=600, fg_color="white")
#         self.listaDias = CTkFrame(self,width=1020, height=50,corner_radius=0)
#         self.listaDias.place(x=20,y=0)
#         self.lblLunes = CTkLabel(self.listaDias,text="Lunes \n 5")
#         self.lblLunes.grid(row=0, column=1, pady=5,padx=50)
#         self.lblMartes = CTkLabel(self.listaDias,text="Martes")
#         self.lblMartes.grid(row=0, column=2, pady=5,padx=50)
#         self.lblMiercoles = CTkLabel(self.listaDias,text="Miercoles")
#         self.lblMiercoles.grid(row=0, column=3, pady=5,padx=50)
#         self.lblJueves = CTkLabel(self.listaDias,text="Jueves")
#         self.lblJueves.grid(row=0, column=4, pady=5,padx=50)
#         self.lblViernes = CTkLabel(self.listaDias,text="Viernes")
#         self.lblViernes.grid(row=0, column=5, pady=5,padx=50)
#         self.lblSabado = CTkLabel(self.listaDias,text="Sabado")
#         self.lblSabado.grid(row=0, column=6, pady=5,padx=50)
#         self.lblDomingo = CTkLabel(self.listaDias,text="Domingo")
#         self.lblDomingo.grid(row=0, column=7, pady=5,padx=50)
        
        




