from typing import Any, Tuple
from customtkinter import *
from PIL import Image
from tkcalendar import *


def main():
    ventana=CTk(fg_color="white")
    ventana.title ("Menu principal del paciente")
    ventana.geometry("900x500")


    frametl=CTkFrame(ventana,width=900,height=130,border_color="#5603ad",fg_color="#c2f8cb",border_width=5)
    frametl.place(x=0,y=0)

    tituloframe=CTkLabel(frametl,text="Menu principal",font=("Ready For Fall",30),text_color="black")
    tituloframe.place(x=350,y=30)









        


    opcion1=Opciones(ventana,"Crear Historia","carlos.png")
    opcion1.place(x=50,y=180)
    opcion1.bind("<Button-1>",lambda v:RegistrarHC())

    opcion2=Opciones(ventana,"Consultar HC","buscar.png")
    opcion2.place(x=500,y=180)
    

    def RegistrarHC():
        opcion1.destroy()
        opcion2.destroy()
        frametl.destroy()

        ventana.geometry("900x700")

        frameob=CTkFrame(ventana,width=900,height=650,border_color="black",border_width=5,fg_color="white")
        frameob.place(x=0,y=120)

        frmtitulo=CTkFrame(ventana,width=900,height=120,border_width=5,border_color="#00c49a",fg_color="#72ddf7")
        frmtitulo.place(x=0,y=0)

        lbltitulo=CTkLabel(frmtitulo,text="Registrar Historia Clinica",font=("Ready For Fall",30))
        lbltitulo.place(x=150,y=30)

        tip_doc=Nopi(frameob,"Tipo de documento:", 230, 100, ["CC", "TI","Cedula de extrangeria","Registro civil"], 200)
        tip_doc.place(x=50,y=20)


        numero_id=Sipi(frameob,"Numero de identificación:",270,80,200)
        numero_id.place(x=300,y=20)

        fecha_exp=Date(frameob,"Fecha de Expedición:")
        fecha_exp.place(x=580,y=20)

        nombres=Sipi(frameob,"Nombres Completos",270,80,200)
        nombres.place(x=50,y=120)

        apllido1=Sipi(frameob,"Apellido 1:",270,80,200)
        apllido1.place(x=300,y=120)

        apllido2=Sipi(frameob,"Apellido 2:",270,80,200)
        apllido2.place(x=580,y=120)

        fecha_nc=Date(frameob,"Fecha de nacimiento")
        fecha_nc.place(x=50,y=220)

        email=Sipi(frameob,"Email",270,80,200)
        email.place(x=300,y=220)

        telefono=Sipi(frameob,"Telefono",270,80,200)
        telefono.place(x=50,y=220)

        sexo = Nopi(frameob, "Sexo:", 250, 100, ["Masculino","Femenino"],200)
        sexo.place(x=580,y=220)

        genero = Nopi(frameob, "Género:", 250, 100, ["Hetero","Gay","Lesbiana","Bisexual"], 200)
        genero.place(x=50,y=320)

        rh=Sipi(frameob,"Tipo de sangre:",270,80,200)
        rh.place(x=300,y=320)

        tpAtencion=Nopi(frameob,"Tipo de Atención especial",280,100,["seleccione","Adultos mayores"," Población habitante de calle", "Comunidades indígenas", " Víctimas del conflicto armado" ],200)
        tpAtencion.place(x=580,y=320)

        ocupacion=Sipi(frameob,"Ocupacion",270,80,200)
        ocupacion.place(x=50,y=420)

        tpafiliacion=Nopi(frameob,"Tipo de afiliación",250,100,["seleccione","Cotizante", "Beneficiario"],200)
        tpafiliacion.place(x=300,y=420)

        regimen =Nopi(frameob,"Regimen",280,100,["seleccione","Contributivo", "Subsidiado"],200)
        regimen.place(x=580,y=420)


        

    
    ventana.mainloop()


class Opciones(CTkFrame):


    def __init__(self, master,titulo,imagen):
        super().__init__(master,width=300,height=180,fg_color="#bdb2ff",border_color="#0582ca",border_width=5)
        self.titulo=titulo
        # # self.titulo.place(x=50,y=45)
        image = Image.open(imagen)
        image = image.resize((100, 100)) 
        
        
        self.ctk_image = CTkImage(light_image=image, size=(100, 100))
        
    
        lblimg = CTkLabel(self, image=self.ctk_image, text="")
        lblimg.place(x=100, y=55)

        self.title_label = CTkLabel(self, text=titulo,font=("Ready For Fall",25))
        self.title_label.place(x=60, y=10)



class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("Ready For Fall",20),text_color="black")
        tituloE.place(x=20,y=12)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2,fg_color="white",text_color="black")
        self.caja.place(x=20,y=50)
    def getEntri(self):
        return self.caja.get()
    







class Nopi(CTkFrame):
    def __init__(self, master, titulo,ancho,largo,opciones,largo2):
        super().__init__(master,width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        ttlo=CTkLabel(self,text=self.titulo,font=("Ready For Fall",20))
        ttlo.place(x=20,y=12)
        self.combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18),dropdown_fg_color="#fae0e4",button_hover_color="#ff7096",button_color="#e7c6ff")
        self.combo.place(x=20,y=50)

    def getEntri(self):
        return self.combo.get()
    





class Date(CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master, width=250, height=100, fg_color="white")
        self.titulo = titulo
    
        ttlD = CTkLabel(self, text=self.titulo, font=("Ready For Fall", 20))
        ttlD.place(x=20,y=12)
        
        self.j = DateEntry(self, width=20, background='#ff8fab', foreground='black', borderwidth=3, font=('Papernotes', 12))
        self.j.place(x=40,y=70)
    def getEntri(self):
        return self.j.get()




main()
    