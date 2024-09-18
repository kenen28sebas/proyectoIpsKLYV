from persona import *
from Experiencia_laboral import *
from academicos import *

class Medicos(Persona):
    def __init__(self, tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,especialidad):
        super().__init__(tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
        self.__especialidad=especialidad
        self.__academicos = []
        self.__expLaboral = []

    def getEspecialidad(self):
        return self.__especialidad

    def setExpLaboral (self,empresa, cargo, fecha_inicio, fecha_fin):
        exp = Experiencia_laboral(empresa, cargo, fecha_inicio, fecha_fin)
        self.__expLaboral.append(exp)
    
    def getExpLaboral(self ):
        return self.__expLaboral 
        
    def setAcademicos (self,titulo,institucion,fechaInicio,fechaFin):
        acad=Academicos(titulo,institucion,fechaInicio,fechaFin)
        self.__academicos.append(acad)

    def getAcademicos(self):
        return self.__academicos
        
#especialidad de jose 
    def getEspecialidad(self):

        return self.__especialidad
    
    def setEspecialidad(self,especialidad):
        self.__especialidad=especialidad

    def consultarHv(self):
        pass

    def solicitarActualizacion(self):
        pass

    def consultarTurnos(self):
        pass

    def actualizarDatosB(self):
        pass

