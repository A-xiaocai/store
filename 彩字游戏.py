
import random
num = random.randint(0,101)
count = 0
G=999
while True:
    count = count + 1
    G=G-10
    num1 = input("请输入您要猜的数:")
    num1 = int(num1)
    if num1 > num:
        print("大了！")
    elif num1 < num:
        print("小了！")
    else:
        print("恭喜你！猜中了！本次中奖号码为：",num,",您本次猜了",count,"次！","剩余金币",G)
        break

