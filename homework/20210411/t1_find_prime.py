"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。


"""
#a=int(input('number:'))
#for i in range(1,a+1):
a=int(input('number:'))
for i in range(2,a):
    for r in range(1,i):
     if i%r==0:
        continue
     else:
        print(i)

