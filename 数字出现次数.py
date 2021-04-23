list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0
b = 0
while True:
    if b < len(list):
        if list[b] ==1:
            a1=a1+1
        elif  list[b]==2:
            a2=a2+1
        elif  list[b]==3:
            a3=a3+1
        elif  list[b]==4:
            a4=a4+1
        elif  list[b]==5:
            a5=a5+1
        elif  list[b]==6:
            a6=a6+1
        elif  list[b]==7:
            a7=a7+1
        elif  list[b]==8:
            a8=a8+1
        elif  list[b]==9:
            a9=a9+1
        elif  list[b]==10:
            a10=a10+1
        b=b+1
    else:
        print("a1的次数：",a1)
        print("a2的次数：",a2)
        print("a3的次数：",a3)
        print("a4的次数：",a4)
        print("a5的次数：",a5)
        print("a6的次数：",a6)
        print("a7的次数：",a7)
        print("a8的次数：",a8)
        print("a9的次数：",a9)
        print("a10的次数：",a10)
        break