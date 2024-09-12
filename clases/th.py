from persona import *
# from hojavida import *
# from academicos import *
# from experienciaL import *
from personalM import Medicos
import pymongo
import json
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
print(cliente.list_database_names())
basedatos = cliente["proyecto_IPS"]
med = basedatos["Medico"]





class TalentoH (Persona):

    def __init__(self, tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        super().__init__(tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
    
    def crearPm(self,tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email, especialidad):
        per = Medicos( tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email, especialidad)
        return per



p1=TalentoH("CC", 12548,"20-05-2024","Bogota","jose alberto","perez","caedenas","03-12-2005","indefinido","travesti","3115698569","kdjskdks@gmail.com")
# print(p1.getNombres())

pm1=Medicos("CC", 45665,"10-04-1698","Suba","martha","contreras","nuñez","14-02-1998","mujer","lesbiana","3225698745","tupapaentanga565@gmail.com","medicina general")
print(pm1)


pm2 = p1.crearPm("CC", 1234567, "23/06/6788", "Soacha", "Juan Miguel", "Tovar", "torres", "12/08/1989", "travesti", "masculino", "323465789", "juan.tovar02@hotmail.com", "perro")
print(pm2.getEspecialidad()) 

def llenarArchivo (objeto):
    archivo = {
        "tipo_documento" : objeto.getTipoDoc(),
        "fecha_expedicion" : objeto.getFechaExp(),
        "lugar_expedicion" : objeto.getLugar(),
        "nombres" : objeto.getNombres(),
        "apellido1" : objeto.getApellido1(),
        "apellido2" : objeto.getApellido2(),
        "fecha_nacimiento" : objeto.getFechaN(),
        "genero": objeto.getGenero(),
        "sexo" : objeto.getSexo(),
        "email" : objeto.getEmail(), 
        "teléfono": objeto.getTelefono()
            
        }
    return archivo
        
llenarArchivo(pm2)
u = llenarArchivo(pm2)
med.insert_one(u)






    



    # def registrarHV ():
    #     nombre_completo=input("escriba su nombre")
    #     identificacion=input("escriba su identificacion")
    #     direccion=input("la direccion hermano")
    #     telefono=input("digite su numero de telefono")
    #     email=input("digite su email")
    #     nacionalidad=input("cual es su nacionalidad,acaso es veneco")


    # registrarHV()
