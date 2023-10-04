import datetime as dt  # as denot us allaies


current_date=dt.date.today()
print("current date:",current_date)


print(current_date)
print("current year:",current_date.year)
print("current month:",current_date.month)
print("current day:",current_date.day)

print("------------------------------------------------")

a=dt.time(10,0,55,654654)
print(a)
print(" minute",a.minute)
print(" second",a.second)
print(" microsecond",a.microsecond)

print("------------------------------------------------")

current_time=dt.datetime.now()
print("Current Time : ", current_time)
print(current_time)
print(current_time.date())
print(current_time.time())

print("--------------------------------------")
new = dt.datetime(2023, 5, 31, 12, 2, 10)
print(new)
print(new.date())
print(new.time())
print("--------------------------------------")
current = dt.datetime.now()
new_year = dt.datetime(2023, 9, 10)
difference = new_year - current
print(difference)
print("--------------------------------------")
current= dt.datetime.now()
print(current)
s=current.strftime("%A %b %d %Y")
print(s)

print(current.strftime("%a"))
print(current.strftime("%A"))
print(current.strftime("%w"))
print(current.strftime("%d"))
print(current.strftime("%b"))
print(current.strftime("%B"))
print(current.strftime("%m"))
print(current.strftime("%y"))
print(current.strftime("%Y"))
print(current.strftime("%H"))
print(current.strftime("%H"))
print(current.strftime("%p"))
print(current.strftime("%M"))
print(current.strftime("%S"))
print(current.strftime("%z"))
print(current.strftime("%Z"))
print(current.strftime("%j"))
print(current.strftime("%U"))
print(current.strftime("%W"))
print(current.strftime("%C"))
print(current.strftime("%x"))
print(current.strftime("%X"))
print(current.strftime("%%"))
print(current.strftime("%G"))
print(current.strftime("%u"))
print(current.strftime("%V"))


