'''
    条件：
        6个厨师同时造面包
        造完把面包扔进篮子里面
        5个窗外有5个人抢，面包
        面包篮子只能存300个
        厨师如果发现满了停3秒，再继续放
        面包10块钱1个
    任务：
        5分钟内，统计厨师总共造了多少个，
        顾客买了多少个，每个顾客花了多少钱
'''
lz = 0
mb = 0
money = 0
mainum = 0
shij = 0

import threading
import time
class shijian(threading.Thread):
    def run(self) -> None:
        global shij
        while shij < 300:
            time.sleep(1)
            shij = shij + 1

class chushi(threading.Thread):
    chush = ""
    def run(self) -> None:
        global shij
        global lz
        global mb
        while shij < 300:
            if lz >=300:
                time.sleep(3)
            else:
                mb = mb + 1
                lz = lz + 1
        print("5分钟做了",mb,"个面包！！")
class guke(threading.Thread):
    guk = ""
    def run(self) -> None:
        global lz
        global money
        global mainum
        while shij < 300:
            if lz <= 0:
                print("当前没有面包")
            else:
                mainum = mainum + 1
                money = mainum * 10
                print(self.guk,"买了",mainum,"个面包花了",money,"元")
g1 = guke()
g2 = guke()
g3 = guke()
g4 = guke()
g5 = guke()
g1.guk = "1"
g2.guk = "2"
g3.guk = "3"
g4.guk = "4"
g5.guk = "5"
g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
c1 = chushi()
c2 = chushi()
c3 = chushi()
c4 = chushi()
c5 = chushi()
c6 = chushi()
c1.chush = "甲"
c2.chush = "乙"
c3.chush = "丙"
c4.chush = "钉"
c5.chush = "锤"
c6.chush = "铁"
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
ti = shijian()
ti.start()
























