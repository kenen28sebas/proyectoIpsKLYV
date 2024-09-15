from persona import *
from personalM import *
# from academicos import *
# from experienciaL import *

from personalM import *
class TalentoH (Persona):

    def __init__(self, tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        super().__init__(tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
    
    def crearPm(self,tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email, especialidad):
        per = Medicos( tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email, especialidad)
        return per

    




    












    



    # def registrarHV ():
    #     nombre_completo=input("escriba su nombre")
    #     identificacion=input("escriba su identificacion")
    #     direccion=input("la direccion hermano")
    #     telefono=input("digite su numero de telefono")
    #     email=input("digite su email")
    #     nacionalidad=input("cual es su nacionalidad,acaso es veneco")


    # registrarHV()
