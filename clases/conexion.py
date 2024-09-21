from clases.th import *

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
med = basedatos["Medico"]



def llenarArchivomd (objeto,collection):
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
        

                
            
                
        collection.insert_one(archivo)
    
print("hola")

p1=TalentoH("CC", 11936212, "12-07-2002", "Cali", "Jose Daniel", "Cardenas", "Contreras", "05-03-1977", "hombre", "masculino","3124564567", "jose.cotreras@gmail.com" )

pm5 = p1.crearPm("CC", 11936212, "12-07-2002", "Cali", "Jose Daniel", "Cardenas", "Contreras", "05-03-1977", "hombre", "masculino","3124564567", "jose.cotreras@gmail.com", "Ortopedista" )
pm5.setAcademicos("Doctor", "Sena", "15-01-2001", "30-12-2006" )

