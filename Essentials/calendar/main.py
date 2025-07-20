import calendar

print(calendar.calendar(2020))
print(calendar.prcal(2020))
print(calendar.month(2020,11))
print(calendar.month(1996,4))

calendar.setfirstweekday(calendar.MONDAY)
calendar.prcal(2020)

print(calendar.weekday(2020,12,24))
print(calendar.weekheader(3))

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021)) # Up to but not including 2021.

c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")

print()
c = calendar.Calendar()
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
print()
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
print()
for data in c.monthdays2calendar(2020, 12):
    print(data)

