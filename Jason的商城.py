hyjg = 5000
nfjg = 3000
import random
list1 = ["海洋之心优惠券，满600-300",

         "南非溏心钻优惠券，半折甩卖" ]

a = random.choice(list1)
print("恭喜你获得，",a, "快去购物吧")
shop = [
    ["海洋之心", 5000],
    ["南非溏心钻", 3000],
    ["紫水晶", 3000],
    ["紫水晶", 3.5],
    ["钻石", 50],
    ["旺仔厉害糖", 50]
]
sy = input("请输入您的薪资：")
salary = int(sy)
mycart = []

while True:
    print("-------------欢迎来到Jason的商城--------------------")
    for index, value in enumerate(shop):
        print(index, "  ", value)

    num = input("请输入您要买的商品编号：")

    if num.isdigit():
        num = int(num)
        if num >= len(shop):
            print("商品不存在！！！请重新输入！！！")
        else:
            if salary >= shop[num][1]:
                mycart.append(shop[num])
                salary1 = salary - (shop[num][1]-300)

            else:
                print("对不起，穷鬼，您的金额不足！！！！")
    elif num == "Q" or num == "q":

        print("--------------欢迎下次光临！！！再见----------------")
        break

    else:
        print("输入非法！！！！请重新输入！！！！！")

jf = (salary - salary1) / 10
print("您本次购物商品如下：")
for index, value in enumerate(mycart):
    print(index, "  ", value)
print("您的余额为：", salary1)
print("您的积分为：", jf)
print("本次优惠300元，谢谢惠顾。")