from typing import Any, Tuple
from customtkinter import *
from tkinter import *
import customtkinter as ctk
from tkcalendar import *
from clases.paciente import Paciente
# from clases.conexion import *

# app =CTk()
# app.geometry("800x600")


# frame1 = CTkFrame(app, width=900, height=100, fg_color="white")
# frame1.place(x=0, y=0)
# app.title("Historia Clínica")

# titulo = CTkLabel(frame1, text="Historia Clínia", text_color= "#16425b", font=("Ready For Fall", 30))
# titulo.place(x=350, y=50)

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


# vi = Tk()
# vi.geometry("1240x690")
# vi.resizable(width=0,height=0)
      
    
# vIndex = CTkFrame(vi,fg_color='white',width=1060,height=590)
# vIndex.place(x=100,y=30)
# txtRegistro = CTkLabel(vIndex,text="Registrar paciente",text_color="black", fg_color="white", font=("212 Moon Child Sans", 40))
# txtRegistro.place(x=390,y=20)
# entTpDoc = EntradasCombo(vIndex,"Tipo de documento",["seleccione",'Cedula de ciudadania','Tarjeta de identidad','Cedula de extrangeria','Registro civil'])
# entTpDoc.place(x=100,y=100)
# entNoDoc = EntradasTexto(vIndex,"Numero de documento")
# entNoDoc.place(x=390,y=100)
# entfExp = EntradaCal(vIndex,"Fecha de expedicion")
# entfExp.place(x=680,y=100)
# entLExp = EntradasTexto(vIndex,'Lugar de expedicion')
# entLExp.place( x=100,y=166)
# entNomb = EntradasTexto(vIndex,"Nombres")
# entNomb.place(x=390,y=166)
# entApe1 = EntradasTexto(vIndex,"Apellido1")
# entApe1.place(x=680,y=166)
# entApe2 = EntradasTexto(vIndex,"Apellido2")
# entApe2.place(x=100,y=232)
# entfnac = EntradaCal(vIndex,"Fecha de nacimiento")
# entfnac.place(x=390,y=232)
# entGenero = EntradasCombo(vIndex,'Genero',["seleccione",' Heterosexual','Gay',' Lesbiana','Bisexual'])
# entGenero.place(x=680,y=232)
# entSex = EntradasCombo(vIndex,'Sexo',["seleccione","Masculino","Femenino"])
# entSex.place(x=100,y=298)
# entCelular = EntradasTexto(vIndex,'Telefono')
# entCelular.place(x=390,y=298)
# entEmail = EntradasTexto(vIndex,'Correo electronico')
# entEmail.place(x=680,y=298)  
# enRh = EntradasTexto(vIndex, "RH")
# enRh.place(x=100,y=364)
# entEcivil = EntradasCombo(vIndex,'Estado civil',["seleccione","Soltero/a","Casado/a","Divorciado/a","Viudo/a","Unión libre","Separado/a"])
# entEcivil.place(x=390,y=364)
# entTAEs = EntradasCombo(vIndex,"Tipo de atencion especial",["seleccione","Adultos mayores"," Población habitante de calle", "Comunidades indígenas", " Víctimas del conflicto armado" ])
# entTAEs.place(x=680, y=364)
# entOcup = EntradasTexto(vIndex, "Ocupación")
# entOcup.place(x=100,y=426)
# entTipoAf =EntradasCombo(vIndex, "Tipo de afiliacion", ["seleccione","Cotizante", "Beneficiario"])
# entTipoAf.place(x=390,y=426)
# entRegi = EntradasCombo(vIndex, "Régimen", ["seleccione","Contributivo", "Subsidiado"])
# entRegi.place(x=680,y=426)
# entEst = EntradasCombo(vIndex,'Estrato',['seleccione','uno','dos', 'tres', 'cuatro', 'cinco', 'seis'])
# entEst.place(x=100, y=490)
# entEps = EntradasTexto(vIndex,'Eps')
# entEps.place(x=390, y=490)  
# entNacio = EntradasCombo(vIndex,"Nacionalidad",["Colombiana","Argentina","Brasileña","Chilena","Ecuatoriana","Peruana","Venezolana","Uruguaya","Boliviana","Paraguaya","Panameña","Costarricense","Nicaragüense","Hondureña","Salvadoreña","Guatemalteca","Mexicana","Cubana","Dominicana","Puertorriqueña","Española","Estadounidense"]) 
# entNacio.place(x=680, y=490)  

