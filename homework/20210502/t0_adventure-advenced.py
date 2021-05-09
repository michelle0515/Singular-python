'''
尋問用魔法/普通攻擊
增加魔法攻擊(4-8點攻擊力)，每次需使用1點魔力
新增商店(m(回魔)/l(回血)/q(離開))
  回魔藥水，一瓶100元/2-4點魔力，錢不夠無法購買
  回血藥水，一瓶100元/3-6點體力，錢不夠無法購買
'''
import random
import time
def update_life(status: list):
    get_life = random.randint(1, 3)
    status[1] += get_life
    print("Recovry Life = %d Your life = %d" % (get_life, status[1]))
    return status


def update_money(status: list):
    get_money = random.randint(10, 30)
    status[2] += get_money
    print("Get Money = %d Your Money = %d" % (get_money, status[2]))
    return status


def fighting(status: list):
    s = 0.5  # attack speed
    monster_life = random.randint(2, 10)
    print("Monster Life = %d" % monster_life)

    while True:
        while True:
            act = input("Use 'm' for magic,'n' for normal,'r' for reef: ")
            if (act == 'm'):
                if status[3] >= 1:
                    attack = random.randint(4, 10) + status[4]
                    status[3] -= 1
                    break
                else:
                    print('not enough')
                    attack = random.randint(1, 3) + status[4]
                    break
            elif act == 'n':
                attack = random.randint(1, 3) + status[4]
                break
            elif act == 'r':
                if status[5] >= 1:
                    attack = monster_life
                    status[5] -= 1
                else:
                    print('not enough')
                    attack = random.randint(1, 3) + status[4]
                    break


        print("You make damage %d" % attack)
        monster_life -= attack
        time.sleep(s)
        print("Monster Life %d" % monster_life)

        if (monster_life < 1):
            print("You beat monster")
            status[2] += random.randint(10, 20)
            return status
        else:
            print("Monster Attack")
            status[1] -= 1
            time.sleep(s)
            print("You hurt, Life = %d" % status[1])

            if (status[1] < 1):
                print("You dead")
                status[0] = 0
                return status


def store(status: list):
    while True:
        if (status[2] < 100):
            print("Money is not enough, quit store ")
            break

        act = input("What do you want to buy 'l'/life,'m'/magic,'w'/weapon,'r'/reef,'q'/quit:")

        if (act == 'q'):
            print("88")
            break
        elif (act == 'l'):
            status[1] += random.randint(1, 3)
            status[2] -= 100
            print("Life=%d, Money=%d" % (status[1], status[2]))
        elif (act == 'm'):
            status[3] += random.randint(1, 3)
            status[2] -= 100
            print("Magic=%d, Money=%d" % (status[3], status[2]))
        elif (act == 'w'):
            status[4] += random.randint(1, 3)
            status[2] -= 100
            print("Weapon=%d, Money=%d" % (status[4], status[2]))
        elif (act == 'r'):
            status[5] += random.randint(1, 3)
            status[2] -= 500
            print("Weapon=%d, Money=%d" % (status[4], status[2]))
        else:
            continue
    return status

#main program
sts = [1, 10, 0, 10, 0, 0]
event_list = [update_life, update_money, fighting, store]
while True:
    '''
    rev = input("Do you want 'c' continue 'q' quit the game:")
    if (rev == "c"):
        sts = event_list[random.randint(0, len(event_list) - 1)](sts)
        if (sts[0] == 0):
            print("Game Over")
            break
        print("[[life = %d, money = %d, MP = %d]]" % (sts[1], sts[2], sts[3]))
    elif (rev == "q"):
        print("88")
        break
    else:
        continue
    '''
    sts = event_list[random.randint(0, len(event_list) - 1)](sts)
    if (sts[0] == 0):
        print("Game Over")
        break
    print("[[life = %d, money = %d, MP = %d, W= %d]]" % (sts[1], sts[2], sts[3], sts[4]))
    time.sleep(1)

