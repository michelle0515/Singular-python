"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:

Triangle Area formula:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

e.g.
Show:a ="
Input1:3

Show:b ="
Input2:4

Show:c ="
Input3:5

output:
perimeter: 12.000000
Area: 6.000000
"""

a = int(input('請輸入第一邊之長度:'))
b = int(input('請輸入第二邊之長度:'))
c = int(input('請輸入第三邊之長度:'))
p = int((a+b+c)*1/2)
if a+b>c:
   print('area:',(p * (p - a) * (p - b) * (p - c)) ** 0.5,'perimeter:',a+b+c)
elif b+c>a:
   print('area:',(p * (p - a) * (p - b) * (p - c)) ** 0.5,'perimeter:',a+b+c)
elif a+c>b:
   print('area:',(p * (p - a) * (p - b) * (p - c)) ** 0.5,'perimeter:',a+b+c)
else:
   print('Cannot form a triangle')















