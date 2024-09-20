from interfaz import*
from clases.paciente import * 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["proyecto_kenenitos"]
persona = mydb["Persona"]
paciente = None
def llenarobPaciente():
    global paciente
    paciente = Paciente(paciente["tipo de identificacion"],
                        paciente["identificacion"],
                        paciente["fecha_exp"],
                        paciente["lugar_exp"],
                        paciente["nombres"],
                        paciente["apellido1"],
                        paciente["apellido2"],
                        paciente["fecha_nacimiento"],
                        paciente["genero"],
                        paciente["sexo"],
                        paciente["telefono"],
                        paciente["email"],
                        "","","","","","","","")
    print(paciente)
    


def buscarPaciente(master,noD,eventoP):
    try:
        
        busqueda = persona.find({"identificacion" : noD})
        global usuario
        usuario = Usuario(master,busqueda[0]["nombres"],busqueda[0]["apellido1"],busqueda[0]["identificacion"],busqueda[0]["tipo de identificacion"],eventoP)
        usuario.place(x=40,y=250)
        global paciente
        paciente = busqueda[0]
    except:
        usuario.destroy()
        tituloError = CTkLabel(vnVusuario,text="No se encontro el páciente")
        tituloError.place(x=150,y=250)

def opcionePaciente():
    global vnVusuario,ventana
    
    
    vnVusuario.destroy()

    op1 = OpcionesBig(secction1,"datos de el paciente",lambda:datosPaciente())
    op1.place(x=20,y=300)
    op2 = OpcionesBig(secction1,"consultar citas",lambda:consultarCitas())
    op2.place(x=320,y=300)
    op3 = OpcionesBig(secction1,"crear cita",lambda:crearCitas())
    op3.place(x=620,y=300)
    def datosPaciente():
        op1.destroy()
        op2.destroy()
        op3.destroy()
        sectionDatos = CTkFrame(secction1,width=860,height=410)
        sectionDatos.place(x=5,y=5)
    def consultarCitas():
        pass
    def crearCitas():
        global header
        op1.destroy()
        op2.destroy()
        op3.destroy()
        secction1.destroy()
        header.destroy()
        ventana.geometry("1100x650")
        
        header=CTkFrame(
            master=ventana,
            width=1100,
            height=100,
            fg_color="#44E3D3",
            corner_radius=0
        )
        header.place(x=0, y=0)
        secctionC=CTkFrame(master=ventana,
            width=1060,
            height=510,
            fg_color="#44E3D3")

        secctionC.place(x=20,y=120)
        agenda = Calendario(secctionC)
        agenda.place(x=0,y=0)
        
        
    

ventana = CTk(fg_color="white")

ventana.geometry("1000x650")



def prueba (p):
    print(p)

header=CTkFrame(
    master=ventana,
    width=1000,
    height=100,
    fg_color="#44E3D3",
    corner_radius=0
)
secction1=CTkFrame(master=ventana,
    width=960,
    height=510,
    fg_color="#44E3D3")

secction1.place(x=20,y=120)
header.place(x=0, y=0)

vnVusuario = CTkToplevel(ventana, width=400, height=400)

titulo = CTkLabel(vnVusuario,text="Buscar paciente")
titulo.place(x=150,y=40)

cajaTexto = Sipi(vnVusuario,"No de documento",320, 80, 280)
cajaTexto.place(x=40,y=90) 

btn = CTkButton(vnVusuario,text="buscar paciente",command=lambda:buscarPaciente(vnVusuario,cajaTexto.getEntri(),lambda:(llenarobPaciente(),opcionePaciente())))
btn.place(x=130,y=180)



ventana.mainloop()