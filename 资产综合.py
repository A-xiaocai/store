import pymysql
# 连接数据库，并获取连接
con = pymysql.connect(host="localhost",user="root",password="",database="银行数据库")

# 通过连接创建数据台
cursor = con.cursor()
d = []
average = 0
# 准备一条sql语句
a = open(file = "用户.txt",mode= "r+",encoding="utf-8")
b = a.readlines()
for i in b:
    c = i.replace("\n","").split(",")
    d.append(c)
for j in d:
    sql = ("insert into article values (%s,%s,%s)")
    param = (j[0],j[1],j[2])
    cursor.execute(sql,param)
    con.commit()
    average = average + int(j[2])
print("所有人资产综合为：",average,)
