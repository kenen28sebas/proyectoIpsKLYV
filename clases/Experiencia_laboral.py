class Experiencia_laboral:
    def __init__(self, empresa, cargo, fecha_inicio, fecha_fin ):
        self.__empresa = empresa
        self.__cargo = cargo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        
        
        
        
    def getEmpresa(self):
        return self.__empresa
    
    def setEmpresa(self, empresa):
        self.__empresa = empresa
        
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo
        
    def getFecha_inicio(self):
        return   self.__fecha_inicio
    
    def setFecha_inicio(self, fecha_inicio):
        self.getFecha_inicio = fecha_inicio
        
    def getFecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin
        
        
    def consultar_experiencia(self):
        pass
        