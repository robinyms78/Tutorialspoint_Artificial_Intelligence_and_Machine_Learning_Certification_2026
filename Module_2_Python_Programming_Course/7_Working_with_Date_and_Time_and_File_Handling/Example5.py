# Date and Time in Python

from datetime import *
dt1 = datetime(year=2019, month=9, day=22, hour=11, minute=30, second=15)
print(dt1)
dt2 = dt1.replace(month=10, day=22, hour=13)
print(dt2)