a=int(input('請輸入身高(公分):'))
b=int(input('請輸入體重:'))
a=(a/100)
c=(b/a**2)
print('您的BMI為:',round(c,1))
