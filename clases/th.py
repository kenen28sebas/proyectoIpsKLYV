from persona import *
# from hojavida import *
# from academicos import *
# from experienciaL import *
from personalM import *
class TalentoH (Persona):

    def __init__(self, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        super().__init__(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
    
    def crearPm(self):
        objeto=Medicos(45665,"11-04-1258","Soacha","maria","ramirez","nuñez","10-02-1325","mujer","jesucristo","3225698745","diostebendiga0945@gmail.com","ginecologa")
        return objeto



p1=TalentoH(12548,"20-05-2024","Bogota","jose alberto","perez","caedenas","03-12-2005","indefinido","travesti","3115698569","kdjskdks@gmail.com")
# print(p1.getNombres())

pm1=Medicos(45665,"10-04-1698","Suba","martha","contreras","nuñez","14-02-1998","mujer","lesbiana","3225698745","tupapaentanga565@gmail.com","medicina general")
print(pm1.getEspecialidad())

pm2=p1.crearPm()

print(pm2.getSexo())


    



    # def registrarHV ():
    #     nombre_completo=input("escriba su nombre")
    #     identificacion=input("escriba su identificacion")
    #     direccion=input("la direccion hermano")
    #     telefono=input("digite su numero de telefono")
    #     email=input("digite su email")
    #     nacionalidad=input("cual es su nacionalidad,acaso es veneco")


    # registrarHV()
