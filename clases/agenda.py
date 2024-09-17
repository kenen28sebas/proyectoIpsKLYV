import datetime
class Agenda ():
    def __init__(self,ano,mes,dia,semana):
        self.ano = datetime.date(ano,mes,dia).year 
        self.mes = datetime.date(ano,mes,dia).month 
        self.semana = datetime.data(ano,mes,dia).isocalendar()[1]
    def semanas (self):
        semanas = datetime.timedelta(weeks=52)
        
    def diasSemanas (self):
        dias = []
        
        
        
        
# o = Agenda(2024,9,13,2)  
# print(o.ano,o.mes,o.semana)     
        
        
# fecha_actual = datetime.datetime.now()
# print("Fecha actual:", fecha_actual)

# # Sumar 2 semanas

# nueva_fecha = fecha_actual + datetime.timedelta(weeks=2)
# print("Fecha después de 2 semanas:", nueva_fecha)

# Obtener la fecha actual
fecha_actual = datetime.datetime(2023,1,10)

# Obtener el número de la semana del año
numero_semana = fecha_actual.isocalendar()[1]

semanas = datetime.timedelta(weeks=2)

print(f"Estamos en la semana número {numero_semana} del año.")

print(semanas)

# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()

# Obtener el número correspondiente al día de la semana (lunes: 0, domingo: 6)
dia_semana = fecha_actual.weekday()

# Definir una lista con los nombres de los días de la semana
nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Mostrar el día de la semana actual
print(dia_semana)


