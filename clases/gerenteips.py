from persona import *

class Gerente(Persona):
    def __init__(self, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        super().__init__(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)

    def consultarServicios (self):
        pass

    def habilitarServicios (self):
        pass

    def inhabilitarServicios (self):
        pass

    