# paciente = None

# def registrarPaciente():
#     global paciente
#     paciente = Paciente(entTpDoc.getter(),
#                       entNoDoc.getter(),
#                       entfExp.getter(),
#                       entLExp.getter(),
#                       entNomb.getter(),
#                       entApe1.getter(),
#                       entApe2.getter(),
#                       entfnac.getter(),
#                       entGenero.getter(),
#                       entSex.getter(),
#                       entCelular.getter(),
#                       entEmail.getter(),
#                       enRh.getter(),
#                       entEcivil.getter(),
#                       entTAEs.getter(),
#                       entOcup.getter(), 
#                       entTipoAf.getter(), 
#                       entRegi.getter(),
#                       entEst.getter(),
#                       entEps.getter(),
#                       entNacio.getter()
#                       ) 
#     print(paciente.getEps())
    
 
# def EviarBD(objeto):
#     archivo = llenarArchivoPa(objeto)
#     paci.insert_one(archivo)
    
    
def registrarHistoria():
    ventana = CTk() 
    ventana.geometry("900x600") 
    frame = ctk.CTkFrame(ventana, fg_color= "white", width=850, height=550) 
    frame.place(x=20, y=20)
    botonAnan = ctk.CTkButton(frame, text= "Anamnesis",command= lambda:abrirAnamnesis())
    botonAnan.place(x=100, y=400)
    boton = ctk.CTkButton(frame, text='Fórmula Médica', command=lambda: abrirFormula())
    boton.place(x=300,y=400)
    botonSoli =ctk.CTkButton(frame, text= "Solicitud de Servicios", command= lambda:solicitudServicios())
    botonSoli.place(x=500,y=400)
    
    def abrirAnamnesis():
        vi = ctk.CTkToplevel(fg_color="white")
        vi.geometry("1300x700")
        vi.resizable(width=0,height=0)  
        titulo= ctk.CTkLabel(vi, text="Anamnesis", text_color="black",fg_color="white", font=("212 Moon Child Sans", 50))
        titulo.place(x=600, y=30)

        vIndex = ctk.CTkFrame(vi,fg_color='white',width=400,height=500,border_width=5,border_color="black")
        vIndex.place(x=30,y=100)
        txtRegistro = ctk.CTkLabel(vIndex,text="Consulta",text_color="black",fg_color="#fea6a2", font=("212 Moon Child Sans", 20))
        txtRegistro.place(x=200,y=34)  
        motivo_consulta= EntradasTexto(vIndex, "Motivo de la consulta")
        motivo_consulta.place(x=50, y=100)
        enfermedad_actual = EntradasTexto(vIndex, "Enfermedad actual")
        enfermedad_actual.place(x=50, y=180)
        fecha_consulta = EntradaCal(vIndex, "Fecha de la consulta")
        fecha_consulta.place(x=50, y=260)
        anexo = EntradasTexto(vIndex, "Anexo")
        anexo.place(x=50,y=340)
        medico_consulta = EntradasTexto(vIndex, "Médico consulta")
        medico_consulta.place(x=50, y=420)

        veIndex = ctk.CTkFrame(vi,fg_color='white',width=400,height=500, border_width=5,border_color="black")
        veIndex.place(x=450,y=100)
        txtRegistro = ctk.CTkLabel(veIndex,text="Antecedentes Personales",text_color="black",fg_color="#fea6a2", font=("212 Moon Child Sans", 20))
        txtRegistro.place(x=180,y=34)
        alergias = EntradasTexto(veIndex, "Alergias")
        alergias.place(x=50, y=100)
        enfer = EntradasTexto(veIndex, "Enfermedades")
        enfer.place(x=50, y=180)
        ciru = EntradasTexto(veIndex, "Cirugías")
        ciru.place(x=50, y=260)

        venIndex = ctk.CTkFrame(vi,fg_color='white',width=400,height=500, border_width=5,border_color="black")
        venIndex.place(x=870,y=100)
        txtRegistro = ctk.CTkLabel(venIndex,text="Antecedentes Familiares",text_color="black",fg_color="#fea6a2", font=("212 Moon Child Sans", 20))
        txtRegistro.place(x=150,y=34)
        alergias = EntradasTexto(venIndex, "Alergias")
        alergias.place(x=50, y=100)
        enfer = EntradasTexto(venIndex, "Enfermedades")
        enfer.place(x=50, y=180)



        boton = ctk.CTkButton(vi, text= "Guardar")
        boton.place(x=1000, y=650)


        vi.mainloop() 
                
        
           
    def abrirFormula():
        vi = ctk.CTkToplevel()
        vi.geometry("700x600")
        vi.resizable(width=0,height=0)  

        vIndex = ctk.CTkFrame(vi,fg_color='white',width=660,height=560)
        vIndex.place(x=30,y=30)
        txtRegistro = ctk.CTkLabel(vIndex,text="Fórmula Medica",text_color="black",fg_color="white", font=("212 Moon Child Sans", 20))
        txtRegistro.place(x=200,y=34)  
        medicamento = EntradasTexto(vIndex, "Medicamento")
        medicamento.place(x=50, y=100)
        concentracion = EntradasTexto(vIndex, "Concentracion")
        concentracion.place(x=360, y=100)
        forma_farmaceutica = EntradasTexto(vIndex, "forma Farmacéutica")
        forma_farmaceutica.place(x=50, y=180)
        dosis = EntradasTexto(vIndex, "Dosis")
        dosis.place(x=360,y=180)
        Via_admin = EntradasTexto(vIndex, "Vía de administración")
        Via_admin.place(x=50, y=260)
        frecuencia = EntradasTexto(vIndex, "Frecuencia")
        frecuencia.place(x=360, y=260)
        tiempo_tto = EntradasTexto(vIndex, "Tiempo de tratamiento")
        tiempo_tto.place(x=50, y=340)
        cantidad = EntradasTexto(vIndex, "Cantidad")
        cantidad.place(x=360, y=340)
        cantidad_letras = EntradasTexto(vIndex, "Cantidad en letras")
        cantidad_letras.place(x=50, y=420)
        posologia =EntradasTexto(vIndex, "Posología")
        posologia.place(x=360, y=420)
        recomenda = EntradasTexto(vIndex, "Recomendaciones")
        recomenda.place(x=50, y=500)


        boton = ctk.CTkButton(vIndex, text= "Guardar")
        boton.place(x=500, y=520)


        vi.mainloop() 
        
        
    def solicitudServicios():
        vi = ctk.CTkToplevel()
        vi.geometry("700x540")
        vi.resizable(width=0,height=0)  

        vIndex = ctk.CTkFrame(vi,fg_color='white',width=660,height=560)
        vIndex.place(x=30,y=30)
        txtRegistro = ctk.CTkLabel(vIndex,text="Solicitud de Servicios",text_color="black",fg_color="white", font=("212 Moon Child Sans", 20))
        txtRegistro.place(x=200,y=34)  
        codigo = EntradasTexto(vIndex, "Codigo")
        codigo.place(x=50, y=100)
        cups = EntradasTexto(vIndex, "Cups")
        cups.place(x=360, y=100)
        descripcion = EntradasTexto(vIndex, "Descripcion")
        descripcion.place(x=50, y=180)
        cantidad = EntradasTexto(vIndex, "Cantidad")
        cantidad.place(x=360,y=180)
        observacion = EntradasTexto(vIndex, "Observacion")
        observacion.place(x=50, y=260)
        estado = EntradasTexto(vIndex, "Estado")
        estado.place(x=360, y=260)
        medico = EntradasTexto(vIndex, "Medico")
        medico.place(x=50, y=340)
        especialidad = EntradasTexto(vIndex, "Especialidad")
        especialidad.place(x=360, y=340)
                


        boton = ctk.CTkButton(vIndex, text= "Guardar")
        boton.place(x=500, y=450)





        vi.mainloop() 
    
        
    
    
    ventana.mainloop()
registrarHistoria()
    


# boton = ctk.CTkButton(vIndex, text= "Guardar", command= lambda:[registrarPaciente(), EviarBD(paciente)])
# boton.place(x=850, y=560)






# def saludar():
#     print("Hola kenen")
#     opcion1.destroy()        
        
# opcion1 = Cuadros(app, "Crear Historia")
# opcion1.place(x=200, y=200)

# opcion2 = Cuadros(app, "Consultar Historia")
# opcion2.place(x=500, y=200)
# opcion2.bind("<Button-1>", lambda v:saludar())

# opcion3 = Cuadros(app, "Salir")
# opcion3.place(x=500, y=450)
        








# app.mainloop()