from  persona import *
from  hojavida import *
from academicos import *
from experienciaL import *
from personalM import Medicos
class TalentoH (Persona):

    def __init__(self, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        super().__init__(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
    
    def crearPm(self,identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,especialidad ):
        objeto=Medicos(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email,especialidad)
        return objeto



# p1=TalentoH(12548,"20-05-2024","Bogota","jose alberto","perez","caedenas","03-12-2005","indefinido","travesti","3115698569","kdjskdks@gmail.com")
# print(p1.getNombres())

p1 = TalentoH(12548,"20-05-2024","Bogota","jose alberto","perez","caedenas","03-12-2005","indefinido","travesti","3115698569","kdjskdks@gmail.com") 

pm1=Medicos(45665,"10-04-1698","Suba","martha","contreras","nuñez","14-02-1998","mujer","lesbiana","3225698745","tupapaentanga565@gmail.com","medicina general")
print(pm1.getEspecialidad())

# pm2=p1.crearPm()

pm3=p1.crearPm(45665,"11-04-1258","Soacha","maria","ramirez","nuñez","10-02-1325","mujer","jesucristo","3225698745","diostebendiga0945@gmail.com","ginecologa")
print(pm3.getSexo())

pm4=p1.crearPm(3214623,"11,02,2025","Bosa","jesus","tu papa","en tanga","03-07-1898","hombre","gay","311256987","djfdjfdrf@gmail.com","cardiologia")
print(pm4.getEmail())
# print(pm2.getSexo())

expe = pm4.getExpLaboral ("yanguas", "enfermera jefe", "2020- 06-12", "2024 - 09 - 13")
print(expe.getEmpresa())

pm5 = p1.crearPm("CC", 11936212, "12-07-2002", "Cali", "Jose Daniel", "Cardenas", "Contreras", "05-03-1977", "hombre", "masculino","3124564567", "jose.cotreras@gmail.com", "Ortopedista" )
