#-*- encoding:gbk-*-
tp =open(file="1.png",mode="rb")
zp = open(file="E:\\Python\\day01\\zhipiao.jpg",mode="wb")

qqq=tp.read()
zp.write(qqq)

zp.close()
tp.close()
