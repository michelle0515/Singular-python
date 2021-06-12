'''
學校提供分數等第查尋，讓使用都輸入分數
90分以上含90為優等
80-89輸出為甲等
70-79輸出為乙等
60-69輸出為丙等
59以下輸出為不及格
請寫出以上程式
'''
score=int(input('your score:'))
if score>=90:
    print('優等')
elif score>=80:
    print('甲等')
elif score>=70:
    print('乙等')
elif score>=60:
    print('丙等')
else:
    print('不及格')
