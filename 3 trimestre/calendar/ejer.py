import calendar

# imprime todo el calendario de ese año
#print(calendar.calendar(2023))

# para cambiar el dia de inicio de la semana
calendar.setfirstweekday(calendar.SUNDAY) # para cambiar el dia de inicio de la semana
#print(calendar.month(2023,3)) imprime el mes seleccionado del año seleccionado

# impreme el numero de dia de la semana para este ejemplo fue 2 que e sigual a miercoles
#print(calendar.weekday(2023, 3, 22))

#CANTIDAD DE LETRAS INICIALES DEL NOMBRE DEL DIA DE LA SEMANA.
#print(calendar.weekheader(2))

# año biciesto
#print(calendar.isleap(2023))
#print(calendar.leapdays(2010, 2024 +1))  # Hasta 2021, pero sin incluirlo.

# Objeto que muestre de manera iterada los numeros de los dias de la semana
c = calendar.Calendar(calendar.SUNDAY)
#for i in c.iterweekdays():
    #print(i, end=" ")

#muesta año, mes y dia, incluso los dias que falten antes y despues para la semana completa
c = calendar.Calendar(calendar.SUNDAY)

#for date in c.itermonthdates(2023, 3):
#    print(date, end=" ")

#devuelve los dias del mes y pone ceros en los dias que esten fuera del mes seleccionado.
# metodo itermonthdays y similare
c = calendar.Calendar()
#for iter in c.itermonthdays(2023, 3):
#    print(iter, end=" ")
#for iter in c.itermonthdays2(2023, 3):
#    print(iter, end=" ")
#for iter in c.itermonthdays3(2023, 3):
#     print(iter, end=" ")
#for iter in c.itermonthdays4(2023, 3):
#    print(iter, end=" ")

# toma el año y el mes, y luego devuelve una lista de semanas en un mes específico.
# hace una lista de cada semana que tenga el mes con tuplas
c = calendar.Calendar()

for i in c.monthdays2calendar(2023, 3):
    print(i)