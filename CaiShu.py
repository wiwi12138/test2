import random

mun2=random.randint(1,100)
# print(mun2)
while True:
    mun1 = int(input("请输入一个数据:"))
    if mun1>mun2 :
        print("猜小一点")

    elif mun1< mun2 :
        print("猜大一点")

    elif mun1==mun2:
        print("猜对了")
        break

