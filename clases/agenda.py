import datetime
from clases.agendaDia import *
class Agenda ():
    def __init__(self,año,mes,dia):
        self.año = datetime.date(año,mes,dia).year 
        self.mes = datetime.date(año,mes,dia).month 
        self.semana = datetime.date(año,mes,dia).isocalendar()[1]
        self._dias = []
        self.dia = dia
    def getsemanas (self):
        return self.semana
        
    def getdiasSemanas (self):
        return self._dias
        
    def setSigSemana(self):
        año = self.año
        mes = self.mes  
        
    def getDiasSemanas (self,indice):
        return self._dias[indice]     
        
    def setDia(self,dia): 
        if len(self._dias) < 7:
            dia = AgendaDia(self.año,self.mes,dia )
            self._dias.append(dia)
            
        
        
# o = Agenda(2024,9,13,2)  
# print(o.año,o.mes,o.semana)     
        
        
# fecha_actual = datetime.datetime.now()
# print("Fecha actual:", fecha_actual)

# # Sumar 2 semanas

# nueva_fecha = fecha_actual + datetime.timedelta(weeks=2)
# print("Fecha después de 2 semanas:", nueva_fecha)


# Obtener la fecha actual
año = datetime.datetime.now().year
mes = datetime.datetime.now().month
dia = datetime.datetime.now().day

ob = Agenda(año,mes,dia)

print(ob.año)


