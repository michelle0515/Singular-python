"""
str = "00000:00000:00000:00000:00000"

請使用list 分割及重組元素


for loop show list value
"99999:00000:00000:00000:00000"  第一圈
"00000:99999:00000:00000:00000"  第二圈
"00000:00000:99999:00000:00000"  第三圈
"00000:00000:00000:99999:00000"  第四圈
"00000:00000:00000:00000:99999"  第五圈

只能用一個list
"""
for i in range(0,5):
   a="00000:00000:00000:00000:00000"
   a=a.split(':')
   a[i]='99999'
   print(':'.join(a))















