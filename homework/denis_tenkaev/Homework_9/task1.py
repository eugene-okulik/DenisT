import datetime as dt

hum_date = "Jan 15, 2023 - 12:05:33"
pyt_date = dt.datetime.strptime(hum_date, "%b %d, %Y - %H:%M:%S")
print(pyt_date.strftime("%B"))
print(pyt_date.strftime("%d.%m.%Y, %H:%M"))
