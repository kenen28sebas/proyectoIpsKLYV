from interfaz import*
from clases.paciente import * 
import pymongo
from clases.agenda import *
from clases.Cita import * 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["proyecto_kenenitos"]
persona = mydb["Persona"]
cita = basedatos["Cita"]
paciente = None
listacitas =[]
año = datetime.datetime.now().year
mes = datetime.datetime.now().month
dia = datetime.datetime.now().day
fecha = datetime.datetime(2024,9,24,8,20)
def llenarobCita(fechad):
    global listacitas,fecha
    listacitas =[]
    cu = cita.find({"fecha_cita": fechad}).sort("fecha_cita", pymongo.ASCENDING)
    for i in cu:
        # print(i["fecha_creacion"].split(","))
        citas = Cita(fecha,"","",cita)
        citas.setDatosdb(
            i["no_cita"],
            i["vigencia"],
            i["fecha_creacion"],
            i["fecha_cita"],
            i["medico"],
            i["consultorio"],
            i["hora_consulta"],
            i["hora_f"]
        )
        listacitas.append(citas)
    return listacitas




agenda = Agenda(año,mes,23)
for i in range(0,7):
    agenda.setDia(i+23)
    lis = llenarobCita(f'{año},{mes},{i+23}')
    agenda.getDiasSemanas(i).setCitas(lis)

        




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
                        paciente["nacionalidad"],
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
        # usuario.destroy()
        tituloError = CTkLabel(vnVusuario,text="No se encontro el páciente")
        tituloError.place(x=150,y=250)

def opcionePaciente():
    global vnVusuario,ventana
    
    
    vnVusuario.destroy()

    op2 = OpcionesBig(secction1,"consultar citas",lambda:consultarCitas())
    op2.place(x=220,y=350)
    op3 = OpcionesBig(secction1,"crear cita",lambda:crearCitas())
    op3.place(x=520,y=350)
    def consultarCitas():
        pass
    def crearCitas():
        global header,agenda
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
        agenda = Calendario(secctionC,agenda.getDiasSemanas(0).getCitas(),agenda.getDiasSemanas(1).getCitas(),agenda.getDiasSemanas(2).getCitas(),agenda.getDiasSemanas(3).getCitas(),agenda.getDiasSemanas(4).getCitas(),agenda.getDiasSemanas(5).getCitas(),agenda.getDiasSemanas(6).getCitas(),lambda v :confirmarCita())
        agenda.place(x=0,y=0)
        
            
        
    

ventana = CTk(fg_color="white")

ventana.geometry("1000x650")
def confirmarCita():
            vnCita = CTkToplevel(ventana, width=400, height=400)
            vnCita.lift()
            vnCita.attributes('-topmost', True)
            cajaTexto = Sipi(vnCita,"doctor",320, 80, 280)
            cajaTexto.place(x=40,y=20) 
            cajaTexto = Sipi(vnCita,"consultorio",320, 80, 280)
            cajaTexto.place(x=40,y=120) 
            btncargarCita = CTkButton(vnCita,text="cargar")
            btncargarCita.place(x=130,y =220)


def prueba ():
    print("hola")

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
vnVusuario.lift()
vnVusuario.attributes('-topmost', True)
titulo = CTkLabel(vnVusuario,text="Buscar paciente")
titulo.place(x=150,y=40)



cajaTexto = Sipi(vnVusuario,"No de documento",320, 80, 280)
cajaTexto.place(x=40,y=90) 

btn = CTkButton(vnVusuario,text="buscar paciente",command=lambda:buscarPaciente(vnVusuario,cajaTexto.getEntri(),lambda:(llenarobPaciente(),opcionePaciente())))
btn.place(x=130,y=180)



ventana.mainloop()