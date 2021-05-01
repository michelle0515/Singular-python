'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
def lcm(x,y):
    if x>y:
        a=x
    else:
        a=y
    while True:
        if a%x==0 and a%y==0:
            lcm=a
            break
        a+=1

    return lcm

num1=int(input('number1:'))
num2=int(input('number2:'))
print(num1,'and',num2,'最小公倍數為:',lcm(num1,num2))
