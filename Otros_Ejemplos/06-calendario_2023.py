# El ejemplo configura TextCalendar para comenzar semanas
# el domingo, siguiendo la convención estadounidense. 
# El valor predeterminado es utilizar la convención europea de comenzar una semana el lunes.

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
print(c.formatyear(2023))
