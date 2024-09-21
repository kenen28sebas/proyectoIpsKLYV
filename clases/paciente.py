from clases.persona import *
class Paciente (Persona):
    
    def __init__(self, tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,RH, tp_atencionEspecial,ocupacion,tp_afiliado,regimen,estraro, estado_civil,EPS):
        super().__init__(tipo_doc, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
        
        self.RH = RH
        
        self.tp_atencionEspecial = tp_atencionEspecial
        self.ocupacion = ocupacion
        self.tp_afiliado = tp_afiliado
        self.regimen = regimen
        self.estraro = estraro
        self.estado_civil = estado_civil
        self.EPS = EPS
        self.citas = []
    def setCitas(self, cita):
        self.citas.append(cita)  