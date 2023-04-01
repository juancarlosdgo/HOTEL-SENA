import calendar

class MyCalendar:
    def __init__(self,year,day):
        self.__year=year
        self.__day=day
    
    def count_weekday_in_year (self,year,day):
        c = calendar.calendar(calendar.Calendar.monthdays2calendar)
        for i in c(int(year), int(day)):
            print(i)
        
a = MyCalendar
b = a.count_weekday_in_year(2019,0,1)
