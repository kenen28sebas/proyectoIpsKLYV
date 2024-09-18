import datetime
class Agenda ():
    def __init__(self,ano,mes,dia,semana):
        self.ano = datetime.date(ano,mes,dia) - datetime.timedelta(weeks=semana)
        self.mes = datetime.date(ano,mes,dia) - datetime.timedelta(weeks=semana)
        self.semana = semana
        
    def semanas (self):
        semanas = datetime.timedelta(weeks=52)
        
        
        
# o = Agenda(2024,9,13,2)  
# print(o.ano,o.mes,o.semana)     
        
        
# fecha_actual = datetime.datetime.now()
# print("Fecha actual:", fecha_actual)

# # Sumar 2 semanas

# nueva_fecha = fecha_actual + datetime.timedelta(weeks=2)
# print("Fecha después de 2 semanas:", nueva_fecha)

# Obtener la fecha actual
fecha_actual = datetime.datetime(2012,1,6)

# Obtener el número de la semana del año
numero_semana = fecha_actual.isocalendar()[2]

s = numero_semana.day

print(f"Estamos en la semana número {numero_semana} del año.")

print(s)

