from persona import *

class Medicos(Persona):
    def __init__(self, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,especialidad):
        super().__init__(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
        self.__especialidad=especialidad


    def GetEspecialidad(self):
        return self.__especialidad
















#especialidad de jose 
    def getEspecialidad (self):

        return self.__especialidad
    def setEspecialidad(self,especialidad):
        self.__especialidad=especialidad

    def consultarHv (self):
        pass

    def solicitarActualizacion (self):
        pass

    def consultarTurnos(self):
        pass

    def actualizarDatosB (self):
        pass

