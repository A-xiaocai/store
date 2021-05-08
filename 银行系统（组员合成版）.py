import random
from DBUtils1 import update
from DBUtils1 import select

# 导包、全局变量
# 1. 空的银行的库 ： 100个


# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    sql = "select * from bank"
    data = select(sql,[])

    if len(data) >= 100:
        return 3
    # 判断是否存在
    sqll = "select * from bank where account = %s"
    data1 = select(sqll,account)
    if len(data1) != 0:
        return 2

    #正常开户
    #数据存到数据库里
    sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account,username,password,country,province,street,door,0.0,bank_name]
    update(sql2,param)
    return 1
# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    username = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,username,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        # import pymysql
        # con=pymysql.connect(host="localhost",user="root",password="",database="bank")
        # cursor=con.cursor()
        sql="select *  from bank where account = %s"
        # cursor.execute(sql,account)
        data = select(sql,account)
        # cursor.close()
        # con.close()

        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8]))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

#2.存款逻辑（刘钧建负责）

def bank_cunkuang(account,money):
    sql = "select * from bank where account = %s"
    data = select(sql,account)
    if len(data) != 0:
        sql1 = "update bank set money = money + %s where account = %s"
        update(sql1,[money,account])
        return True
    else:
        return False
#2.存款方法
def addmoney():
    account = input("请输入您的银行账号;")
    money = input("请输入您的存钱金额：")

    ck = bank_cunkuang(account,money)
    if ck == True:
        print("ATM机存钱成功")
    elif ck == False:
        print("ATM机存款失败！！！！")

#3 用户取钱的逻辑（宫思瑾负责）
def bank_getmoney(account,password,getmoney):
    sql = "select * from bank where account = %s"
    data = select(sql,account)
    if len(data) != 0:
        sql = "select account from bank where password = %s"
        data1 = select(sql,password)
        if len(data1) != 0:
            sql2 = "select * from bank where account = %s and money >= %s"
            data2 = select(sql2,[account,getmoney])
            if len(data2) != 0 :
                sql3 = "update bank set money = money - %s where account = %s"
                update(sql3,[getmoney,account])
                return  0
            else:
                return  3
        else:
            return 2
    else:
        return 1



#3 取钱方法：
def getmoney():
    account=input("请输入账号：")
    password=input("请输入密码：")
    getmoney=input("请输入您要取的金额：")
    money1= bank_getmoney(account, password, getmoney)
    if money1 == 0:
        print("恭喜你，取款成功")
    elif money1 == 1:
        print("账号不存在！")
    elif money1 == 2:
        print("密码错误！")
    elif money1 == 3:
        print("你的钱不够！")
#4转账逻辑（唐彪杰负责）
def money_transfer(outuser,takeinuser,password,outmoney):
    sql = "select * from bank where account = %s "
    data = select(sql,outuser)
    if len(data) != 0:
        sql = "select * from bank where account = %s"
        data1 = select(sql,takeinuser)
        if len(data1) != 0:
            sql2 = "select * from bank where account = %s and password = %s"
            data2 = select(sql2,[outuser,password])
            if len(data2) != 0:
                sql3 = "select * from bank where account = %s and money >= %s"
                data3 = select(sql3,[outuser,outmoney])
                if len(data3) != 0:
                    sql4 = "update bank set money = money - %s where account = %s"
                    update(sql4,[outmoney,outuser])
                    sql5 = "update bank set money = money + %s where account = %s"
                    update(sql5,[outmoney,takeinuser])
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    else:
        return 1


#4转账
def out_money():
    outuser=input("请输入转账账号：")
    takeinuser=input("请输入收款账号：")
    password=input("请输入转账账号密码：")
    outmoney=input("请输入转账金额：")
    if outmoney.isdigit():
        outmoney=int(outmoney)
        status=money_transfer(outuser,takeinuser,password,outmoney)
        if status==1:
            print("您输入的账号错误！！！")
        elif status==2:
            print("您输入的密码错误！！！")
        elif status==3:
            print("您账号余额不足！！！")
        elif status==0:
            print("转账成功！")
    else:
        print("输入非法字符！！！")

#查询（陈鑫涛负责）
def bank_chaxun(u,p):
    sql = "select * from bank where account = %s"
    data =select(sql,u)
    if data != 0:
        sql = "select account from bank where password = %s"
        data1 = select(sql,p)
        if data1 != 0:
            return 1
        else:
            return 2
    else:
        return 3

def chaxun():
    u = input("请输入您的账号")
    p = input("请输入您的密码")
    xinxi = bank_chaxun(u,p)
    if xinxi == 1:
        sql2 = "select * from bank where account = %s and password = %s"
        data1 = select(sql2,[u,p])
        if data1 !=0:
            print("您的信息如下：")
            print("您的账号为",data1[0][0],"您的密码为",data1[0][1],"您的国家为",data1[0][2],"您的省份为",data1[0][3],
                  "您的街道为",data1[0][4],"您的门牌号为",data1[0][5],"您的金额为",data1[0][6],"开户行",data1[0][7])
    elif xinxi == 2:
        print("密码错误！！")
    elif xinxi == 3:
        print("用户不存在，请重新输入！！！")






while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            addmoney()
        elif num == 3:
            getmoney()
        elif num == 4:
            out_money()
        elif num == 5:
            chaxun()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            DBUtils.close
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")


