'''
    笔记本电脑：
            屏幕大小，价格，cpu型号，内存大小，待机时长
            行为（打字，打游戏，看视频）
'''


class notebook:
    __size = ""
    __price = ""
    __CPU = ""
    __memory = ""
    __time = ""

    def setsize(self,size):
        self.__size = size
    def getsize(self):
        return self.__size

    def setprice(self,price):
        self.__price = price
    def getprice(self):
        return self.__price

    def setCPU(self,CPU):
        self.__CPU = CPU
    def getCPU(self):
        return self.__CPU

    def setmemory(self,memory):
        self.__memory = memory
    def getmemory(self):
        return self.__memory

    def settime(self,time):
        self.__time = time
    def gettime(self):
        return self.__time

    # 打字
    def dz(self,type):
        print(self.__price,"的电脑",type)
    # 打游戏
    def dyx(self,dayouxi):
        print(self.__price,"的电脑",dayouxi)
    # 看视频
    def ksp(self,kanshipin):
        print(self.__price,"的电脑",kanshipin)

    def show(self):
        print("电脑屏幕大小为",self.__size,"电脑价格为",self.__price,"电脑CPU为",self.__CPU,"电脑内存大小为",self.__memory,
              "电脑待机时长为",self.__time)

bjb = notebook()
bjb.setsize("8寸")
bjb.setprice("5000")
bjb.setCPU("11")
bjb.setmemory("15")
bjb.settime("24")
bjb.show()
bjb.ksp("看视频")
bjb.dyx("打游戏")
bjb.dz("打字")

