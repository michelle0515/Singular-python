import random as r
small=1
large=100
ans = r.randint(1,100)
a=0
print(ans)
while a!=ans:
    a=int(input('number:'))
    if a<ans and a>small:
        small=a
    if a>ans and a<large:
        large=a

    print('no',small,'到',large)

print('game over')


