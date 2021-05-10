'''
    # 封装 :
        1,将属性全部对外隐藏
            将属性前面加上两个下划线
        2,提供方法，间接能对属性进行赋值
            提供一个setxxx/getxxx用于赋值和获取值
'''

class watercup:
    __height = ""  # 高度
    __volume = ""  # 容积
    __colour = ""  # 颜色
    __texture = "" # 材质

    def setheight(self,height):
        self.__height = height
    def getheight(self):
        return self.__height


    def setvolume(self,volume):
        self.__volume = volume
    def getvolume(self):
        return self.__volume


    def setcolour(self,colour):
        self.__colour = colour
    def getcolour(self):
        return self.__colour


    def settexture(self,texture):
        self.__texture = texture
    def gettexture(self):
        return self.__texture

    def show(self):
        print("水杯高度为",self.__height,"水杯容积为",self.__volume,"水杯颜色为",self.__colour,"水杯材质为",self.__texture)
sb = watercup()
sb.setheight("1m")
sb.setvolume("8l")
sb.setcolour("透明色")
sb.settexture("塑料")
sb.show()