# from clases.th import *


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



def llenarArchivoPeM (objeto):
        archivo = {
            "tipo_documento" : objeto.getTipoDoc(),
            "Identificacion" : objeto.getIdentificacion(),
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
    
    
def llenarArchivoPa(objeto):
    archivo = {
        "tipo_documento" :objeto.getTipoDoc(),
        "Identificacio" : objeto.getIdentificacion(),
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
            "Rh" : objeto.getRh(),
            "estado_civil" : objeto. getEstadoCivil(),
            "tipo_atencionEspecial" : objeto.getTpAtencionEs(),
            "ocupación" : objeto.getOcupacion(),
            "tipo_afiliado  " : objeto.getTpAfiliado(),
            "regimen" : objeto.getRegimen(),
            "estrato" : objeto.getEstrato(),
            "Eps" : objeto. getEps(),
            "Nacionalidad" : objeto.getNacionalidad()
    
     }
    
    return archivo
    
    
def crearPaciente(objeto):
    archivoPa ={
        "tipo_documento": ""
        
    }
    
    
print("hola")





