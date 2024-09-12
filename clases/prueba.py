# from conexion import *
from academicos import *
from experienciaL import *
from persona import *

class TalentoH(Persona):
    def __init__(self, identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email):
        super().__init__(identificacion, fecha_exp, lugar_exp, nombres, apellido1, apellido2, fecha_nacimiento, genero, sexo, telefono, email)
        # self.coleccion = db["hojav"]

    def agregarExperiencias(self, experiencias):
        
        experienciaL = []

        
        for exp in experiencias:
            #creando el objeto por que somos pudientes
            experiencia = Experiencia(
                empresa=exp["empresa"], 
                cargo=exp["cargo"], 
                fecha_inicio=exp["fecha_inicio"], 
                fecha_fin=exp["fecha_fin"]
            )
            
            
            diccionario = {
                "empresa": experiencia.getEmpresa(),
                "cargo": experiencia.getCargo(),
                "fecha_inicio": experiencia.getFechaInicio(),
                "fecha_fin": experiencia.getFechaFin()
            }
            
            
            experienciaL.append(diccionario)

        
        # return experienciaL

    def agregarAcademicos(self, academicos):
        
        academicoss = []

        
        for acad in academicos:
            
            academico = Academicos(
                titulo=acad["titulo"], 
                institucion=acad["institucion"], 
                fecha_graduacion=acad["fecha_graduacion"]
            )
            
            
            academico = {
                "titulo": academico.getTitulo(),
                "institucion": academico.getInstitucion(),
                "fecha_graduacion": academico.getFechaGraduacion()
            }
            
            
            academicoss.append(academico)

        
        # return academicoss

    def guardarHojaDeVida(self, direccion, nacionalidad, experiencias, academicos):

        documentos = []

        
        documento = {
            "identificacion": self.getIdentificacion(),
            "nombre_completo": self.getNombres(),
            "direccion": direccion,
            "telefono": self.getTelefono(),
            "email": self.getEmail(),
            "nacionalidad": nacionalidad,
            "experiencia_laboral": self.agregarExperiencias(experiencias),
            "academicos": self.agregarAcademicos(academicos)
        }

        
        documentos.append(documento)

        
        # resultado = self.collection.insert_many(documentos)
        # # print(f"Documentos insertados con ids {resultado.inserted_ids}")
