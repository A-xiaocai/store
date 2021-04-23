list = [1,2,3,4,5,6,7,8,9]
last = []
b = len(list)
c = 0
while c < len(list):
    last.append(list[b - 1])
    b = b - 1
    c = c + 1
list = last
print("list = ",list)



