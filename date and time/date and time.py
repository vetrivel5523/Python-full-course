#get current time
import datetime
x=datetime.datetime.now()
print(x)

#get month
import datetime
x=datetime.datetime.now()
print(x.month)
print(x.strftime("%b"))

##change into correct allignment
import datetime
x=datetime.datetime(2003,5,5)
print(x)

#tik tok
#strf- string format
import datetime
x=datetime.datetime(2003,5,5)
print(x.strftime("%b"))

#no of tiks
import time
tiktok=time.time()
print("number of tiks: ",tiktok)

#print today details

import datetime
presenttime= datetime.datetime.now()
print("now the time is :",presenttime)
print("today date is :",presenttime.strftime("%d%m %y"))
print("year is :",presenttime.year)
print("month is :",presenttime.month)
print("day is :",presenttime.day)