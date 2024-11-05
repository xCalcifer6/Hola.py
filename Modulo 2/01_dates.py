## Dates ##

from datetime import datetime

ahora = datetime.now() # Obtener fecha actual

print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)

timestamp = ahora.timestamp() # marca de tiempo (1970)

año_2025 = datetime(2025, 1, 1) # Crear una fecha

print(año_2025)

from datetime import date

current_date = date.today()
print(current_date)