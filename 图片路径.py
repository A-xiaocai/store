url = input("请输入图片路径：")
a = open(file=url,mode="rb")
import random
z = random.randint(0,9999999999)
c = open(file="E:\Python\day01\\" + str(z) +".jpg",mode="wb")


b = a.read()
c.write(b)

c.close()
a.close()
print("上传成功！！！")
