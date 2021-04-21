# 1号衣服
date1=1
name1="羽绒服"
price1=253.6
num1=500
sales1=10
# 2号衣服
date2=2
name2="牛仔裤"
price2=86.3
num2=600
sales2=60
# 3号衣服
date3=3
name3="风衣"
price3=96.8
num3=335
sales3=43
# 4号衣服
date4=4
name4="皮草"
price4=135.9
num4=855
sales4=63
# 5号衣服
date5=5
name5="T恤"
price5=65.8
num5=632
sales5=63
# 6号衣服
date6=6
name6="衬衫"
price6=49.3
num6=562
sales6=120
# 7号衣服
date7=7
name7="牛仔裤"
price7=86.3
num7=600
sales7=72
# 8号衣服
date8=8
name8="羽绒服"
price8=253.6
num8=500
sales8=69
# 9号衣服
date9=9
name9="牛仔裤"
price9=86.3
num9=600
sales9=35
# 10号衣服
date10=10
name10="羽绒服"
price10=253.6
num10=500
sales10=140
# 11号衣服
date11=11
name11="牛仔裤"
price11=86.3
num11=600
sales11=90
# 12号衣服
date12=12
name12="皮草"
price12=135.9
num12=855
sales12=24
# 13号衣服
date13=13
name13="T恤"
price13=65.8
num13=632
sales13=45
# 14号衣服
date14=14
name14="风衣"
price14=96.8
num14=335
sales14=25
# 15号衣服
date15=15
name15="牛仔裤"
price15=86.3
num15=600
sales15=60
# 16号衣服
date16=16
name16="T恤"
price16=65.8
num16=632
sales16=129
# 17号衣服
date17=17
name17="羽绒服"
price17=253.6
num17=500
sales17=10
# 18号衣服
date18=18
name18="风衣"
price18=96.8
num18=335
sales18=43
# 19号衣服
date19=19
name19="T恤"
price19=65.8
num19=632
sales19=63
# 20号衣服
date20=20
name20="牛仔裤"
price20=86.3
num20=600
sales20=60
# 21号衣服
date21=21
name21="皮草"
price21=135.9
num21=855
sales21=63
# 22号衣服
date22=22
name22="风衣"
price22=96.8
num22=335
sales22=60
# 23号衣服
date23=23
name23="T恤"
price23=65.8
num23=632
sales23=58
# 24号衣服
date24=24
name24="牛仔裤"
price24=86.3
num24=600
sales24=140
# 25号衣服
date25=25
name25="T恤"
price25=65.8
num25=632
sales25=48
# 26号衣服
date26=26
name26="风衣"
price26=96.8
num26=335
sales26=43
# 27号衣服
date27=27
name27="皮草"
price27=135.9
num27=855
sales27=57
# 28号衣服
date28=28
name28="羽绒服"
price28=253.6
num28=500
sales28=10
# 29号衣服
date29=29
name29="T恤"
price29=65.8
num29=632
sales29=63
# 30号衣服
date30=30
name30="风衣"
price30=96.8
num30=335
sales30=78

# 所有种类衣服的库存量
lnventory=num1+num2+num3+num4+num5+num6

# 本月所有种类衣服的销售量
down=(sales1+sales2+sales3+sales4+sales5+sales6+sales7+sales8+sales9+sales10+sales11+sales12+sales13+sales14+sales15+sales16+sales17+sales18+sales19+sales20+sales21+sales22+sales23+sales24+sales25+sales26+sales27+sales28+sales29+sales30)

#羽绒服在本月的总销售额
jackets=(sales1+sales8+sales10+sales17+sales28)*253.6

#牛仔裤在本月的总销售额
jeans=(sales2+sales7+sales9+sales11+sales15+sales20+sales24)*86.3

#风衣在本月的总销售额
wind=(sales3+sales14+sales18+sales22+sales26+sales30)*96.8

#皮草在本月的总销售额
fur=(sales4+sales12+sales21+sales27)*135.9

#T恤在本月的总销售额
shirt=(sales5+sales13+sales16+sales19+sales23+sales25+sales29)*65.8

