import datetime
day = input("What is your birthday？")
birth = datetime.datetime.strptime(day,"%Y-%m-%d").date()
today = datetime.date.today()
print('距離下次生日還剩',birth-today,'天')


