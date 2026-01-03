# Date and Time in Python

from datetime import *
d = date(2021,6,15)
t = time(12,30)

dt = datetime.combine(d, t)
print(dt)
