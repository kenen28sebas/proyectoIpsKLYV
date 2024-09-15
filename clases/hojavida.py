from persona import *

class HojaDeVida(Persona):

    def __init__(self, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,experiencia_laboral,academicos):
        super().__init__(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
        self.__experiencia_laboral=[]
        self.__academicos=[]
        

    # def __init__(self,nombre_completo,identificacion,direccion,telefono,email,nacionalidad,academicos,experiencia_laboral):

    #     self.__nombre_completo=nombre_completo
    #     self.__identificacion=identificacion
    #     self.__direccion=direccion
    #     self.__telefono=telefono
    #     self.__email=email
    #     self.__nacionalidad=nacionalidad
    #     self.__academicos=[]
    #     self.__experiencia_laboral=[]



    