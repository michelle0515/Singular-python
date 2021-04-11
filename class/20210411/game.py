import random as r
small=1
large=100
ans = r.randint(1,100)
a=0
cnt = 0
print(ans)
while True:
    # a=int(input('number:'))
    a = r.randint(small, large)
    cnt+=1
    if a==ans:
        print(a, 'yes')
        break
    if a<ans and a>small:
        small=a
    if a>ans and a<large:
        large=a

    print(a, 'no',small,'到',large)

print('game over', cnt)


