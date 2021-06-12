'''
顯示今天的日期，
零食的保存期限為2/21/2022，
請顯示還有多久會到保存期限。
'''
import datetime
todaytime = datetime.date.today()
expirationdate = datetime.datetime.strptime('2022/2/21','%Y/%m/%d').date()
print('距離保存期限還剩',expirationdate-todaytime,'天')




