a = int(input("a边为："))
b = int(input("b边为："))
c = int(input("c边为："))
# 不能构成三角形的形成条件
if a+b<=c or a-b>=c :
    print("不能构成三角形")

# 等边三角形形成条件
elif a==b==c:
    print("等边三角形")

# 等腰三角形形成条件
elif a==b!=c or a==c!=b or b==c!=a:
    print("等腰三角形")
elif a^2+b^2==c^2 :
    print("直角三角形")
# 普通三角形形成条件
else :
    print("普通三角形")
