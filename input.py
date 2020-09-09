"""
name = input("input name: ")
print(name)


x = int(input("input number: "))
print(x * 2)
"""



# 숫자 맞추기 게임
import random

rannum = random.randint(1, 20)
n = 1
chance = 4
for i in range(1, 5):
    print("기회가 {}번 남았습니다. ".format(chance))
    num = int(input("1-20 사이의 숫자를 맞춰보세요: "))
    if rannum == num:
        print("축하합니다. {}번 만에 숫자를 맞추셨습니다.".format(n))
        n += 1
        chance -= 1
        break
    elif rannum > num:
        print("Up")
        n += 1
        chance -= 1
        if chance == 0:
            print("아쉽습니다. 정답은 {}입니다.".format(rannum))
    elif rannum < num:
        print("Down")
        n += 1
        chance -= 1
        if chance == 0:
            print("아쉽습니다. 정답은 {}입니다.".format(rannum))

