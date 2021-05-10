a = open(file="scores.txt",mode="r+",encoding="utf-8")
# a.write("罗恩 23 35 44\n")
# a.write("哈利 60 77 68 88 90\n")
# a.write("赫敏 97 99 89 91 95 90\n")
# a.write("马尔福 100 85 90")
z =[]
b = a.readlines()
for i in b:
    c = i.replace("\n","").replace(" ",",").split(",")
    for j in c:
        if j.isdigit():
            z.append(j)
z = [int(x) for x in z]
x = sum(z)
print("成绩总和为：",x)
