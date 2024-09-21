from interfaz import*
from clases.paciente import * 
import pymongo
from clases.agenda import *
from clases.Cita import * 


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["proyecto_IPS"]
persona = mydb["Paciente"]
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

    op2 = OpcionesBig(secction1,"Consultar citas",lambda:consultarCitas())
    op2.place(x=100,y=60)
    op3 = OpcionesBig(secction1,"Crear cita",lambda:crearCitas())
    op3.place(x=500,y=60)
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
            fg_color="#9bf6ff",
            corner_radius=0
        )

        # lbltitulo=CTkLabel(header,text="Menu principal",font=("Ready For Fall",20),text_color="black")
        # lbltitulo.place(x=450,y=40)
        header.place(x=0, y=0)

        lblheader=CTkLabel(header,text="Agenda",font=("Ready For Fall",30),text_color="black")
        lblheader.place(x=500,y=30)


    
        # img = ImageTk.PhotoImage(Image.open("C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\agenda.png"))

    
        # lblformulario2 = CTkLabel(header, image=img)

        # lblformulario2.place(x=20,y=20)








        secctionC=CTkFrame(master=ventana,
            width=1060,
            height=510,
            fg_color="#44E3D3")
        secctionC.place(x=20,y=120)
        agenda = Calendario(secctionC,agenda.getDiasSemanas(0).getCitas(),agenda.getDiasSemanas(1).getCitas(),agenda.getDiasSemanas(2).getCitas(),agenda.getDiasSemanas(3).getCitas(),agenda.getDiasSemanas(4).getCitas(),agenda.getDiasSemanas(5).getCitas(),agenda.getDiasSemanas(6).getCitas(),lambda v :confirmarCita())
        agenda.place(x=0,y=0)
        
            
        
    

ventana = CTk(fg_color="white")

ventana.geometry("1000x450")
def confirmarCita():
            vnCita = CTkToplevel(ventana, width=500, height=500,fg_color="white")
            vnCita.lift()
            vnCita.attributes('-topmost', True)
            cajaTexto = Sipi(vnCita,"doctor:",320, 80, 280)
            cajaTexto.place(x=40,y=100) 
            cajaTexto = Sipi(vnCita,"consultorio:",320, 80, 280)
            cajaTexto.place(x=40,y=200) 
            btncargarCita = CTkButton(vnCita,text="cargar",border_width=5,border_color="#127475",fg_color="#c2f8cb",text_color="black",width=200,height=50,font=("Ready For Fall",20))
            btncargarCita.place(x=100,y =300)
            frame=CTkFrame(vnCita,width=400,height=80,border_width=5,border_color="black",fg_color="#f7c7db")
            frame.place(x=0,y=0)
            tituloframe=CTkLabel(frame,text="Crear Cita",font=("Ready For Fall",25),text_color="black")
            tituloframe.place(x=130,y=20)


def prueba ():
    print("hola")

header=CTkFrame(
    master=ventana,
    width=1000,
    height=100,
    fg_color="#f5cac3",
    corner_radius=5,
    border_width=5,
    border_color="black"
)

lbltitulo=CTkLabel(header,text="Menu principal",font=("Ready For Fall",30),text_color="black")
lbltitulo.place(x=400,y=30)

# tituloheader=CTkLabel(header,text="Agenda",font=("Ready For Fall",30),text_color="black")
# tituloheader.place(x=350,y=20)

secction1=CTkFrame(master=ventana,
    width=960,
    height=300,
    fg_color="white",border_width=5,border_color="black")

secction1.place(x=20,y=120)
header.place(x=0, y=0)

vnVusuario = CTkToplevel(ventana, width=500, height=600,fg_color="white")
vnVusuario.lift()
vnVusuario.attributes('-topmost', True)


frameTitulo=CTkFrame(vnVusuario,width=450,height=80,fg_color="#b5e2fa",border_width=5,border_color="#0fa3b1")
frameTitulo.place(x=0,y=0)
titulo = CTkLabel(frameTitulo,text="Buscar paciente",font=("Ready For Fall",20),text_color="black")
titulo.place(x=120,y=30)

# imgbuscar=Image.open("buscar.png")
# imgbuscar=imgbuscar.resize((100,100))
# imagen1=CTkImage(light_image=imgbuscar,size=(100,100))

# lblimgbuscar=CTkLabel(master=frameTitulo,image=imagen1,text="")
# lblimgbuscar.place(x=10,y=20)


cajaTexto = Sipi(vnVusuario,"No de documento",320, 80, 280)
cajaTexto.place(x=40,y=100) 

btn = CTkButton(vnVusuario,text="buscar paciente",command=lambda:buscarPaciente(vnVusuario,cajaTexto.getEntri(),lambda:(llenarobPaciente(),opcionePaciente())),border_width=3,border_color="#8338ec",fg_color="#c8b6ff",width=200,height=40,font=("Ready For Fall",18),text_color="black")
btn.place(x=100,y=200)



ventana.mainloop()