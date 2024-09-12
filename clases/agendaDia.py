import datetime
class AgendaDia():
    def __init__(self,dia):
        self._dia = datetime.date(dia).strftime("%A")
        self._horas = {
            '7:00 am':{},
            '8:00 am':{} ,
            '9:00 am':{},
            '10:00 am':{},
            '11:00 am':{},
            '12:00 pm':{},
            '1:00 pm':{},
            '2:00 pm':{},
            '3:00 pm':{},
            '4:00 pm':{},
            '5:00 pm':{},
            '6:00 pm':{},
            '7:00 pm':{}
        }