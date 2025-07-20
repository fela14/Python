from datetime import date
from datetime import time
import time

today = date.today()
print("Today: ", today)
print("Year: ", today.year)
print("Month: ", today.month)
print("Day: ", today.day)

my_date = date(1996, 4, 20)
print(my_date)

timestamp = time.time()
print("Timestamp: ", timestamp)
d = date.fromtimestamp(timestamp)
print("Date: ", d)

d = d.replace(year=2020, month=1, day=16)
print("Date: ", d)
d = date.today()
print(d.weekday())
print(d.isoweekday())

from datetime import time
t = time(14, 53, 20, 1)
print("Today: ", t)
print("Hour: ", t.hour)
print("Minute: ", t.minute)
print("Second: ", t.second)
print("Microsecond ", t.microsecond)

import time
class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well, I feel great!")
student = Student()
student.take_nap(0)

timestamp = 1572879180
print(time.localtime(timestamp))
print(time.gmtime(timestamp))
print(time.ctime(timestamp))

timestamp = time.time()
st1 = time.gmtime(timestamp)
print(time.asctime(st1))
st2 = time.mktime((2019,12,6,14,53,20,0,308,0))
print(time.ctime(st2))

from datetime import datetime
from datetime import time
print("today:", datetime.today())
print("now", datetime.now())
print("utcnow", datetime.utcnow()) #deprecated

d = date(2025,12,31)
t = time(14,53)
dt = datetime(2025,12,31,14,53)

print(d.strftime("%Y/%m/%d"))
print(t.strftime("%H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S"))

import time
timestamp = 1572879180
st = time.gmtime(timestamp)
print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print("*"*30)
from datetime import datetime
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

d1 = date(2020,11,4)
d2 = date(2019,11,4)
print(d1-d2)
dt1 = datetime(2020,11,4,0,0,0)
dt2 = datetime(2019,11,4,14,53,0)
print(dt1-dt2)

from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019,10,4) + delta2
print(d)

dt = datetime(2019,10,4,14,53) + delta2
print(dt)











