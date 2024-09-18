from .persona import Persona
class Paciente (Persona):
    
    def __init__(self, tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,Rh,estado_civil, tp_atencionEspecial,ocupacion,tp_afiliado,regimen,estrato,Eps, nacionalidad):
        super().__init__(tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
        
        self.__Rh = Rh
        self.__estado_civil = estado_civil
        self.__tp_atencionEspecial = tp_atencionEspecial
        self.__ocupacion = ocupacion
        self.__tp_afiliado = tp_afiliado
        self.__regimen = regimen
        self.__estrato = estrato
        self.__Eps = Eps
        self.__nacionalidad = nacionalidad
        
    
    def getRh(self):
        return self.__Rh
    
    def setRh(self, Rh):
        self.__Rh = Rh
        
    def getTpAtencionEs(self):
        return self.__tp_atencionEspecial
    
    def setTpAtencionEs(self, tp_atencionEspecial ):
        self.__tp_atencionEspecial = tp_atencionEspecial
        
    def getOcupacion(self):
        return self.__ocupacion
    
    def setOcupacion(self, ocupacion):
        self.__ocupacion = ocupacion
    
    def getTpAfiliado(self):
        return self.__tp_afiliado
    def setTpAfiliado(self, tp_afiliado):
        self.__tp_afiliado = tp_afiliado
        
    def getRegimen(self):
        return self.__regimen
    
    def setRegimen(self, regimen):
        self.__regimen = regimen
        
    def getEstrato(self):
        return self.__estrato
    
    def setEstrato(self, estrato):
        self.__estrato = estrato
        
    def getEstadoCivil(self):
        return self.__estado_civil
    
    def setEstadocivil(self, estado_civil):
        self.__estado_civil = estado_civil
    
    def getEps(self):
        return self.__Eps
    
    def setEps(self, Eps):
        self.__Eps = Eps
        
    def getNacionalidad(self):
        return self.__nacionalidad
    
    def setNacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad