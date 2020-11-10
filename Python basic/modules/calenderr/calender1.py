import calendar

print(calendar.month(2020,10))

c=calendar.TextCalendar(calendar.WEDNESDAY)
#str1=c.formatmonth(2020,10)

#print(str1)

#c=calendar.TextCalendar(calendar.WEDNESDAY)
#str2=c.formatmonth(2020,10)

#print(str2)
#for c in c.itermonthdays(2020,10):
#    print(c,end="")
for i in calendar.month_name:
    print(i,end="")

print(calendar.month_name[10])

for i in calendar.day_name:
    print(i,end="")

for i in calendar.month_abbr:
    print(i)

for i in calendar.day_abbr:
    print(i)