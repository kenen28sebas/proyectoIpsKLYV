class Experiencia ():

    def __init__(self,empresa,cargo,fechaInicio,fecha_fin):

        self.__empresa=empresa
        self.__cargo=cargo
        self.__fechaInicio=fechaInicio
        self.__fecha_fin=fecha_fin

    def getempresa (self):
        return self.__empresa
    def getCargo(self):
        return self.__cargo
    def getFechaIni(self):
        return self.__fechaInicio
    def getFechaFi(self):
        return self.__fecha_fin