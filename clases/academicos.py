class Academicos ():

    def __init__(self,titulo,institucion,fechaInicio,fechaFin):

        self.__titulo=titulo
        self.__institucion=institucion
        self.__fechaInicio=fechaInicio
        self.__fechaFin=fechaFin

    def gettitulo (self):
        return self.__titulo

    def getInstitucion (self):
        return self.__institucion
    def getFechaI (self):
        return self.__fechaInicio
    def getFechaF (self):
        return self.__fechaFin 