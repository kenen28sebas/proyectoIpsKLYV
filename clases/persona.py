
class Persona:
    def __init__(self,tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        self.__tipo_doc = tipo_doc
        self.__identificacion = identificacion
        self.__fecha_exp = fecha_exp
        self.__lugar_exp = lugar_exp
        self.__nombres = nombres
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__fecha_nacimiento = fecha_nacimiento
        self.__genero = genero
        self.__sexo = sexo
        self.__telefono = telefono
        self.__email = email


# Identificacion
    def getTipoDoc(self):
        return self.__tipo_doc
    def setTipoDoc(self, tipo_doc):
        self.__tipo_doc = tipo_doc

    def getIdentificacion(self):
        return self.__identificacion

    def setIdentificacion(self, identificacion):
        self.__identificacion = identificacion
# Fecha expedicion
    def getFechaExp(self):
        return self.__fecha_exp

    def setFechaExp(self, fecha_exp):
        self.__fecha_exp = fecha_exp
# Lugar de expedicion
    def getLugar(self):
        return self.__lugar_exp

    def setLugar(self, lugar_exp):
        self.__lugar_exp = lugar_exp
# Nombres
    def getNombres(self):
        return self.__nombres

    def setNombres(self, nombres):
        self.__nombres = nombres
# Apellido1
    def getApellido1(self):
        return self.__apellido1

    def setApellido1(self, apellido1):
        self.__apellido1 = apellido1
# Apellido2
    def getApellido2(self):
        return self.__apellido2

    def setApellido2(self, apellido2):
        self.__apellido2 = apellido2
# Fecha nacimiento
    def getFechaN(self):
        return self.__fecha_nacimiento

    def setFechaN(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
# Genero
    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero
# Sexo
    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        self.__sexo = sexo
# Telefono
    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono
# Email
    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email
