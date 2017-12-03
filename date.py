#!/usr/bin/python3.5
import datetime

today = datetime.date.today()
print(today)
crimedate = datetime.date(2013,3,30)
print(crimedate)

z = today-crimedate 	# type datetime.timedelta
print(z)
print(type(z))

# get days only instead of "1708 days, 0:00:00"
print(z.days)

date_format = "%m/%d/%Y"
xxx = datetime.datetime.strptime('3/15/2012', date_format)
datetime.combine(z, datetime.min.time())
#print(today-xxx) 

