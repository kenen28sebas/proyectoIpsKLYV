from typing import Any, Tuple
from customtkinter import *
from tkinter import *
import customtkinter as ctk
from tkcalendar import *

app =CTk()
app.geometry("800x600")


frame1 = CTkFrame(app, width=900, height=100, fg_color="white")
frame1.place(x=0, y=0)
app.title("Historia Clínica")

titulo = CTkLabel(frame1, text="Historia Clínia", text_color= "#16425b", font=("Ready For Fall", 30))
titulo.place(x=350, y=50)

class Cuadros(CTkFrame):
    def __init__(self, master, texto):
        super().__init__(master,width=200, height=110, border_width=3, border_color="#00b4d8", fg_color="#fed9b7", corner_radius=45 )
        self.titulo = CTkLabel(self, text= texto, text_color="#d80032", font=("Ready For Fall", 15))
        self.titulo.place(x=50 , y= 50)
        
class EntradasTexto (ctk.CTkFrame):
    
    def __init__(self, master,textoLBL):
        super().__init__(master,width=280,height=54,fg_color="transparent")
        self.textoLBL = textoLBL
        self.texto()
        self.boxTex()

    def texto (self):
        self.lbltexto = ctk.CTkLabel(self, text=self.textoLBL, bg_color="transparent", font=("212 Moon Child Sans", 20),text_color='black')
        self.lbltexto.place(x=0, y=-2)

    def boxTex (self):
        self.boxTexto = ctk.CTkEntry(self,fg_color='white',width=275,text_color='black')
        self.boxTexto.place(x=0, y=20)
    def getter (self):
        return self.boxTexto.get()
    
class EntradasCombo (ctk.CTkFrame):
    
    def __init__(self, master,textoLBL,contenido):
        super().__init__(master,width=280,height=100,fg_color='white')
        self.textoLBL = textoLBL
        self.contenido = contenido
       
        self.texto()
        self.comboBox()

    def texto (self):
        self.lbltexto = ctk.CTkLabel(self, text=self.textoLBL, bg_color="transparent", font=("212 Moon Child Sans", 20),text_color='black')
        self.lbltexto.place(x=0, y=0)

    def comboBox (self):
        self.boxTexto = ctk.CTkComboBox(self,fg_color='white',width=275,text_color='black',values=self.contenido)
        self.boxTexto.place(x=0, y=20)
    def getter (self):
        return self.boxTexto.get()
        
class EntradaCal (ctk.CTkFrame):
    def __init__(self, master,textoLBL):
        super().__init__(master,width=280,height=100,fg_color='white')
        self.textoLBL = textoLBL
        self.texto()
        self.calendario()
    def texto (self):
        self.lbltexto = ctk.CTkLabel(self, text=self.textoLBL, bg_color="transparent", font=("212 Moon Child Sans", 20),text_color='black')
        self.lbltexto.place(x=0, y=0)
    def calendario (self):
        self.contenedor = ctk.CTkFrame(self,width=275,height=30,corner_radius=5,border_color='black',fg_color='white',border_width=2)
        self.contenedor.place(x=0,y=18)
        self.entry_fecha_nacimiento = DateEntry(self, width=41,height=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')    
        self.entry_fecha_nacimiento.place(x=2, y=22)
    def getter (self):
        return self.entry_fecha_nacimiento.get()


vIndex = Tk()
vIndex.geometry("1240x690")
vIndex.resizable(width=0,height=0)
      
    
vformuario = CTkFrame(vIndex,fg_color='white',width=1060,height=530)
vformuario.place(x=100,y=126)
txtRegistro = CTkLabel(vIndex,text="Registrar paciente",text_color="black",fg_color="white")
txtRegistro.place(x=490,y=134)
entTpDoc = EntradasCombo(vIndex,"Tipo de documento",["seleccione",'Cedula de ciudadania','Tarjeta de identidad','Cedula de extrangeria','Registro civil'])
entTpDoc.place(x=200,y=200)
entNoDoc = EntradasTexto(vIndex,"Numero de documento")
entNoDoc.place(x=490,y=200)
entfExp = EntradaCal(vIndex,"Fecha de expedicion")
entfExp.place(x=780,y=200)
entLExp = EntradasCombo(vIndex,'Lugar de expedicion',['s','d'])
entLExp.place( x=200,y=266)
entNomb = EntradasTexto(vIndex,"Nombres")
entNomb.place(x=490,y=266)
entApel = EntradasTexto(vIndex,"Apellido1")
entApel.place(x=780,y=266)
entApel = EntradasTexto(vIndex,"Apellido2")
entApel.place(x=200,y=332)
entfnac = EntradaCal(vIndex,"Fecha de nacimiento")
entfnac.place(x=490,y=332)
entGenero = EntradasCombo(vIndex,'Genero',["seleccione",'nose','nose','nose'])
entGenero.place(x=780,y=332)
entSex = EntradasCombo(vIndex,'Sexo',["seleccione","Masculino","Femenino"])
entSex.place(x=200,y=398)
entCelular = EntradasTexto(vIndex,'Telefono')
entCelular.place(x=490,y=398)
entEmail = EntradasTexto(vIndex,'Correo electronico')
entEmail.place(x=780,y=398)  
enRh = EntradasTexto(vIndex, "RH")
enRh.place(x=200,y=464)
entEcivil = EntradasCombo(vIndex,'Estado civil',["seleccione","Soltero/a","Casado/a","Divorciado/a","Viudo/a","Unión libre","Separado/a"])
entEcivil.place(x=490,y=464)
entTAEs = EntradasCombo(vIndex,"Tipo de atencion especial",["seleccione","Adultos mayores"," Población habitante de calle", "Comunidades indígenas", " Víctimas del conflicto armado" ])
entTAEs.place(x=780, y=464)
entOcup = EntradasTexto(vIndex, "Ocupación")
entOcup.place(x=200,y=526)
entTipoAf =EntradasCombo(vIndex, "Tipo de afiliacion", ["seleccione","Cotizante", "Beneficiario"])
entTipoAf.place(x=490,y=526)
entRegi = EntradasCombo(vIndex, "Régimen", ["seleccione","Contributivo", "Subsidiado"])
entRegi.place(x=780,y=526)
entEst = EntradasCombo(vIndex,'Estrato',['seleccione','uno','dos', 'tres', 'cuatro', 'cinco', 'seis'])
entEst.place(x=200, y=590)
entDirec = EntradasTexto(vIndex,'Eps')
entDirec.place(x=490, y=590)  
entPais = EntradasCombo(vIndex,"Nacionalidad",["Colombiana","Argentina","Brasileña","Chilena","Ecuatoriana","Peruana","Venezolana","Uruguaya","Boliviana","Paraguaya","Panameña","Costarricense","Nicaragüense","Hondureña","Salvadoreña","Guatemalteca","Mexicana","Cubana","Dominicana","Puertorriqueña","Española","Estadounidense"]) 
entPais.place(x=780, y=590)       
   
 
  
   
        

def saludar():
    print("Hola kenen")
    opcion1.destroy()        
        
opcion1 = Cuadros(app, "Crear Historia")
opcion1.place(x=200, y=200)

opcion2 = Cuadros(app, "Consultar Historia")
opcion2.place(x=500, y=200)
opcion2.bind("<Button-1>", lambda v:saludar())

opcion3 = Cuadros(app, "Salir")
opcion3.place(x=500, y=450)
        








app.mainloop()