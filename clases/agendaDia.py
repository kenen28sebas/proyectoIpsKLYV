import datetime
class AgendaDia():
    def __init__(self,año,mes,dia,):
        self._dia = datetime.date(año,mes,dia).strftime("%A")
        self._dian = dia 
        self._horas = {
            '7:00 am':[],
            '8:00 am':[] ,
            '9:00 am':[],
            '10:00 am':[],
            '11:00 am':[],
            '12:00 pm':[],
            '1:00 pm':[],
            '2:00 pm':[],
            '3:00 pm':[],
            '4:00 pm':[],
            '5:00 pm':[],
            '6:00 pm':[],
            '7:00 pm':[]
        }
        self.citas = []
        
    def llenarPendientes(self):
        pass
    
    def getHora(self):
        return self._horas
    
    def getDia(self):
        return self._dia
    
    def getDian(self):
        return self._dian
    
    def setCitas(self,arreglo):
        for i in arreglo:
            self.citas.append(i)
            
    def getCitas(self):
        return self.citas        