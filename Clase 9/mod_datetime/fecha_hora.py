import datetime

mi_hora = datetime.time(17,35)
print(mi_hora)

mi_dia = datetime.date(1997,5,23)
print(mi_dia.today())
from datetime import datetime
mi_fecha = datetime(1997,5,23,23,23,23)
mi_fecha = mi_fecha.replace(month=11)

despierta=datetime(2022,10,4,7,30)
duerme = datetime(2022,10,5,23,30)
vigilia= duerme-despierta

from datetime import date
nacimiento = date(1995,3,5)
defuncion = date(2080,4,4)
vida = defuncion-nacimiento
print(vida)
