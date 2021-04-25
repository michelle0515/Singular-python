import random

def roll_dice(n:int):
    dice=[]
    for i in range(n):
      dice.append(random.randint(1,6))
    return dice
def who_win(user,system):
    user_sum = sum(user)
    system_sum = sum(system)
    if user_sum>system_sum :
       print('user win')
    elif user_sum<system_sum :
       print('system win')
    else:
       print('tie')
num_dice = int(input('擲骰子的次數:'))
user = roll_dice(n=num_dice)
system = roll_dice(n=num_dice)

print('user',user,sum(user))
print('system',system,sum(system))

who_win(user,system)






