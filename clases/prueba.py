import datetime
ahora = datetime.datetime.now()
des = datetime.datetime(ahora.year,ahora.month,ahora.day,ahora.hour)

año = ahora.year
mes = ahora.month
dia = ahora.day + 20

if dia > 29 :
    dia = dia - 29
    mes = mes + 1
    if mes > 12:
        mes = 1
        año = año + 1
        

des = datetime.date(año, mes, dia)


print(ahora)
print(des)


