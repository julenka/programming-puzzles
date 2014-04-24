__author__ = 'julenka'

import datetime

years = [(i, datetime.datetime(i,1,26).weekday()) for i in range(1,2000) if datetime.datetime(i,1,26).weekday() == 0 and i % 10 == 6]

print years
