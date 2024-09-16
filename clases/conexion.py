from th import *
from paciente import *

import pymongo
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
print(cliente.list_database_names())
basedatos=cliente["proyecto_IPS"]
med=basedatos["Medico"]
histo = basedatos["Historia"]
ips = basedatos["ips"]
paci = basedatos["Paciente"]
per = basedatos["Persona"]
solicitud = basedatos["Solicitud_de_servicios"]



def llenarArchivo (objeto):
        archivo = {
            "tipo_documento" : objeto.getTipoDoc(),
            "fecha_expedicion" : objeto.getFechaExp(),
            "lugar_expedicion" : objeto.getLugar(),
            "nombres" : objeto.getNombres(),
            "apellido1" : objeto.getApellido1(),
            "apellido2" : objeto.getApellido2(),
            "fecha_nacimiento" : objeto.getFechaN(),
            "genero": objeto.getGenero(),
            "sexo" : objeto.getSexo(),
            "email" : objeto.getEmail(), 
            "teléfono": objeto.getTelefono(),
            "experiencia":[
                
            ],
            "academicos": [
                
            ],
            
            "especialidad" : objeto.getEspecialidad()
            
            }
        for i in objeto.getExpLaboral():
            x = {
                "empresa" :i.getEmpresa(),
                "cargo":i.getCargo(),
                "fechaInicio":i.getFechaIni(),
                "fecha_fin":i.getFechaFi()  }
            archivo["experiencia"].append(x)
            
            
        for j in objeto.getAcademicos():
             y = {
                 "titulo": j.getTitulo(),
                "institucion" : j.getInstitucion(),
                "fechaInicio" : j.getFechaI(),
                "fechaFin" : j.getFechaF()
             }
                
             archivo["academicos"].append(y)
        

                
            
                
        return archivo
    
    
def crearPaciente(objeto):
    archivoPa ={
        "tipo_documento": ""
        
    }
    
    
print("hola")

p1=TalentoH("CC", 11936212, "12-07-2002", "Cali", "Jose Daniel", "Cardenas", "Contreras", "05-03-1977", "hombre", "masculino","3124564567", "jose.cotreras@gmail.com" )

pm5 = p1.crearPm("CC", 11936212, "12-07-2002", "Cali", "Jose Daniel", "Cardenas", "Contreras", "05-03-1977", "hombre", "masculino","3124564567", "jose.cotreras@gmail.com", "Ortopedista" )
pm5.setAcademicos("Doctor", "Sena", "15-01-2001", "30-12-2006" )

med.insert_one(llenarArchivo(pm5))

# p1= Paciente("CC", 1030547698, "10-03-2024", "Fusagasuga", "Ana del carmen", "Sanabria", "Redondo", "03-04-1872","trans", "femenino", "312456789","Anaredondo@gmail.com", "B-", "casada", "desplazado", "desempleado","beneficiario","subsidiado", "uno","Nueva Eps", "Venezolana")
# p1.getApellido1()