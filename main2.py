from interfaz import *

nombre=Sipi(ventana,"Nombres completos:",250,100,200)
nombre.place(x=50,y=200)

apellido1=Sipi(ventana,"Apellido 1:",250,100,200)
apellido1.place(x=50,y=280)

apellido2=Sipi(ventana,"Apellido 2:",250,100,200)
apellido2.place(x=50,y=360)

identificacion=Sipi(ventana,"Numero identificacion:",250,100,200,)
identificacion.place(x=50,y=440)
identificacion.validar()


fecha_exp=Sipi(ventana,"Fecha expedicion:",250,100,200)
fecha_exp.place(x=50,y=520)

lugar_exp=Sipi(ventana,"Lugar expedicion:",250,100,200)
lugar_exp.place(x=50,y=600)

# fecha_na=Sipi(ventana,"Fecha de Nacimiento:",250,100,200)
# fecha_na.place(x=350,y=200)

genero=Sipi(ventana,"Genero:",250,100,200)
genero.place(x=350,y=280)

sexo=Sipi(ventana,"Sexo:",250,100,200)
sexo.place(x=350,y=360)

telefono=Sipi(ventana,"Telefono:",250,100,200)
telefono.place(x=350,y=440)
telefono.validar()

email=Sipi(ventana,"Email:",250,100,200)
email.place(x=350,y=520)

especialidad=Sipi(ventana,"Especialidad:",250,100,200)
especialidad.place(x=350,y=600)

h = None

def cargarPm (th):
    ob = th.crearPm(nombre.getEntri(),identificacion.getEntri(),fecha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri())
    return ob

def hola (th):
    ob = th.crearPm(nombre.getEntri(),identificacion.getEntri(),fecha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri(),"s")
    h = ob
    print(h.getNombres())

btn = CTkButton(ventana,text="vive la vida",command=lambda:hola(p1))
btn.place(x=0,y=0)




ventana.mainloop()