import pymysql
# 连接的四大参数，写死
host="localhost"
user="root"
password=""
database="银行数据库"

# 专门针对于增，删，改
def update(sql,param):
    # 2. 获取连接
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    # 3. 创建游标
    cursor = con.cursor()
    # 4.执行sql
    cursor.execute(sql,param)
    # 5.提交
    con.commit()

    # 6.关闭
    # cursor.close()
    # con.close()


# 专门针对于查询
def select(sql,param):
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    return cursor.fetchall()
     # 提交数据
    # cursor.close()
    # con.close()