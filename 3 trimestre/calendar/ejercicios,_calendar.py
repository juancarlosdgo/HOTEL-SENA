import calendar  

#print(calendar.calendar(2023))
print(calendar.month(2023,3)) #imprima el mes 
print(calendar.weekday(2023, 3, 22)) #imprima el dia

#mostrar el mes de marzo de 2023 con la sama que inicia con 

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2023,3))

# una lista de semanas en un mes específico.

c = calendar.Calendar(calendar.SUNDAY)
for i in c.monthdays2calendar(2023, 3):
    print(i)
