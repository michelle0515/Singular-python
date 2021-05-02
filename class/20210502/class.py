'''
初始血量:10點
初始錢:0元
冒險者攻擊力:1-3點
怪物攻擊力:1點
獲得紅藥水:1-3點血量
獲得錢袋:10-30元
擊敗怪物可以獲得10-20元
回合制，冒險者有先攻擊的優先權
冒險者隨機對怪物產生1-3點傷害
怪物生命隨機2-10點，攻擊力1點
戰鬥結束後，更新冒險者狀態
status[0] = 1活著，0死亡
status[1] = 剩餘生命
status[2] = 剩餘金幣
'''
import random
def update_life(life):
    get_life=random.randit(1,3)
    new_life=life+get_life
    print('RecoveryLife=%d Your life %d'%(get_life,new_life)
    return new_life

def update_money(money):
    get_money=random.randit(10,20)
    new_money=money+get_money
    print('RecoveryMoney=%d Your money %d'%(get_money,new_money)
    return new_money

def fighting(life,money):
    status=[0,0,0]
    monster_life=random.randint(2,10)
    print('Monster Life = %d'%monster_life)
    while True:
        attack=random.randit(1,3)
        print('You Make Damage%d'%attack)
        monster_life-=attack
        time.sleep(1)
        print('Monster Life %d'%monster_life)

        if(monster_life<1):
           print('You beat monster')
           money+=random.randint(10,20)
           status[0]=1
           status[1]=life
           status[2]=money
          return status

        print('Monster atteck')
        life-=1
        print('You get hurt,My life %d'%my_life)

        if(my_life<1):
           print('You dead')
           status[0]=0
           status[1]=life
           status[2]=money
    return status
sts=[1,10,0]
while True:
    rev=input("Do you want 'c' continue or 'q' quit the game？")
    if(rev=='c'):
       gen_event=random.randint(1,3)
       if(gen_event==1):
           sts[1]=life(sts[1])
           if(gen_event==2):
               sts[2]=money(sts[2])
               if(gen_event==3):
                   sts=fighting(sts[1],sts[2])
                   if(sts[0]==0):
                       print('game over')
                       break
                    print('sts=%s'%sts)
    elif(rev==q):
        print('bye')
        break
    else:
        continue





