#衬衫在本月的总销售额
str=sales6*price6
print("-------------------------12月份衣服销售数据---------------------------------------")
print("日期     服装名称     价格/件     库存数量    销售量/每日")
print("-------------------------------------------------------------------------------")
print(date1,"\t\t",name1,"\t\t",price1,"\t\t",num1,"\t\t",sales1,"\t\t")
print(date2,"\t\t",name2,"\t\t",price2,"\t\t",num2,"\t\t",sales2,"\t\t")
print(date3,"\t\t",name3,"\t\t",price3,"\t\t",num3,"\t\t",sales3,"\t\t")
print(date4,"\t\t",name4,"\t\t",price4,"\t\t",num4,"\t\t",sales4,"\t\t")
print(date5,"\t\t",name5,"\t\t",price5,"\t\t",num5,"\t\t",sales5,"\t\t")
print(date6,"\t\t",name6,"\t\t",price6,"\t\t",num6,"\t\t",sales6,"\t\t")
print(date7,"\t\t",name7,"\t\t",price7,"\t\t",num7,"\t\t",sales7,"\t\t")
print(date8,"\t\t",name8,"\t\t",price8,"\t\t",num8,"\t\t",sales8,"\t\t")
print(date9,"\t\t",name9,"\t\t",price9,"\t\t",num9,"\t\t",sales9,"\t\t")
print(date10,"\t\t",name10,"\t\t",price10,"\t\t",num10,"\t\t",sales10,"\t\t")
print(date11,"\t\t",name11,"\t\t",price11,"\t\t",num11,"\t\t",sales11,"\t\t")
print(date12,"\t\t",name12,"\t\t",price12,"\t\t",num12,"\t\t",sales12,"\t\t")
print(date13,"\t\t",name13,"\t\t",price13,"\t\t",num13,"\t\t",sales13,"\t\t")
print(date14,"\t\t",name14,"\t\t",price14,"\t\t",num14,"\t\t",sales14,"\t\t")
print(date15,"\t\t",name15,"\t\t",price15,"\t\t",num15,"\t\t",sales15,"\t\t")
print(date16,"\t\t",name16,"\t\t",price16,"\t\t",num16,"\t\t",sales16,"\t\t")
print(date17,"\t\t",name17,"\t\t",price17,"\t\t",num17,"\t\t",sales17,"\t\t")
print(date18,"\t\t",name18,"\t\t",price18,"\t\t",num18,"\t\t",sales18,"\t\t")
print(date19,"\t\t",name19,"\t\t",price19,"\t\t",num19,"\t\t",sales19,"\t\t")
print(date20,"\t\t",name20,"\t\t",price20,"\t\t",num20,"\t\t",sales20,"\t\t")
print(date21,"\t\t",name21,"\t\t",price21,"\t\t",num21,"\t\t",sales21,"\t\t")
print(date22,"\t\t",name22,"\t\t",price22,"\t\t",num22,"\t\t",sales22,"\t\t")
print(date23,"\t\t",name23,"\t\t",price23,"\t\t",num23,"\t\t",sales23,"\t\t")
print(date24,"\t\t",name24,"\t\t",price24,"\t\t",num24,"\t\t",sales24,"\t\t")
print(date25,"\t\t",name25,"\t\t",price25,"\t\t",num25,"\t\t",sales25,"\t\t")
print(date26,"\t\t",name26,"\t\t",price26,"\t\t",num26,"\t\t",sales26,"\t\t")
print(date27,"\t\t",name27,"\t\t",price27,"\t\t",num27,"\t\t",sales27,"\t\t")
print(date28,"\t\t",name28,"\t\t",price28,"\t\t",num28,"\t\t",sales28,"\t\t")
print(date29,"\t\t",name29,"\t\t",price29,"\t\t",num29,"\t\t",sales29,"\t\t")
print(date30,"\t\t",name30,"\t\t",price30,"\t\t",num30,"\t\t",sales30,"\t\t")
print("每件衣服的销售占比为：￥",(lnventory/down))
print("羽绒服的销售额占比为：￥",(253.6/jackets))
print("牛仔裤的销售额占比为：￥",(86.3/jeans))
print("风衣的销售额占比为：￥",(96.8/wind))
print("皮草的销售额占比为：￥",(135.9/fur))
print("T恤的销售额占比为：￥",(65.8/shirt))
print("衬衫的销售额占比为：￥",(49.3/str))
print("本月总销售额为：￥",(jackets+jeans+wind+fur+shirt+str))