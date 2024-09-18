import datetime

class Cita ():
    def __init__(self,fechaCita,medico,consultorio,bdc):
        self._noCita = 0
        self._vigencia = 0
        self._fechaCreacion = f'{datetime.datetime.now().year},{datetime.datetime.now().month},{datetime.datetime.now().day},{datetime.datetime.now().hour},{datetime.datetime.now().minute}'
        self._fechaCita = f'{fechaCita.year},{fechaCita.month},{fechaCita.day}'
        self._medico = medico
        self._consultorio = consultorio
        self.setVigencia(fechaCita)
        self.setNoCita(bdc)
        self.horaC = f'{fechaCita.hour}:{fechaCita.minute}'
        self.hora = fechaCita.hour
     
    def setNoCita(self,c):
        no = 1
        n = c.find()
        for i in n:
            no += 1
        self._noCita = no
    
    def setVigencia(self,fechaCita):
        año = fechaCita.year
        mes = fechaCita.month
        dia = fechaCita.day + 20

        if dia > 29 :
            dia = dia - 29
            mes = mes + 1
            if mes > 12:
                mes = 1
                año = año + 1
        self._vigencia = f'{datetime.date(año, mes, dia).year},{datetime.date(año, mes, dia).month},{datetime.date(año, mes, dia).day}'
        
    def getNoCita(self):
        return self._noCita
    
    def getVigencia(self):
        return self._vigencia
    
    def getFechaCreacion(self):
        return self._fechaCreacion

    def getFechaCita(self):
        return self._fechaCita
    
    def getFranjaCita(self):
        return self.hora
    
    def getMedico(self):
        return self._medico
    
    def getConsultorio(self):
        return self._consultorio
    
    def getHoraConsulta(self):
        return self.horaC
    
    def setDatosdb(self, datosdb1, datosdb2, datosdb3, datosdb4, datosdb5, datosdb6, datosdb7,datosdb8):
        self._noCita = datosdb1
        self._vigencia = datosdb2
        self._fechaCreacion = datosdb3
        self._fechaCita = datosdb4
        self._medico = datosdb5
        self._consultorio = datosdb6
        self.horaC = datosdb7
        self.hora = datosdb8

    
l = datetime.datetime(2024,9,25,8,0)   


    


import pymongo
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
print(cliente.list_database_names())
basedatos=cliente["proyecto_kenenitos"]
cita = basedatos["Cita"]


p = Cita(l,"lina","c13",cita)

def llenarArchivo (objeto):
        archivo = {
            "no_cita" : objeto.getNoCita(),
            "vigencia" : objeto.getVigencia(),
            "fecha_creacion" : objeto.getFechaCreacion(),
            "fecha_cita" : objeto.getFechaCita(),
            "medico" : objeto.getMedico(),
            "consultorio" : objeto.getConsultorio(),
            "hora_consulta": objeto.getHoraConsulta(),
            "hora_f": objeto.getFranjaCita()
            }
        return archivo
    
archivoC = llenarArchivo(p)



