import random as r
cnt=0
while d!=7:
    d = r.randint(1,10)
    cnt+=1
    print(d)
  if d==5:
    print('game over')
     break
else:
    print('恭喜',cnt,'次')
